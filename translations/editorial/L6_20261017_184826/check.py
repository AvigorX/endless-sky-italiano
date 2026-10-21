import json, re, collections, hashlib, sqlite3

D = 'staging/editorial/L6_20261017_184826'
src = json.load(open(f'{D}/source.json'))
units = src['units']
tr = {}
for p in ('part01', 'part02', 'part03', 'part04'):
    for k, v in json.load(open(f'{D}/parts/{p}.json')).items():
        tr[int(k)] = v

out = {'block': src['block'], 'continues_from': src['continues_from'], 'units': []}
for u in units:
    it = tr[u['idx']]
    out['units'].append({
        "idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
        "context": u['context'], "english": u['english'], "italian": it,
        "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(f'{D}/translation.json', 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))

TAGS = re.compile(r'<[^<>]+>')
rows = []
rows.append(('indici attesi/presenti', f"{len(units)}/{len(out['units'])}",
             len(units) == len(out['units'])))
rows.append(('id allineati a source.json',
             all(a['id'] == b['id'] for a, b in zip(units, out['units'])),
             all(a['id'] == b['id'] for a, b in zip(units, out['units']))))
e = sum(1 for v in out['units'] if not v['italian'].strip())
rows.append(('traduzioni vuote', e, e == 0))
en = collections.Counter(v['english'] for v in out['units'])
it = collections.Counter(v['italian'] for v in out['units'])
de = [(k, c) for k, c in en.items() if c > 1]
di = [(k, c) for k, c in it.items() if c > 1]
rows.append(('duplicati english', len(de), True))
rows.append(('duplicati italiano', len(di), len(di) == 0))
tab = [(b['idx'], a['english'].count('\t'), b['italian'].count('\t'))
       for a, b in zip(units, out['units']) if a['english'].count('\t') != b['italian'].count('\t')]
rows.append(('tab per unita', tab or 'ok', not tab))
lead = [(a['idx'], b['idx']) for a, b in zip(units, out['units'])
        if a['english'].startswith('\t') != b['italian'].startswith('\t')]
rows.append(('tab iniziale conservato', lead or 'ok', not lead))
quo = [(b['idx'], a['english'].count('"'), b['italian'].count('"'))
       for a, b in zip(units, out['units']) if a['english'].count('"') != b['italian'].count('"')]
rows.append(('virgolette per unita', quo or 'ok', not quo))
tag = [b['idx'] for a, b in zip(units, out['units'])
       if collections.Counter(TAGS.findall(a['english'])) != collections.Counter(TAGS.findall(b['italian']))]
rows.append(('token <...>', tag or 'ok', not tag))
sp = [b['idx'] for b in out['units'] if '  ' in b['italian'] or b['italian'] != b['italian'].rstrip()
      or b['italian'].startswith(' ') or ' \t' in b['italian'] or '\t ' in b['italian']
      or '\n' in b['italian']]
rows.append(('spazi doppi/ai bordi', sp or 'ok', not sp))
rs = [v['ratio'] for v in out['units']]
rows.append(('rapporto lunghezza', '%.2f - %.2f' % (min(rs), max(rs)), min(rs) > 0.80 and max(rs) < 1.40))

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
res = [(v['idx'], sorted(set(m.group(0).lower() for m in ENG.finditer(v['italian'])))) for v in out['units'] if ENG.search(v['italian'])]
rows.append(('parole inglesi residue', res or 'nessuna', not res))

FOREIGN = ['standby', 'design', 'marketing', 'management', 'shipping', 'layout', 'feedback']
fo = [(v['idx'], w) for v in out['units'] for w in FOREIGN if re.search(r'\b%s\b' % w, v['italian'], re.I)]
rows.append(('anglicismi evitabili', fo or 'ok', not fo))

# integrita': state.db invariato, nessuna scrittura
c = sqlite3.connect('file:state.db?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
rows.append(('state.db APPROVED/PENDING', f"{st['APPROVED']}/{st['PENDING']}", st['APPROVED'] == 364))
last = c.execute("select max(updated_at) from units where state='APPROVED'").fetchone()[0]
rows.append(('ultimo aggiornamento APPROVED', last, last == '2026-10-17T14:33:18Z'))

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
print('coppia english duplicata:', [(k[:55], cnt, [v['idx'] for v in out['units'] if v['english'] == k]) for k, cnt in de])
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
