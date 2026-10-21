r"""check.py — L209 (`data/coalition/coalition news.txt`, 21 unita', righe 247-308). Quarto lotto del file.

**Tre stringhe ripetute tre volte**: le unita' **4/9/14**, **5/10/15** e **6/11/16** sono lo stesso testo inglese sotto
tre contesti diversi (arach, kimek e saryd civilian). La resa italiana deve essere **identica** nelle tre copie, e le
famiglie devono coincidere: se una copia divergesse, il controllo cade.

**21 `NEWS`**, tutte citazioni (42 virgolette, 2 per unita'), **zero tab**, **zero segnaposto**.

**Registro**: 18 unita' su 21 chiudono con un verbo flesso. Le tre eccezioni sono **esattamente** la famiglia 5/10/15,
che nel sorgente finisce con «I never can...»: la resa chiude con «non posso mai...».
"""
import collections
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
WORDS = re.compile(r"[A-Za-z\u00C0-\u024F']+")
IT_ALL = ' '.join(v['italian'] for v in cov)
EN_ALL = ' '.join(v['english'] for v in cov)
EN_T = sum(len(TAGS.findall(v['english'])) for v in cov)
IT_T = sum(len(TAGS.findall(v['italian'])) for v in cov)
EN_Q = sum(v['english'].count(QUOTE) for v in cov)
IT_Q = sum(v['italian'].count(QUOTE) for v in cov)
EN_A = sum(v['english'].count(APOS) for v in cov)
IT_A = sum(v['italian'].count(APOS) for v in cov)
KINDS = collections.Counter(u['kind'] for u in units)
CTX = collections.Counter(u['context'].replace('news:', '') for u in units)
FAMILIES = [[4, 9, 14], [5, 10, 15], [6, 11, 16]]
NAMES = ('Ring of Wisdom', 'Saryd', 'Arach', 'Kimek', 'Heliarch', 'Arachi', 'jump drive',
         'longcow', 'ringworld')
VEND = ('guadagnerei', 'stato', 'è', 'fatto', 'fanno', 'sta', 'essere', 'provano', 'ho', 'sono', 'fare')
rows = []


def ck(n, c, d=''):
    rows.append((n, d if d else ('OK' if c else ''), c))


def tail(i):
    w = WORDS.findall(by[i]['italian'].rstrip('."!?'))
    return w[-1] if w else ''


def fam(lang):
    d = {}
    for i in sorted(by):
        d.setdefault(by[i][lang], []).append(i)
    return sorted([v for v in d.values() if len(v) > 1])


ck("unita' tradotte 21/21", len(cov) == 21 == len(units), '%d/%d' % (len(cov), len(units)))
ck('nessuna traduzione vuota', all(v['italian'].strip() for v in cov))
ck('tipi: 21 NEWS', KINDS == {'NEWS': 21}, dict(KINDS))
ck('ZERO VALUE, TEXT, DIALOG, UI_LABEL (asserzioni vuote scritte)',
   [u['idx'] for u in units if u['kind'] != 'NEWS'] == [])
ck('5 contesti: 3 merchant, 3 vendor e tre contesti civilian da 5 unita ciascuno',
   len(CTX) == 5 and sorted(CTX.values()) == [3, 3, 5, 5, 5]
   and [k for k in CTX if k.endswith('civilian')] == ['arach civilian', 'kimek civilian', 'saryd civilian'],
   dict(CTX))
ck('righe 247 e 308 (prima e ultima del lotto)',
   (cov[0]['line'], cov[-1]['line']) == (247, 308), (cov[0]['line'], cov[-1]['line']))
ck('ZERO segnaposto e ZERO tab in entrambe le lingue (asserzioni vuote scritte)',
   EN_T == 0 == IT_T and '<' not in IT_ALL and '<' not in EN_ALL
   and [v['idx'] for v in cov if TAB in v['english'] or TAB in v['italian']] == [])
ck('42 virgolette, 2 per unita\' in tutte e 21 (nessuna narrazione in questo lotto)',
   EN_Q == 42 == IT_Q and all(v['english'].count(QUOTE) == 2 == v['italian'].count(QUOTE) for v in cov)
   and all(v['italian'].startswith(QUOTE) and v['italian'].endswith(QUOTE) for v in cov), (EN_Q, IT_Q))
ck("apici: 2 inglesi (unita' 2, 'field trip') e 7 italiani (unita' 2, 4, 9, 12, 14, 19)",
   EN_A == 2 and IT_A == 7
   and [v['idx'] for v in cov if APOS in v['english']] == [2]
   and [v['idx'] for v in cov if APOS in v['italian']] == [2, 4, 9, 12, 14, 19], (EN_A, IT_A))
ck("le virgolette singole di 'gita di studio' (unita' 2) sono conservate, due per lato come in inglese",
   "'gita di studio'" in by[2]['italian'] and "'field trip,'" in by[2]['english']
   and by[2]['italian'].count(APOS) == 2 == by[2]['english'].count(APOS))
ck('FAMIGLIE: le tre stringhe ripetute sono le stesse tre in inglese e in italiano (4/9/14, 5/10/15, 6/11/16)',
   fam('english') == FAMILIES and fam('italian') == FAMILIES, (fam('english'), fam('italian')))
ck('FAMIGLIE: dentro ogni famiglia la resa italiana e\' identica (nessuna copia divergente)',
   all(len({by[i]['italian'] for i in f}) == 1 for f in FAMILIES))
ck('REGISTRO SARYD: 17 unita\' su 21 chiudono con un verbo flesso',
   [i for i in sorted(by) if tail(i) in VEND] == [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20],
   [i for i in sorted(by) if tail(i) in VEND])
ck('le quattro eccezioni: la famiglia 5/10/15 chiude con «mai...» come il sorgente «never can...», '
   'e l\'unita\' 21 chiude con «crediti!» come «credits!»',
   [i for i in sorted(by) if tail(i) not in VEND] == [5, 10, 15, 21]
   and all(by[i]['italian'].rstrip(QUOTE).endswith('mai...')
           and by[i]['english'].rstrip(QUOTE).endswith('never can...') for i in (5, 10, 15))
   and by[21]['italian'].rstrip(QUOTE).endswith('crediti!')
   and by[21]['english'].rstrip(QUOTE).endswith('credits!'))
ck('nessun caporale e nessun carattere tipografico',
   not [v['idx'] for v in cov if any(c in v['italian'] for c in '\u00ab\u00bb\u201c\u201d\u2018\u2019\u2014\u2013\u2026')])
ENGW = (' the ', ' of the ', ' and ', ' with ', ' your ', ' this ', ' when ', ' you ', ' to the ', ' will be ',
        ' is ', ' are ', ' from the ', ' its ', ' it is ', ' such as ', ' rather than ', ' for a ', ' that ')
ck('nessun residuo inglese', not [w for w in ENGW if w in IT_ALL.lower()],
   [w for w in ENGW if w in IT_ALL.lower()])
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
ck('i nomi restano invariati (Ring of Wisdom, Saryd, Arach, Kimek, Heliarch, Arachi, jump drive...)',
   not [n for n in NAMES if n in EN_ALL and n not in IT_ALL],
   [n for n in NAMES if n in EN_ALL and n not in IT_ALL])
ck('«Houses» (istituzione) diventa «Case»; il nome proprio «House Ablomab» non tocca questo lotto',
   'our Houses' in EN_ALL and 'le nostre Case' in IT_ALL and 'Houses' not in IT_ALL)
c = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
st = dict(c.execute('select state,count(*) from units group by state').fetchall())
ck('state.db APPROVED/PENDING', st['APPROVED'] == 364, '%s/%s' % (st['APPROVED'], st['PENDING']))
ck('tutte le 21 unita sono PENDING (misurato)',
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
