r"""check.py — L199 (`data/hai/hai jobs.txt`, 26 unita', righe 1579-1750). Quarto lotto del file.

Cinque **famiglie** di eventi (cinema, musica, sicurezza informatica, fantascienza) in due taglie ciascuna, piu' il
primo pezzo di `Superstitious Hai [1]`, che continua in L200. **9 `VALUE`** (inglesi), **8 `DESCRIPTION`**, **9
`DIALOG`**.

Struttura da verificare come **relazioni**, non come uguaglianze isolate:
- le quattro coppie `[1]`/`[2]` differiscono **solo** per l'aggettivo `grande` (`un` -> `un grande`);
- le quattro coppie di `DIALOG` sono **identiche** dentro la coppia (4=7, 10=13, 16=19, 22=25);
- l'unita' 1 e' la stessa stringa gia' tradotta in L198 (chiusura della convention [1]): resa **identica**.

**Zero tab, zero virgolette** (asserzioni vuote scritte). **2 apici** inglesi (`passengers'`, idx 16 e 19) contro
**0** italiani: il possessivo inglese non ha equivalente con apostrofo. **42 segnaposto su 3 simboli**.
"""
import collections
import glob
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
units = sorted(src['units'], key=lambda x: x['line'])
tr = {}
parts = sorted(f for f in os.listdir(os.path.join(HERE, 'parts')) if f.endswith('.json'))
for p in parts:
    for k, v in json.load(open(os.path.join(HERE, 'parts', p), encoding='utf-8')).items():
        tr[int(k)] = v
out = {'block': src['block'], 'note': src['note'], 'units': []}
for u in units:
    if u['idx'] not in tr:
        continue
    it = tr[u['idx']]
    out['units'].append({"idx": u['idx'], "id": u['id'], "path": u['path'], "line": u['line'],
                         "kind": u['kind'], "context": u['context'], "english": u['english'],
                         "italian": it, "ratio": round(len(it) / max(1, len(u['english'])), 3)})
open(os.path.join(HERE, 'translation.json'), 'w', encoding='utf-8').write(
    json.dumps(out, ensure_ascii=False, indent=1))
cov = out['units']
by = {v['idx']: v for v in cov}
TAGS = re.compile(r'<[^<>]+>')
NON_VALUE = ' '.join(v['italian'] for v in cov if v['kind'] != 'VALUE')
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
PAIRS = [(3, 6), (9, 12), (15, 18), (21, 24)]
DIALOG_PAIRS = [(4, 7), (10, 13), (16, 19), (22, 25)]
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def strip_grande(s):
    return s.replace('un grande ', 'un ').replace('una grande ', 'una ')


def prior_italians(english):
    found = set()
    for f in glob.glob(os.path.join(L10N, 'staging/editorial/L*/translation.json')):
        if os.path.dirname(f) == HERE:
            continue
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        for u in d.get('units', []):
            if u.get('english') == english and u.get('italian'):
                found.add(u['italian'])
    return found


ck("unita' tradotte 26/26", len(cov) == 26 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 9 VALUE, 8 DESCRIPTION, 9 DIALOG (asserzione scritta)',
   KINDS == {'VALUE': 9, 'DESCRIPTION': 8, 'DIALOG': 9}, dict(KINDS))
ck('ZERO UI_LABEL, ZERO tab, ZERO TEXT (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] == 'UI_LABEL'] == []
   and [u['idx'] for u in units if u['kind'] == 'TEXT'] == []
   and [u['idx'] for u in units if u['english'].startswith(TAB)] == []
   and [v['idx'] for v in cov if v['italian'].startswith(TAB)] == [])
ctx = [u['context'].replace('mission:', '') for u in units]
ck('10 contesti distinti, da Swiftsong Business Convention [2] a Superstitious Hai [1]',
   len(set(ctx)) == 10 and (ctx[0], ctx[-1]) == ('Swiftsong Business Convention [2]', 'Superstitious Hai [1]'),
   '%d · %s · %s' % (len(set(ctx)), ctx[0], ctx[-1]))
ck('righe 1579 e 1750 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (1579, 1750), (cov[0]['line'], cov[-1]['line']))
EN_T = collections.Counter(t for u in units for t in TAGS.findall(u['english']))
IT_T = collections.Counter(t for v in cov for t in TAGS.findall(v['italian']))
ck('42 segnaposto su 3 simboli (payment 17, planet 17, bunks 8), stesso multiset',
   sum(EN_T.values()) == 42 and EN_T == {'<payment>': 17, '<planet>': 17, '<bunks>': 8} and EN_T == IT_T,
   (sum(EN_T.values()), dict(EN_T)))
ck('nessun <date>, <cargo> o <destination> in questo lotto (asserzione vuota scritta)',
   not [t for t in EN_T if t in ('<date>', '<cargo>', '<destination>')])
bad_tags = [(v['idx'], sorted(TAGS.findall(v['english'])), sorted(TAGS.findall(v['italian'])))
            for v in cov
            if collections.Counter(TAGS.findall(v['english'])) != collections.Counter(TAGS.findall(v['italian']))]
ck('nessuna unita\' perde, duplica o sposta un segnaposto', not bad_tags, bad_tags)
ck('9 VALUE identici all\'inglese, uno per uno',
   [v['idx'] for v in cov if v['kind'] == 'VALUE'] == [2, 5, 8, 11, 14, 17, 20, 23, 26]
   and all(v['italian'] == v['english'] for v in cov if v['kind'] == 'VALUE'))
ck('9 DIALOG tradotti (nessuno lasciato in inglese)',
   [v['idx'] for v in cov if v['kind'] == 'DIALOG'] == [1, 4, 7, 10, 13, 16, 19, 22, 25]
   and all(v['italian'] != v['english'] for v in cov if v['kind'] == 'DIALOG'))
ck('zero virgolette in entrambe le lingue (asserzione vuota scritta)', EN_Q == 0 == IT_Q, (EN_Q, IT_Q))
ck("apici: 2 inglesi (passengers', idx 16 e 19) e 0 italiani, causa: possessivo inglese",
   EN_A == 2 and IT_A == 0
   and [v['idx'] for v in cov if APOS in v['english']] == [16, 19], (EN_A, IT_A))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ')
ck('nessun residuo inglese fuori dai VALUE (che restano inglesi per convenzione)',
   not [w for w in ENGW if w in NON_VALUE.lower()], [w for w in ENGW if w in NON_VALUE.lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', IT_ALL)
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
ACC = re.compile(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", re.I)
bad = [(v['idx'], ACC.search(v['italian']).group(0)) for v in cov if ACC.search(v['italian'])]
ck('tipografia (accenti veri, nessun apostrofo al posto dell\'accento)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
ck('nessuno spazio finale e nessun doppio spazio',
   not [v['idx'] for v in cov if v['italian'] != v['italian'].rstrip()
        or '  ' in v['italian'] or v['english'] != v['english'].rstrip()])
ck('le quattro coppie [1]/[2] differiscono SOLO per «grande» (3-6, 9-12, 15-18, 21-24)',
   all(strip_grande(by[b]['italian']) == by[a]['italian'] for a, b in PAIRS)
   and all('grande' in by[b]['italian'] and 'grande' not in by[a]['italian'] for a, b in PAIRS),
   [(a, b, strip_grande(by[b]['italian']) == by[a]['italian']) for a, b in PAIRS])
ck('le quattro coppie di DIALOG sono identiche dentro la coppia (4=7, 10=13, 16=19, 22=25)',
   all(by[a]['italian'] == by[b]['italian'] and by[a]['english'] == by[b]['english'] for a, b in DIALOG_PAIRS))
ck('ogni famiglia ha il suo finale diverso (film, musica, sicurezza, fantascienza)',
   len({by[i]['italian'].split('dalla tua nave. ')[1] for i in (4, 10, 16, 22)}) == 4)
ck('il finale della musica nomina lo spazioporto; quello del cinema le trame sconcertanti',
   'spazioporto' in by[10]['italian'] and 'sconcertanti' in by[4]['italian'])
ck('unita\' 1: resa identica a quella gia\' in staging (L198, stessa stringa)',
   by[1]['italian'] in prior_italians(by[1]['english']))
ck('«movie buffs» compare solo nelle due unita\' del cinema (3, 6)',
   all('appassionati di cinema' in by[i]['italian'] for i in (3, 6))
   and not any('appassionati di cinema' in v['italian'] for v in cov if v['idx'] not in (3, 6)))
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 26 unita sono PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                sum(len(v['italian'].split()) for v in cov)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
