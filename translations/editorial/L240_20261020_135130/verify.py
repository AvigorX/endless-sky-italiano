r"""verify.py — L240 (`data/avgi/avgi jobs.txt`, 40 unita', righe 684-1156). **LOTTO TERMINALE: chiude il file.**

**Invariante di FILE**: la copertura si legge da **tutti** i `translation.json` del percorso e si confronta col database:

    62 (L239) + 40 (L240) = 102 = unita' del file

Si asserisce insieme: **0 unita' dopo la 1156**, `max(line) == 1156`, **102 id distinti su 102 righe distinte**,
**nessuna riga rivendicata due volte**, e i conteggi **misurati** per lotto.

Verifica inoltre cio' che il `check.py` non puo' vedere da solo: `<origin>` **prima** di `<destination>` in ogni unita',
i `VALUE` copiati dal **sorgente** (non riscritti), la coerenza cross-lot delle formule gia' presenti nel corpus e il
possessivo `<planet>'s` che in italiano sparisce (2 apici in inglese, 0 in italiano).

Indipendente da `check.py`: rilegge `source.json`, i `translation.json`, il database e il file del gioco.
"""
import collections
import glob
import hashlib
import json
import os
import re
import sqlite3

TAB = chr(9)
QUOTE = chr(34)
APOS = chr(39)
TAG = re.compile(r'<[^<>]+>')
HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/avgi/avgi jobs.txt'
src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))
su = sorted(src['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
raw_lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-80s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (40/40)',
   not [u for u in su if raw_lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if raw_lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck("unita: 40, righe 684 - 1156", len(tu) == 40 and (tu[0]['line'], tu[-1]['line']) == (684, 1156))
ck('20 VALUE + 20 DESCRIPTION', collections.Counter(u['kind'] for u in su) == {'VALUE': 20, 'DESCRIPTION': 20})
ck("62 unita' prima della 684 (L239)",
   db.execute('select count(*) from units where path=? and line<684', (PATH,)).fetchone()[0] == 62)
ck("ZERO unita' dopo la 1156: il lotto CHIUDE il file",
   db.execute('select count(*) from units where path=? and line>1156', (PATH,)).fetchone()[0] == 0)
ck('il file intero: 102 unita, righe 20 - 1156',
   db.execute('select count(*),min(line),max(line) from units where path=?', (PATH,)).fetchone() == (102, 20, 1156))
VAL = [u for u in tu if u['kind'] == 'VALUE']
DES = [u for u in tu if u['kind'] == 'DESCRIPTION']
ck("i 20 VALUE sono copiati dal sorgente carattere per carattere (il `the` compreso)",
   all(u['italian'] == u['english'] for u in VAL) and len(VAL) == 20,
   [u['idx'] for u in VAL if u['italian'] != u['english']])
ck("le 20 DESCRIPTION sono tutte tradotte", all(u['italian'] != u['english'] for u in DES))
ck('nessun tab, nessuna virgoletta',
   sum(u['english'].count(TAB) for u in su) == 0 == sum(u['italian'].count(TAB) for u in tu)
   and sum(u['english'].count(QUOTE) for u in su) == 0 == sum(u['italian'].count(QUOTE) for u in tu))
tok_en = collections.Counter(t for u in su for t in TAG.findall(u['english']))
tok_it = collections.Counter(t for u in tu for t in TAG.findall(u['italian']))
ck("segnaposto: 99 su 7 simboli, parita' per simbolo",
   tok_en == tok_it == {'<destination>': 26, '<planet>': 22, '<payment>': 20, '<cargo>': 11,
                        '<bunks>': 9, '<origin>': 6, '<date>': 5}, (dict(tok_en), dict(tok_it)))
ck("segnaposto: ordine identico in ogni unita'",
   all(tuple(TAG.findall(u['english'])) == tuple(TAG.findall(u['italian'])) for u in tu),
   [(u['idx'], TAG.findall(u['english']), TAG.findall(u['italian'])) for u in tu
    if TAG.findall(u['english']) != TAG.findall(u['italian'])])
ck("<origin> precede <destination> in tutte le 6 unita' che li hanno entrambi (partenza e arrivo non si invertono)",
   all(TAG.findall(u['italian']).index('<origin>') < TAG.findall(u['italian']).index('<destination>')
       for u in tu if '<origin>' in TAG.findall(u['english']))
   and sum(1 for u in tu if '<origin>' in TAG.findall(u['english'])) == 6)
ck("nessuna unita' con segnaposto solo in una lingua",
   [u['idx'] for u in tu if bool(TAG.findall(u['english'])) != bool(TAG.findall(u['italian']))] == [])
fam = collections.Counter(u['english'] for u in DES)
ck('8 famiglie di DESCRIPTION (6 · 3 · 3 · 3 · 2 · 1 · 1 · 1)', sorted(fam.values()) == [1, 1, 1, 2, 3, 3, 3, 6],
   dict(fam))
ck('una sola resa per famiglia',
   all(len({u['italian'] for u in DES if u['english'] == k}) == 1 for k in fam))
ck("il possessivo `<planet>'s` sparisce in italiano: 2 apici in inglese, 0 in italiano",
   sum(u['english'].count(APOS) for u in su) == 2 and sum(u['italian'].count(APOS) for u in tu) == 0
   and [u['idx'] for u in su if APOS in u['english']] == [26, 28])
gold = 'Porta <cargo> da <origin> a <destination> per sostenere la costruzione di <destination> in cambio di <payment>.'
ck("coerenza interna: la formula da 6 copie ha una resa sola e contiene i 5 segnaposto",
   [u['italian'] for u in DES if u['english'].startswith('Bring <cargo> from <origin>')][0] == gold)
ck("coerenza cross-lot: «su <destination>», «entro il <date>», «in cambio di <payment>» sono le forme di L239",
   ' su <destination>' in ' '.join(u['italian'] for u in DES)
   and 'entro il <date>' in ' '.join(u['italian'] for u in DES)
   and 'in cambio di <payment>' in ' '.join(u['italian'] for u in DES))
ck("PENDING su tutte e 40", not [u['idx'] for u in su
                                 if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0]
                                 != 'PENDING'])
ck('nessuno spazio finale e nessun doppio spazio',
   not [u['idx'] for u in tu if u['italian'] != u['italian'].rstrip() or '  ' in u['italian']])
ck('nessun carattere tipografico e nessun non latino',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate 0,55-1,90 (0,90 - 1,14; 470 -> 476 parole)',
   0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
per, lines, ids, wen, wit = [], [], [], 0, 0
for f in sorted(glob.glob(os.path.join(L10N, 'staging', 'editorial', 'L*', 'translation.json'))):
    us = [u for u in json.load(open(f, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        per.append((os.path.basename(os.path.dirname(f)), len(us)))
        lines += [u['line'] for u in us]
        ids += [u['id'] for u in us]
        wen += sum(len(u['english'].split()) for u in us)
        wit += sum(len(u['italian'].split()) for u in us)
ck("INVARIANTE DI FILE: 62 + 40 = 102 unita' su 102 righe distinte, nessun doppione",
   sum(n for _, n in per) == 102 and per[-1][1] == 40
   and len(lines) == 102 == len(set(lines)) and len(ids) == 102 == len(set(ids))
   and max(lines) == 1156, per)
ck("copertura = database: nessuna unita' del file resta fuori staging",
   set(ids) == set(i for (i,) in db.execute('select id from units where path=?', (PATH,))), len(set(ids)))
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print("FILE: 102/102 unita' (100%%) in %d lotti: %s" % (len(per), ' + '.join('%s %d' % (k.split('_')[0], n) for k, n in per)))
print('FILE parole EN %d -> IT %d' % (wen, wit))
print('parole L240 EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L240 superato' if not fail else 'verify L240 fallito')
raise SystemExit(0 if not fail else 1)
