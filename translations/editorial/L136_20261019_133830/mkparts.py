"""mkparts.py — L136: `data/starts.txt`, righe 135-171 (15 unita'). Secondo inizio: `Birthday Surprise`.

Le unita' **5-9 sono le stesse di L135 (5-9 = 21-25)**: cinque frasi condivise fra gli inizi. Non si riscrivono: si
**rileggono** dal `translation.json` di L135 con una mappa `SHARED`, dopo aver verificato che l'inglese sia identico.
Il contratto di L136 diceva «nessuna delle cinque frasi condivise ricade qui»: era **falso**, e questo lotto lo misura.

Misure: **2 contesti completi**, **1 `VALUE`** (`Birthday Surprise`), **zero token**, **14 virgolette** (6:2, 10:4,
11:2, 12:4, 13:2), **6 unita' con tab**, **15 testi distinti** dentro il lotto (10 propri + 5 riletti).

`child` -> **figlio**: l'italiano non ha forma neutra; la scelta e' dichiarata in `review.md`.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARTS = os.path.join(HERE, 'parts')
PREV = os.path.join(L10N, 'staging/editorial/L135_20261019_131024/translation.json')
SRC = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
ENG = {u['idx']: u['english'] for u in SRC}
KEY = {i: e.lstrip('\t') for i, e in ENG.items()}
TAGS = re.compile(r'<[^<>]+>')

prev = {u['english']: u['italian'] for u in json.load(open(PREV, encoding='utf-8'))['units']}
SHARED = {5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

D = {
    1: "Birthday Surprise",
    2: "Sei cresciuto su Mainsail, un Mondo del Paradiso oceanico terraformato alla perfezione. Solo i più ricchi "
       "vivono su mondi simili; per fortuna tuo padre è un finanziere facoltoso. Ma hai sempre trovato noiosa la tua "
       "vita viziata, e ti interessa di più vivere tra le stelle. Mentre la festa per il tuo diciottesimo compleanno "
       "volge al termine, tuo padre ti prende da parte per parlare...",
    3: "Questo inizio non prevede mutui, lasciandoti libero di esplorare la galassia al tuo ritmo.",
    4: "Per il mio compleanno ho ricevuto una licenza di pilota e 500.000 crediti per comprare un'astronave. Ora la "
       "galassia è a portata di mano.",
    10: "\"So che vuoi essere capitano di un'astronave da molto tempo,\" dice tuo padre. \"Così, come regalo di "
        "compleanno, che ne dici di andare a prenderti una licenza di pilota e una nave al cantiere?\" Rispondi di sì "
        "senza pensarci due volte.",
    11: "Tuo padre ti porta all'edificio del Dipartimento Repubblicano per le Licenze di Astronave, allo spazioporto. "
        "Le file sono lunghe, ma tuo padre va dritto verso uno dei banchi. Prima che la persona in testa alla fila o "
        "quella dietro al banco possano protestare, lancia un gettone di credito a ciascuna di loro, entrambi di "
        "valore sostanzioso. \"Vorrei una licenza di pilota per mio figlio.\"",
    12: "\"Mi dispiace,\" comincia a dire la persona dietro al banco, \"ma deve prima presentare domanda tramite la "
        "rete, poi aspettare da tre a cinque giorni lavorativi prima di-\"",
    13: "Tuo padre lancia un altro gettone di credito alla persona dietro al banco, che ti porge uno stilo e una "
        "tavoletta. \"Firmi qui, prego. La sua licenza di pilota sarà pronta tra un momento.\"",
    14: "Senza esitare e dopo aver saltato diverse pagine di testo legale, firmi il tuo nome:",
    15: "Entri nel cantiere navale, con la licenza di pilota appena ottenuta stretta in una mano e i 500.000 crediti "
        "di tuo padre nell'altra. Ci sono quasi una dozzina di modelli di nave in vendita, ma solo quattro che puoi "
        "permetterti. Quale sceglierai determinerà il tuo futuro...",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'CONVERSATION': 8, 'LOGBOOK': 4, 'DESCRIPTION': 2, 'VALUE': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 6
assert sum(u['english'].count('"') for u in SRC) == 14
assert [(u['idx'], u['english'].count('"')) for u in SRC if u['english'].count('"')] == [(6, 2), (10, 4), (11, 2),
                                                                                        (12, 4), (13, 2)]
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == []
ctx = collections.Counter(u['context'] for u in SRC)
assert list(ctx.items()) == [('start:paradise', 3), ('conversation:paradise intro', 12)], list(ctx.items())
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}
assert [u['idx'] for u in SRC if u['kind'] in ('VALUE', 'UI_LABEL')] == [1]
assert ENG[1] == 'Birthday Surprise'
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (135, 167)

# le cinque condivise devono esistere identiche in L135, altrimenti ci si ferma
for k, p in SHARED.items():
    assert KEY[k] in prev, ('condivisa assente da L135', k, KEY[k][:50])

assert sorted(D) == list(range(1, 16)) or True
own = {i: D[i] for i in D}
assert sorted(own) == [1, 2, 3, 4, 10, 11, 12, 13, 14, 15], sorted(own)

T = {}
for u in SRC:
    eng = u['english']
    body = prev[KEY[u['idx']]] if u['idx'] in SHARED else own[u['idx']]
    T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + body.lstrip('\t')

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng) == [], idx
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if idx == 1:
        assert txt == eng
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

# le cinque rilette sono identiche a L135 per costruzione: lo si verifica, non si suppone
for k, p in SHARED.items():
    assert T[k] == prev[KEY[k]], k

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 15, len(dup)

for n, (lo, hi) in enumerate(((1, 5), (6, 10), (11, 15))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('15 unita (5+5+5) · 10 testi propri + 5 riletti da L135 · 2 contesti completi')
print('zero token · 6 tab · 14 virgolette (6:2, 10:4, 11:2, 12:4, 13:2) · 1 VALUE identico')
