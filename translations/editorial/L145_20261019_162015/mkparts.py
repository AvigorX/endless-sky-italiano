"""mkparts.py — L145: `data/hai/unfettered 0 prologue.txt`, righe 423-459 (13 unita').

Primo `LOGBOOK` del tratto e **tre token** in tre unita' diverse: `<learned>` (unita' 2, dopo un punto esclamativo, con
la maiuscola che segue), `<last>` (unita' 2, il cognome del capitano), `<The engineer>` (unita' 5, **a inizio frase**: il
segnaposto contiene una frase con la maiuscola, quindi il confronto e' `== '<The engineer>'`, **mai** `.lower()`).

**Due virgolette dispari** (unita' 12 e 13): il sorgente apre una battuta e non la chiude. La resa **non la chiude**:
chiuderla sarebbe un'invenzione tipografica.

Nomi di armi e navi restano inglesi: `Tripulse Shredder`, `Blaster`, `Ion Cannon`, `Shield Beetle`, `Firelode`.
"""
import collections
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARTS = os.path.join(HERE, 'parts')
SRC = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
ENG = {u['idx']: u['english'] for u in SRC}
KEY = {i: e.lstrip('\t') for i, e in ENG.items()}
TAGS = re.compile(r'<[^<>]+>')

D = {
    1: "Riesci ad afferrare l'arma, appena in tempo per deviare un attacco della stessa Slegata. Duella con te per "
       "quello che sembra un'eternità. All'inizio sei stupito di essere riuscito a sopravvivere così a lungo, ma presto "
       "capisci che, non essendo riuscito a mettere a segno un solo colpo, deve trattarsi di una sorta di prova "
       "deliberata.",
    2: "Poi, all'improvviso, senti cambiare il ritmo dell'avversaria: il gioco è finito. Sferra un colpo magistrale che "
       "ti disarma con facilità, poi sorride e abbassa la propria arma. \"Sembra che tu sappia come si usa una lama! "
       "<learned>Sono Desneeparu, ed è un piacere conoscerti, capitano <last>!\" esclama, prima di ridere della tua "
       "faccia sorpresa. Capisci che ti stava prendendo in giro fin dall'inizio, ma, ciononostante, sembra soddisfatta "
       "della tua prova.",
    3: "Un guerriero Slegato che sa come si maneggia una lama. Messo alla prova da lei prima di ricevere l'accesso alle "
       "nuove armi Slegate. Sarebbe stata la fine, se lei non si fosse trattenuta.",
    4: "Fa una specie di saluto col pugno prima di andarsene. \"Ora devo andare. Spero che troverai l'arma che ti "
       "serve.\"",
    5: "<The engineer> ti conduce sottoterra, tra file e file di armi prototipo, alcune delle quali sono in lavorazione "
       "da parte degli ingegneri. Spiegano: \"Preferiamo fare la maggior parte dei nostri collaudi sul campo di "
       "battaglia. Qui eseguiamo solo i controlli di sicurezza più elementari prima che i capitani Slegati possano "
       "metterci le mani. Spesso cominciano andando a Firelode per portare l'arma al limite, per assicurarsi che non "
       "esploda in mezzo all'azione. Più interesse suscita un prototipo, più lo sviluppiamo.\" Continuate a camminare "
       "finché non entrate nella sezione del fornitore della struttura, dove noti che gli articoli in esposizione sono "
       "molto più avanzati di qualunque cosa tu abbia visto in superficie: tanto che potrebbe quasi passare per un "
       "fornitore Hai 'normale', se non fosse per la sensazione sovraccarica e opprimente delle aree di prova.",
    6: "\"Benvenuto nella sezione avanzata del fornitore, capitano! È riservata ai nostri ospiti più illustri. Ora che ci "
       "hai venduto diversi motori di salto, posso dirti che offriamo qualcosa di molto più prezioso del denaro. Per ora "
       "posso offrirti solo il possente Tripulse Shredder, ma col tempo ti daremo accesso a ogni tipo di arma. Due "
       "Tripulse Shredder e la nostra riconoscenza in cambio di un motore di salto: è l'accordo che propongo,\" dicono, "
       "porgendoti le armi. Ora che puoi guardarle più da vicino, noti che sembrano piuttosto simili alle altre armi "
       "Hai, ma sono potenziate in un modo o nell'altro. Accanto ai Tripulse puoi scorgere quello che sembra un Ion "
       "Cannon molto piccolo e un Ion Cannon montato su torretta.",
    7: "\"Dimmi di più di quei Tripulse Shredder che posso comprare.\"",
    8: "\"Allora mi accontento del tripulse.\"",
    9: "\"Puoi dirmi di più di quell'arma ionica piccola?\"",
    10: "\"Mi piacerebbe sapere di più di questo... ion cannon montato su una torretta?\"",
    11: "\"In verità, preferirei semplicemente il denaro.\"",
    12: "\"Ah, il Blaster. È prediletto da molti capitani di Shield Beetle, perché li aiuta facilmente a ribaltare le "
        "sorti di una battaglia senza dover dedicare troppo spazio a bordo alle armi. Soprattutto considerando i suoi "
        "altri effetti, il suo potenziale di danno è accettabile. È vero che non infligge abbastanza danni ionici da "
        "disabilitare da sola una nave, ma riesce a inceppare le armi e ti darà il vantaggio in uno scontro prolungato. "
        "Questa però è un'innovazione recente, e alcuni dicono che le manchi la... finezza delle altre.",
    13: "\"È di gran lunga la mia arma preferita fra tutte. A differenza dell'Ion Cannon, che è un'arma ibrida pensata "
        "per danneggiare il nemico a lunga distanza applicando al contempo una buona ionizzazione, il suo ruolo è "
        "soprattutto disabilitare le navi nemiche. Perfino una nave con molte batterie si inchinerà davanti a quest'arma! "
        "E grazie alla sua lunga gittata e alla rapidità di rotazione, le navi piccole e perfino i caccia non ti daranno "
        "più fastidio!",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 12, 'LOGBOOK': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 12
assert sum(u['english'].count('"') for u in SRC) == 20
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == [12, 13]
assert [u['idx'] for u in SRC if u['kind'] == 'LOGBOOK'] == [3]
assert collections.Counter(u['context'] for u in SRC) == {'mission:Unfettered Jump Drive Trading': 13}
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert dict(tok) == {'<learned>': 1, '<last>': 1, '<The engineer>': 1}, dict(tok)
assert [u['idx'] for u in SRC if TAGS.findall(u['english'])] == [2, 5]
assert [len(TAGS.findall(ENG[i])) for i in (2, 5)] == [2, 1]
assert [u['idx'] for u in SRC if u['kind'] in ('VALUE', 'UI_LABEL')] == []
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (423, 459)
assert sorted(D) == list(range(1, 14)), [i for i in range(1, 14) if i not in D]
assert '<The engineer>' in ENG[5] and ENG[5].lstrip('\t').startswith('<The engineer>')
assert ENG[12].count('"') == ENG[13].count('"') == 1

T = {}
for u in SRC:
    eng = u['english']
    T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + D[u['idx']].lstrip('\t')

for idx, txt in T.items():
    eng = ENG[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()), ('spazio finale', idx)
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 13, len(dup)
assert 'lama! <learned>Sono Desneeparu' in T[2]
assert 'capitano <last>!' in T[2]
assert T[5].lstrip('\t').startswith('<The engineer> ti conduce')
assert T[12].count('"') == T[13].count('"') == 1
assert not T[12].rstrip().endswith('"') and not T[13].rstrip().endswith('"')
for nome in ('Tripulse Shredder', 'Blaster', 'Ion Cannon', 'Shield Beetle', 'Firelode'):
    assert nome in ' '.join(T.values()), nome

for n, (lo, hi) in enumerate(((1, 5), (6, 9), (10, 13))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('13 unita (5+4+4) · 12 MISSION_TEXT + 1 LOGBOOK · 1 contesto · 13 testi distinti')
print('3 token in 3 unita (2 e 5) · 2 virgolette dispari (12, 13) · 12 tab · 20 virgolette')
