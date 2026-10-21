r"""check.py — L146 (`data/hai/unfettered 0 prologue.txt`, 19 unita', righe 460-530). **CHIUDE IL FILE.**

Controlli propri: **2 `UI_LABEL` identiche al sorgente** (`back to choose`, `buy tripulse`) in `ID_OK` con controllo
dedicato, escluse da «tutte tradotte»; **4 token** in 4 unita' (`<origin>`, `<as before (run)>`, `<as before (flee)>`,
`<leave>`), due con **parentesi** confrontati **interi**; **28 virgolette e ZERO dispari** (l'assenza va dichiarata,
dopo due lotti con dispari); **17 tab**.
"""
import collections
import json
import os
import re
import sqlite3

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
missing = [u['idx'] for u in units if u['idx'] not in tr]
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
ID_OK = {1: 'back to choose', 8: 'buy tripulse'}
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 19/19", len(cov) == 19 == len(units) and not missing, '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 17 MISSION_TEXT + 2 UI_LABEL',
   collections.Counter(u['kind'] for u in units) == {'MISSION_TEXT': 17, 'UI_LABEL': 2},
   collections.Counter(u['kind'] for u in units))
ck('ID_OK: le 2 UI_LABEL sono IDENTICHE al sorgente, dichiarate e verificate',
   all(by[k]['italian'].lstrip('\t') == v == by[k]['english'].lstrip('\t') for k, v in ID_OK.items()),
   [(k, by[k]['italian'].lstrip('\t'), ID_OK[k]) for k in ID_OK if by[k]['italian'].lstrip('\t') != ID_OK[k]])
ck('un VALUE asserzione vuota: ZERO VALUE', [u['idx'] for u in units if u['kind'] == 'VALUE'] == [])
ck('tutte le unita di testo sono tradotte (le 2 UI_LABEL a parte)',
   not [v['idx'] for v in cov if v['idx'] not in ID_OK and v['italian'].strip() == v['english'].strip()])
ck('4 token, parita 1 = 1 per simbolo',
   dict(collections.Counter(t for u in units for t in TAGS.findall(u['english'])))
   == {'<origin>': 1, '<as before (run)>': 1, '<as before (flee)>': 1, '<leave>': 1})
ck('i token stanno nelle stesse unita: 9, 11, 13, 17',
   [u['idx'] for u in units if TAGS.findall(u['english'])] == [9, 11, 13, 17]
   == [u['idx'] for u in cov if TAGS.findall(u['italian'])])
ck('token con parentesi confrontati INTERI, non spezzati',
   '<as before (run)>' in by[11]['italian'] and '<as before (flee)>' in by[13]['italian']
   and 'as before' not in by[11]['italian'].replace('<as before (run)>', ''))
ck('<as before (run)> e <as before (flee)> aprono la frase, come in inglese',
   by[11]['italian'].lstrip('\t').startswith('<as before (run)> riesci')
   and by[13]['italian'].lstrip('\t').startswith('<as before (flee)> fuggi'))
ck('<origin> al suo posto, dentro la frase («qui su <origin>»)', 'qui su <origin>, dato che' in by[9]['italian'])
ck('<leave> apre la frase seguita dalla maiuscola', by[17]['italian'].lstrip('\t').startswith("<leave> L'ingegnere"))
ck('28 virgolette in inglese e in italiano',
   sum(v['english'].count('"') for v in cov) == 28 == sum(v['italian'].count('"') for v in cov),
   (sum(v['english'].count('"') for v in cov), sum(v['italian'].count('"') for v in cov)))
ck('ZERO virgolette dispari (dichiarato: dopo L145 non ce ne sono)',
   [v['idx'] for v in units if v['english'].count('"') % 2] == []
   and [v['idx'] for v in cov if v['italian'].count('"') % 2] == [])
ck('virgolette per unita: stesso numero in tutte',
   not [v['idx'] for v in cov if v['english'].count('"') != v['italian'].count('"')])
tabs = [v['idx'] for v in cov if v['english'].startswith('\t')]
ck('17 unita iniziano con tab (le 2 UI_LABEL no)',
   len(tabs) == 17 and tabs == [v['idx'] for v in cov if v['italian'].startswith('\t')]
   and [v['idx'] for v in cov if not v['english'].startswith('\t')] == [1, 8], len(tabs))
ck('spazi iniziali e finali identici al sorgente (19/19)',
   not [v['idx'] for v in cov
        if len(v['italian']) - len(v['italian'].rstrip()) != len(v['english']) - len(v['english'].rstrip())])
ck('1 contesto: Jump Drive Trading, 19 unita',
   list(collections.Counter(v['context'] for v in cov).items()) == [('mission:Unfettered Jump Drive Trading', 19)])
ck('prima e ultima unita: righe 460 e 530', (cov[0]['line'], cov[-1]['line']) == (460, 530),
   (cov[0]['line'], cov[-1]['line']))
ck('19 testi distinti', len({v['english'] for v in cov}) == 19)
ck('i nomi restano inglesi: Tripulse Shredder, Sea Scorpion, Shield Beetle',
   all(n in ' '.join(v['italian'] for v in cov) for n in ('Tripulse Shredder', 'Sea Scorpion', 'Shield Beetle')))
ck('nessuna traduzione inventata dei nomi',
   not [n for n in ('Scorpione marino', 'Scorpione di mare', 'Scarabeo', 'Distruttore') if n in ' '.join(
       v['italian'] for v in cov)])
LOW = ' '.join(v['italian'] for v in cov).lower()
TERMS = ('bacheca dei lavori', 'motore di salto', 'camera blindata', 'portello', 'guerrieri', 'subordinati',
         'mordi e fuggi', 'raffica', 'alloggiamento')
ck('terminologia presente: 9 termini chiave', all(t in LOW for t in TERMS), [t for t in TERMS if t not in LOW])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ')
LONG = ' '.join(TAGS.sub('""', v['italian']) for v in cov).lower()
for s in ('tripulse shredder', 'sea scorpion', 'shield beetle', 'hai', '<origin>'):
    LONG = LONG.replace(s, '@@')
ck('nessun residuo inglese fuori dai nomi propri',
   not [w for w in ENGW if w in LONG], [w for w in ENGW if w in LONG])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', ' '.join(v['italian'] for v in cov))
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo'),
       ('\u00ab', 'caporale'), ('\u00bb', 'caporale')) if re.search(p, v['italian'])]
ck('tipografia', not bad, bad)
nonlat = [v['idx'] for v in cov for c in TAGS.sub('', v['italian'])
          if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini (fuori dai token)', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 19 unita sono PENDING nel database (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov),
                                 sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len(missing)))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
