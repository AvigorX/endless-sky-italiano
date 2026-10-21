r"""verify.py — L141 (`data/hai/unfettered 0 prologue.txt`, 20 unita', righe 83-132). Chiude la prima missione.

Invariante di **segmento**: 147 unita' nel file, **25 prima** della riga 83, **102 dopo** la 132, e il confine alla riga
**139** e' un **cambio di missione** (`First Contact: Unfettered` -> `Unfettered Jump Drive 1`): e' la prova che il
contesto si chiude davvero.
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
PATH = 'data/hai/unfettered 0 prologue.txt'
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


ck('riga grezza identica al sorgente', not [u for u in su if lines[u['line'] - 1] != u['raw']])
db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
bad = []
for u in su:
    r = db.execute('select english,kind,path,context from units where id=?', (u['id'],)).fetchone()
    if r is None or r[0] != u['english'] or r[1] != u['kind'] or r[2] != u['path'] or r[3] != u['context']:
        bad.append(u['idx'])
ck('english/kind/path/context identici al DB', not bad, bad)
ck('idx 1..20 e ordine = sorgente', [u['idx'] for u in tu] == list(range(1, 21)) == [u['idx'] for u in su])
first, last = tu[0]['line'], tu[-1]['line']
ck('unita: 20 righe 83 - 132', len(tu) == 20 and (first, last) == (83, 132), (len(tu), first, last))
ck('25 unita prima della riga 83 (L140)', db.execute(
    'select count(*) from units where path=? and line<?', (PATH, first)).fetchone()[0] == 25)
ck('147 unita nel file, 102 dopo la riga 132', db.execute(
    'select count(*) from units where path=?', (PATH,)).fetchone()[0] == 147
   and db.execute('select count(*) from units where path=? and line>?', (PATH, last)).fetchone()[0] == 102)
ck('confine alla riga 139: cambio di missione verso Unfettered Jump Drive 1', db.execute(
    'select line,context from units where path=? and line>? order by line limit 1',
    (PATH, last)).fetchone() == (139, 'mission:Unfettered Jump Drive 1'))
ck('il contesto First Contact: Unfettered e chiuso: 45 unita in tutto', db.execute(
    'select count(*) from units where path=? and context=?',
    (PATH, 'mission:First Contact: Unfettered')).fetchone()[0] == 45)
ck('tipi: 18 MISSION_TEXT, 2 LOGBOOK', collections.Counter(u['kind'] for u in su)
   == {'MISSION_TEXT': 18, 'LOGBOOK': 2})
ck('ZERO VALUE, ZERO UI_LABEL, ZERO token (tre asserzioni vuote)',
   [u['idx'] for u in su if u['kind'] in ('VALUE', 'UI_LABEL')] == []
   and collections.Counter(t for u in su for t in TAGS.findall(u['english'])) == {})
ck('tutte le unita sono tradotte',
   not [u['idx'] for u in tu if u['italian'].strip() == u['english'].strip()])
ck('tutte PENDING', not [u['idx'] for u in su
                         if db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] != 'PENDING'])
ck('spazi iniziali e finali identici al sorgente (20/20)',
   not [u['idx'] for u in tu
        if len(u['italian']) - len(u['italian'].rstrip()) != len(u['english']) - len(u['english'].rstrip())])
tabs = [u['idx'] for u in su if u['english'].startswith('\t')]
ck('18 unita con tab (le due di diario no)',
   len(tabs) == 18 and tabs == [u['idx'] for u in tu if u['italian'].startswith('\t')]
   and [u['idx'] for u in su if not u['english'].startswith('\t')] == [19, 20])
ck('58 virgolette, stesse per unita',
   sum(u['english'].count('"') for u in su) == 58 == sum(u['italian'].count('"') for u in tu)
   and not [u['idx'] for u in tu if u['english'].count('"') != u['italian'].count('"')])
ck('nessuna unita dispari', [u['idx'] for u in su if u['english'].count('"') % 2] == [])
ck('1 contesto: 20 unita', list(collections.Counter(u['context'] for u in su).values()) == [20])
ck('20 testi inglesi distinti', len({u['english'] for u in tu}) == 20)
ck('la frase sugli «antenati ottusi» ha la stessa resa in 3 e 5',
   'sopravvivono solo i loro antenati ottusi' in by[3]['italian']
   and 'sopravvivono solo i loro antenati ottusi' in by[5]['italian'])
ck('la voce telegrafica resta telegrafica',
   'molti mondi oltre il wormhole erano nostri' in by[1]['italian'])
ck('i nomi restano: Sheragi, Drak, Hai, wormhole',
   all(t in ' '.join(u['italian'] for u in tu) for t in ('Sheragi', 'Drak', 'Hai', 'wormhole')))
ck('nessun carattere non latino, nessun carattere tipografico',
   not [u['idx'] for u in tu if any(c in u['italian'] for c in '\u2014\u2013\u2018\u2019\u201C\u201D\u00AB\u00BB\u2026')
        or any(ord(c) > 126 and not 0xC0 <= ord(c) <= 0x24F for c in u['italian'])])
rs = [u['ratio'] for u in tu]
ck('rapporto nel gate', 0.55 < min(rs) and max(rs) < 1.90, (min(rs), max(rs)))
merged = {}
for f in sorted(os.listdir(os.path.join(HERE, 'parts'))):
    if f.endswith('.json'):
        for k, v in json.load(open(os.path.join(HERE, 'parts', f), encoding='utf-8')).items():
            merged[int(k)] = v
ck('le tre parti ricostruiscono translation.json (1..20)',
   sorted(merged) == list(range(1, 21)) and merged == {u['idx']: u['italian'] for u in tu})
ck('nessun altro lotto rivendica le righe 83-132',
   not [f for f in os.listdir(os.path.join(L10N, 'staging/editorial'))
        if f.startswith('L') and os.path.exists(os.path.join(L10N, 'staging/editorial', f, 'translation.json'))
        and os.path.abspath(os.path.join(L10N, 'staging', 'editorial', f)) != HERE
        and any(u['path'] == PATH and first <= u['line'] <= last for u in json.load(open(os.path.join(
            L10N, 'staging', 'editorial', f, 'translation.json'), encoding='utf-8'))['units'])])
h = hashlib.sha256(open(os.path.join(HERE, 'translation.json'), 'rb').read()).hexdigest()
print('segmento: 45/147 unita del file (30,6%) · 25 prima / 102 dopo · il contesto First Contact e chiuso (45/45)')
print('parole EN %d -> IT %d · rapporto min %.2f max %.2f media %.2f' % (
    sum(len(u['english'].split()) for u in tu), sum(len(u['italian'].split()) for u in tu),
    min(rs), max(rs), sum(rs) / len(rs)))
print('sha256[:16] %s' % h[:16])
print()
print('FAIL:', len(fail), '·', 'verify L141 superato' if not fail else 'verify L141 fallito')
raise SystemExit(0 if not fail else 1)
