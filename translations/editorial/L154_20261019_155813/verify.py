r"""verify.py — L154 (`data/coalition/coalition jobs.txt`, 41 unita', righe 1475-1807).

Invariante di **FILE**: il lotto chiude il file. Le 8 finestre (L147…L154) devono sommare **197** unita' su **197 righe
distinte**, con `min(line) = 16` e `max(line) = 1807`; nessuna riga rivendicata due volte; nessuna unita' dopo la 1807.

Misure proprie: 9 famiglie `Lunarium: X Delivery` con forma regolare; **0 tab** e **0 virgolette**; **57 token su 7
simboli**; assenza incrociata `<destination>` / `<planet>`; 13 `VALUE` identici.
"""
import collections
import hashlib
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ROOT = os.path.abspath(os.path.join(L10N, '..'))
PATH = 'data/coalition/coalition jobs.txt'
TAGS = re.compile(r'<[^<>]+>')
su = sorted(json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units'], key=lambda x: x['line'])
tu = json.load(open(os.path.join(HERE, 'translation.json'), encoding='utf-8'))['units']
by = {u['idx']: u for u in tu}
lines = open(os.path.join(ROOT, 'endless-sky', *PATH.split('/')), encoding='utf-8').read().split('\n')
fail = []


def ck(n, c, d=''):
    print('%-70s %s %s' % (n, 'OK' if c else 'FAIL', '' if c else d))
    if not c:
        fail.append(n)


ck('riga grezza identica al sorgente (41/41)', not [u for u in su if lines[u['line'] - 1] != u['raw']],
   [u['idx'] for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..41 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 42)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 41 righe 1475 - 1807', len(tu) == 41 and (first, last) == (1475, 1807), (len(tu), first, last))
ck('156 unita prima della riga 1475 (L147…L153)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 156)
ck('197 unita nel file, ZERO dopo la riga 1807 (fine file)',
   db.execute('select count(*) from units where path=?', (PATH,)).fetchone()[0] == 197
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 0)
ck('max(line) del file = 1807, min(line) = 16', db.execute(
    'select min(line),max(line) from units where path=?', (PATH,)).fetchone() == (16, 1807))
# invariante di FILE: tutte le finestre chiuse su questo percorso
lots, claimed = [], []
for f in sorted(os.listdir(os.path.join(L10N, 'staging/editorial'))):
    p = os.path.join(L10N, 'staging/editorial', f, 'translation.json')
    if not os.path.isdir(os.path.join(L10N, 'staging/editorial', f)) or not os.path.exists(p):
        continue
    us = [u for u in json.load(open(p, encoding='utf-8'))['units'] if u['path'] == PATH]
    if us:
        lots.append((f, len(us)))
        claimed.extend(u['line'] for u in us)
ck('8 lotti su questo file (L147…L154)', len(lots) == 8, lots)
ck('somma delle finestre = 197 unita del file', sum(n for _, n in lots) == 197, sum(n for _, n in lots))
ck('zero sovrapposizioni: 197 righe rivendicate, 197 distinte',
   len(claimed) == 197 == len(set(claimed)), (len(claimed), len(set(claimed))))
ck('copertura esatta: min 16, max 1807, nessun buco',
   (min(claimed), max(claimed)) == (16, 1807)
   and sorted(set(claimed)) == sorted(r[0] for r in db.execute(
       'select line from units where path=?', (PATH,)).fetchall()))
ck('tipi: 13 VALUE + 13 DESCRIPTION + 15 DIALOG',
   collections.Counter(u['kind'] for u in su) == {'VALUE': 13, 'DESCRIPTION': 13, 'DIALOG': 15})
ck('ZERO UI_LABEL (asserzione vuota)', [u['idx'] for u in su if u['kind'] == 'UI_LABEL'] == [])
TOK = {'<payment>': 23, '<destination>': 14, '<planet>': 9, '<bunks>': 4, '<stopovers>': 3,
       '<origin>': 2, '<date>': 2}
ck('57 token su 7 simboli, stesso multiset in italiano',
   dict(collections.Counter(t for u in su for t in TAGS.findall(u['english']))) == TOK ==
   dict(collections.Counter(t for u in tu for t in TAGS.findall(u['italian'])))
   and sum(TOK.values()) == 57)
ck('parita per unita: stesso ordine di simboli in tutte le 41',
   not [u['idx'] for u in tu if TAGS.findall(u['italian']) != TAGS.findall(u['english'])])
ck('13 VALUE identici al sorgente',
   len([u for u in tu if u['kind'] == 'VALUE']) == 13
   and [u['idx'] for u in tu if u['kind'] == 'VALUE' and u['italian'].rstrip() != u['english'].rstrip()] == [])
ck('ZERO tab e ZERO virgolette nel sorgente e in traduzione',
   [u['idx'] for u in su if '\t' in u['english']] == [] == [u['idx'] for u in tu if '\t' in u['italian']]
   and sum(u['english'].count('"') for u in su) == 0 == sum(u['italian'].count('"') for u in tu))
PLANET = [u['idx'] for u in su if '<planet>' in u['english']]
ck('9 DIALOG di consegna con <planet>, nessuno con <destination>',
   PLANET == [17, 20, 23, 26, 29, 32, 35, 38, 41]
   and not [i for i in PLANET if '<destination>' in by[i]['english']])
ck('9 DIALOG: tre giunture fisse presenti in tutte',
   not [i for i in PLANET
        if 'Alcuni membri del Lunarium scaricano ' not in by[i]['italian']
        or 'dopo che atterri su una parte isolata di <planet>, come richiesto' not in by[i]['italian']
        or 'Ti consegnano <payment> prima di portare via ' not in by[i]['italian']])
ck('le due VALUE Rescue Lunarium Members identiche in italiano',
   by[8]['italian'] == by[12]['italian'])
ck('le due DESCRIPTION Evacuate hanno rese diverse (articolo)',
   by[9]['italian'] != by[13]['italian']
   and by[9]['italian'].startswith('Preleva <bunks>') and by[13]['italian'].startswith('Preleva i <bunks>'))
ck('40 stringhe distinte su 41 unita', len({(u['kind'], u['english']) for u in tu}) == 40)
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (41/41)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())
        or len(u['italian']) - len(u['italian'].lstrip()) != len(u['english']) - len(u['english'].lstrip())])
ck('nessun carattere tipografico e nessun non latino fuori dai token',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in TAGS.sub('', u['italian']))])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le tre parti ricostruiscono translation.json (1..41)',
   sorted(merged) == list(range(1, 42)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 1475-1807',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging/editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging/editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('file CHIUSO: 197/197 unita (100%) · 8 finestre · 156 prima / 41 nel lotto / 0 dopo · max(line) 1807')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L154 superato' if not fail else 'verify L154 fallito')
raise SystemExit(0 if not fail else 1)
