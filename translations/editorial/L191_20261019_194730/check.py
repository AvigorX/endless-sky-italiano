r"""check.py — L191 (`data/bunrodea/bunrodea missions.txt`, 12 unita', righe 16-52). **Apre il file.**

Primo lotto di **missione narrativa**: un solo contesto per dodici unita', **6 virgolette** di dialogo (idx 5, 6, 7),
**9 tab** e **1 segnaposto `<origin>`** (idx 3) che va conservato **alla lettera**. Controlli propri: le virgolette sono
diritte e pari in inglese e in italiano, il segnaposto c'e' in entrambe le lingue una volta sola, e le due varianti di
scelta (idx 11 e 12) condividono la **seconda meta'** con la stessa resa.
"""
import collections
import json
import os
import re
import sqlite3

TAB = chr(9)
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
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_Q = sum(v['english'].count('"') for v in cov)
IT_Q = sum(v['italian'].count('"') for v in cov)
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


ck("unita' tradotte 12/12", len(cov) == 12 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 10 MISSION_TEXT + 1 VALUE + 1 DESCRIPTION', collections.Counter(u['kind'] for u in units)
   == {'MISSION_TEXT': 10, 'VALUE': 1, 'DESCRIPTION': 1})
ck('il VALUE resta inglese (`An Intriguing Invitation`)',
   by[1]['kind'] == 'VALUE' and by[1]['italian'] == by[1]['english'] == 'An Intriguing Invitation')
ck("il segnaposto `<origin>` c'e' UNA volta in inglese e UNA in italiano, nella stessa unita'",
   {t for u in units for t in TAGS.findall(u['english'])} == {'<origin>'}
   == {t for v in cov for t in TAGS.findall(v['italian'])}
   and [v['idx'] for v in cov if '<origin>' in v['english']] == [3] == [v['idx'] for v in cov if '<origin>' in v['italian']])
ck('6 virgolette di dialogo, diritte, in inglese e in italiano',
   EN_Q == 6 == IT_Q and [v['idx'] for v in cov if '"' in v['english']] == [5, 6, 7]
   == [v['idx'] for v in cov if '"' in v['italian']], (EN_Q, IT_Q))
ck('nessun caporale e nessuna virgoletta tipografica in italiano',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d')])
ck('9 tab iniziali, in inglese e in italiano (idx 4-12)',
   [v['idx'] for v in cov if v['english'].startswith(TAB)] == list(range(4, 13))
   == [v['idx'] for v in cov if v['italian'].startswith(TAB)])
ck('le tre battute sono interrogativa, negazione, esclamativa (traduzione fedele)',
   'Vieni in pace?' in by[5]['italian'] and 'Non capisco una parola' in by[6]['italian']
   and 'Non sparare!' in by[7]['italian'])
ck('idx 9 e 10 sono due scelte brevi fra parentesi',
   by[9]['italian'].strip().startswith('(Raccoglilo') and by[10]['italian'].strip().startswith('(Schiva'))
ck('le due varianti 11 e 12 condividono la mappa, il sistema evidenziato e la partenza',
   all(x in by[11]['italian'] and x in by[12]['italian'] for x in
       ('mappa stellare olografica', 'Un solo sistema in quella regione è evidenziato',
        'la senti decollare e allontanarsi')))
ck('idx 11 e 12 differiscono solo nel primo tratto (raccogliere vs schivare)',
   'Raccogli il dispositivo' in by[11]['italian'] and 'Schivi e ti metti al riparo' in by[12]['italian']
   and 'Raccogli il dispositivo' not in by[12]['italian'])
ck('le creature sono «simili a mantidi» e hanno quattro zampe e due braccia (idx 3)',
   'simili a mantidi' in by[3]['italian'] and 'quattro lunghe zampe' in by[3]['italian']
   and 'due braccia' in by[3]['italian'])
ck("l'alieno modificato si distingue dall'altro (idx 4)",
   'modifiche cibernetiche' in by[4]['italian'] and "L'altro però non ha modifiche" in by[4]['italian'])
ck('12 unita, 11 testi inglesi distinti (11 e 12 differiscono)',
   len({v['english'] for v in cov}) == 12)
ck('UN solo contesto per tutte le unita', len({u['context'] for u in units}) == 1,
   {u['context'] for u in units})
ck('prima e ultima unita: righe 16 e 52',
   (cov[0]['line'], cov[-1]['line']) == (16, 52))
ck('nessuno spazio finale (tab iniziali ammessi)',
   not [v['idx'] for v in cov if v['english'].rstrip(TAB) != v['english'].rstrip(TAB).rstrip()
        or v['italian'].rstrip(TAB) != v['italian'].rstrip(TAB).rstrip()])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ')
ck('nessun residuo inglese fuori dal VALUE', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
CORT = re.findall(r'\bLei\b|(?<![.!?] )\b(?:Suo|Sua|Suoi|Sue)\b', IT_ALL)
ck('nessuna forma di cortesia «Lei»', not CORT, CORT)
rs = [v['ratio'] for v in cov]
ck('rapporto nel gate 0,55-1,90', 0.55 < min(rs) and max(rs) < 1.90, '%.2f - %.2f' % (min(rs), max(rs)))
bad = [(v['idx'], n) for v in cov for p, n in ((r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", 'accento'),
       ('\u2026', 'ellissi'), ('\u2014', 'em dash'), ('\u2013', 'en dash'), ('\u2019', 'apostrofo curvo')) if re.search(p, v['italian'])]
ck('tipografia (accenti veri, nessun carattere tipografico)', not bad, bad)
nonlat = [v['idx'] for v in cov for c in v['italian'] if ord(c) > 127 and not 0x00C0 <= ord(c) <= 0x024F]
ck('caratteri non latini', not nonlat, nonlat)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 12 unita sono PENDING (misurato)',
   c.execute('select count(*) from units where id in (%s) and state != "PENDING"'
             % ','.join('?' * len(units)), [u['id'] for u in units]).fetchone()[0] == 0)
print('| Controllo | Esito | OK |')
print('|---|---|---|')
for n, d, ok in rows:
    print('| %s | %s | %s |' % (n, d, 'OK' if ok else 'FAIL'))
print()
print('parole EN %d -> IT %d' % (sum(len(v['english'].split()) for v in cov), sum(len(v['italian'].split()) for v in cov)))
print('righe %d/%d · parti %d · mancanti %d' % (min(u['line'] for u in units), max(u['line'] for u in units),
      len(parts), len([u for u in units if u['idx'] not in tr])))
print('FAIL totale:', sum(1 for _, _, ok in rows if not ok))
raise SystemExit(0 if all(ok for _, _, ok in rows) else 1)
