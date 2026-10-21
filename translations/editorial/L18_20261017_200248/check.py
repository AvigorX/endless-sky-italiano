import json, re, collections, sqlite3, os

D = 'staging/editorial/L18_20261017_200248'
src = json.load(open(f'{D}/source.json'))
units = src['units']
tr = {}
for p in ('part01', 'part02', 'part03', 'part04', 'part05', 'part06'):
    for k, v in json.load(open(f'{D}/parts/{p}.json')).items():
        tr[int(k)] = v

out = {'block': src['block'], 'continues_from': src['continues_from'], 'units': []}
for u in units:
    it = tr[u['idx']]
    out['units'].append({
        "idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
        "kind": u['kind'], "context": u['context'], "english": u['english'],
        "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(f'{D}/translation.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))

# --- classificazione: unita' che NON si traducono (elenco esplicito, motivato) ---
NT = {
    124: 'label "shoot and die" (bersaglio di goto)',
    131: 'label "more money" (bersaglio di goto)',
    137: 'label "shoot and live" (bersaglio di goto)',
    164: 'frammento tipografico: spazio + virgola di apertura',
    180: 'frammento tipografico: virgola di chiusura',
}
# duplicati ammessi perche' il sorgente ripete la stessa stringa (nome missione / testo identico)
DUP_OK = {1, 2, 20, 28, 29, 51, 52, 65, 77, 78, 79, 82, 83, 84, 87, 88, 89,
          97, 102, 108, 109, 111, 112, 114, 115, 116, 117,
          121, 122, 123, 128, 129, 130, 145, 148}

TAGS = re.compile(r'<[^<>]+>')
rows = []
rows.append(('indici attesi/presenti', f"{len(units)}/{len(out['units'])}",
             len(units) == len(out['units'])))
rows.append(('id allineati a source.json',
             all(a['id'] == b['id'] for a, b in zip(units, out['units'])),
             all(a['id'] == b['id'] for a, b in zip(units, out['units']))))
e = sum(1 for v in out['units'] if not v['italian'].strip())
rows.append(('traduzioni vuote', e, e == 0))

ident = [(v['idx'], v['english'], v['italian']) for v in out['units']
         if v['idx'] in NT and v['italian'] != v['english']]
rows.append((f'non traducibili lasciate identiche ({len(NT)})', ident or 'ok', not ident))

en = collections.Counter(v['english'] for v in out['units'])
it = collections.Counter(v['italian'] for v in out['units'])
de = [(k, c, [v['idx'] for v in out['units'] if v['english'] == k]) for k, c in en.items() if c > 1]
di = [(k, c, [v['idx'] for v in out['units'] if v['italian'] == k]) for k, c in it.items() if c > 1]
di = [d for d in di if not set(d[2]) <= DUP_OK]
rows.append(('duplicati english', [(k[:40], c, i) for k, c, i in de], True))
rows.append(('duplicati italiano', di or 'ok', len(di) == 0))

tab = [(b['idx'], a['english'].count('\t'), b['italian'].count('\t'))
       for a, b in zip(units, out['units']) if a['english'].count('\t') != b['italian'].count('\t')]
rows.append(('tab per unita', tab or 'ok', not tab))
lead = [a['idx'] for a, b in zip(units, out['units'])
        if a['english'].startswith('\t') != b['italian'].startswith('\t')]
rows.append(('tab iniziale conservato', lead or 'ok', not lead))
quo = [(b['idx'], a['english'].count('"'), b['italian'].count('"'))
       for a, b in zip(units, out['units']) if a['english'].count('"') != b['italian'].count('"')]
rows.append(('virgolette per unita', quo or 'ok', not quo))
tag = [b['idx'] for a, b in zip(units, out['units'])
       if collections.Counter(TAGS.findall(a['english'])) != collections.Counter(TAGS.findall(b['italian']))]
rows.append(('token <...>', tag or 'ok', not tag))
bt = [(b['idx'], a['english'].count('`'), b['italian'].count('`'))
      for a, b in zip(units, out['units']) if a['english'].count('`') != b['italian'].count('`')]
rows.append(('backtick per unita', bt or 'ok', not bt))

# --- spazio semantico: nei frammenti di phrase lo spazio iniziale/finale fa parte del testo ---
sig = [(b['idx'], a['english'][:1] == ' ', b['italian'][:1] == ' ', a['english'][-1:] == ' ', b['italian'][-1:] == ' ')
       for a, b in zip(units, out['units'])
       if (a['english'][:1] == ' ') != (b['italian'][:1] == ' ') or (a['english'][-1:] == ' ') != (b['italian'][-1:] == ' ')]
rows.append(('spazio iniziale/finale come il sorgente', sig or 'ok', not sig))
sp = [b['idx'] for a, b in zip(units, out['units'])
      if '  ' in b['italian'] and '  ' not in a['english']
      or b['italian'] != b['italian'].rstrip('\t') and not a['english'].endswith(' ')
      or ' \t' in b['italian'] or '\t ' in b['italian'] or '\n' in b['italian']
      or (b['italian'].startswith(' ') and not a['english'].startswith(' '))]
rows.append(('spazi doppi/ai bordi non voluti', sp or 'ok', not sp))

rs = [v['ratio'] for v in out['units']]
rows.append(('rapporto lunghezza', '%.2f - %.2f' % (min(rs), max(rs)), min(rs) > 0.55 and max(rs) < 1.90))

bad = []
for v in out['units']:
    s = v['italian']
    for pat, name in ((r"\b(e|E|piu|perche|cosi|gia|puo|cioe|percio)'", 'accento sostitutivo'),
                      ('\u2026', 'ellissi tipografica'), ('\u00ab', 'caporale'), ('\u00bb', 'caporale'),
                      ('\u2014', 'em dash'), ('\u2019', 'apostrofo curvo')):
        if re.search(pat, s):
            bad.append((v['idx'], name))
rows.append(('tipografia (accenti/apostrofi/dash)', bad or 'ok', not bad))

ENG = re.compile(r'\b(the|and|with|this|that|from|your|their|which|have|into|about|there|would|while|'
                 r'windows|but|are|was|were|they|his|her|its|be|been)\b', re.I)
TITLES = ('There Might Be Riots', 'Songs for the End of Civilization', 'Gluttony',
          'Trouble on the Tarmac Tour')
def scrub(s):
    for t in TITLES:
        s = s.replace(t, '')
    return s
res = [(v['idx'], sorted(set(m.group(0).lower() for m in ENG.finditer(scrub(v['italian'])))))
       for v in out['units'] if v['idx'] not in NT and ENG.search(scrub(v['italian']))]
rows.append(('parole inglesi residue (titoli esclusi)', res or 'nessuna', not res))

# --- composizione della phrase: i 10 slot devono dare una frase pulita in EN e in IT ---
def phrase_slots():
    path = '../endless-sky/data/human/human missions.txt'
    lines = open(path, encoding='utf-8').read().split('\n')
    start = next(i for i, l in enumerate(lines) if l.startswith('phrase "generic human package offer"'))
    slots, cur = [], None
    for i in range(start + 1, len(lines)):
        l = lines[i]
        if not l.startswith('\t'):
            break
        if l.strip() == 'word':
            cur = []
            slots.append(cur)
        elif l.strip().startswith('`'):
            cur.append((i + 1, l.strip()[1:-1]))
    return slots

slots = phrase_slots()
byline = {v['line']: v for v in out['units']}
# 11 slot: 5 soggetti, 1 spazio, 5 verbi, 1 virgoletta, 4 saluti, 1 spazio, 4 frasi,
# 1 spazio, 4 domande, 3 pagamenti, 1 virgoletta di chiusura (gli slot di solo spazio non sono unita')
rows.append(('phrase: 11 slot individuati', len(slots), len(slots) == 11))

def compose(which):
    parts = []
    for slot in slots:
        line, text = slot[0]
        u = byline.get(line)
        parts.append(u[which] if u else text)
    return ''.join(parts)

en_s, it_s = compose('english'), compose('italian')
print('EN composto:', repr(en_s[:300]))
print('IT composto:', repr(it_s[:300]))
for name, s in (('EN', en_s), ('IT', it_s)):
    rows.append((f'phrase {name}: nessuno spazio doppio', bool(re.search('  ', s)), not re.search('  ', s)))
    rows.append((f'phrase {name}: nessuno spazio prima di punteggiatura', bool(re.search(r' [,.;:!?]', s)),
                 not re.search(r' [,.;:!?]', s)))
    rows.append((f'phrase {name}: virgolette pari', s.count('"') % 2 == 0, s.count('"') % 2 == 0))
    if name == 'IT':  # in inglese il pronome "I" e' maiuscolo anche dopo virgola: test solo sull'italiano
        rows.append((f'phrase {name}: nessuna maiuscola dopo virgola', bool(re.search(r'[,;:]\s+[A-ZÀ-Ý]', s)),
                     not re.search(r'[,;:]\s+[A-ZÀ-Ý]', s)))
    rows.append((f'phrase {name}: nessuna minuscola dopo punto', bool(re.search(r'\.\s+[a-zà-ù]', s)),
                 not re.search(r'\.\s+[a-zà-ù]', s)))

c = sqlite3.connect('file:state.db?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
rows.append(('state.db APPROVED/PENDING', f"{st['APPROVED']}/{st['PENDING']}", st['APPROVED'] == 364))
last = c.execute("select max(updated_at) from units where state='APPROVED'").fetchone()[0]
rows.append(('ultimo aggiornamento APPROVED', last, last == '2026-10-17T14:33:18Z'))

print()
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for a, b, ok in rows:
    print('| %s | %s | %s |' % (a, b, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in out['units']),
                                 sum(len(v['italian'].split()) for v in out['units'])))
print('tab IT %d / EN %d' % (sum(v['italian'].count('\t') for v in out['units']),
                             sum(v['english'].count('\t') for v in units)))
print('virgolette IT %d / EN %d' % (sum(v['italian'].count('"') for v in out['units']),
                                    sum(v['english'].count('"') for v in units)))
print('token IT %d / EN %d' % (sum(len(TAGS.findall(v['italian'])) for v in out['units']),
                               sum(len(TAGS.findall(v['english'])) for v in units)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
