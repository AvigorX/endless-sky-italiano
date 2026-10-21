"""mkparts.py — L146: `data/hai/unfettered 0 prologue.txt`, righe 460-530 (19 unita'). **CHIUDE IL FILE.**

Due **`UI_LABEL`** (`back to choose` riga 460, `buy tripulse` riga 482): restano **identiche al sorgente**, escluse da
«tutte tradotte» e verificate in un controllo proprio. Quattro **token**, due dei quali con **parentesi**:
`<as before (run)>` e `<as before (flee)>` sono soggetti di frase (`<...> riesci a schivare`) e si confrontano **interi**;
`<leave>` apre una frase seguita da una maiuscola; `<origin>` e' il nome del mondo.

A differenza di L145 qui **nessuna virgoletta e' dispari**: 28, tutte pareggiate, e l'assenza va dichiarata.
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

L1 = "back to choose"
L2 = "buy tripulse"

D = {
    1: L1,
    2: "\"Però di queste armi ne abbiamo in quantità molto limitate, e quindi non possiamo ancora permetterci di "
       "dartele. Dunque, tornando alla mia offerta, hai deciso?\"",
    3: "\"Oh. Beh, in tal caso non ti disturberemo più con quest'arma, né con nessun'altra, capitano, né qui né nella "
       "bacheca dei lavori.\"",
    4: "\"Mi sembra un buon accordo.\"",
    5: "\"Aspetta, com'era quell'arma?\"",
    6: "\"Come vuoi. Ricorda però che se vuoi venderci altri motori di salto in cambio di denaro puoi andare alla "
       "bacheca dei lavori.\"",
    7: "\"Il Tripulse Shredder può sembrare grezzo, ma colpisce duro! La sua specialità è concentrare molta potenza di "
       "fuoco in un solo alloggiamento per arma e, grazie alla sua natura a raffica, è perfetto per i piloti che usano "
       "già tattiche mordi e fuggi. Alcuni capitani dicono perfino che uno Sea Scorpion possa avere la meglio su uno "
       "Shield Beetle se ne monta quattro, se sai quello che fai, naturalmente! Come dicevo, posso offrirti due di "
       "queste in cambio del tuo motore di salto.\"",
    8: L2,
    9: "Fanno eseguire il trasferimento ai loro uomini e ti si rivolgono prima di andarsene. \"Tieni presente che, se "
       "mai volessi altre armi, saremo sempre disposti a scambiarle con motori di salto nella bacheca dei lavori. "
       "Possiamo però sempre offrirti del denaro, se per te vale di più. Naturalmente possiamo fare questo scambio solo "
       "qui su <origin>, dato che è il luogo dove queste armi avanzate vengono prodotte e immagazzinate.\"",
    10: "L'ingegnere se ne va e tu torni alla tua nave, dopo che ti hanno scortato fuori dalla struttura.",
    11: "<as before (run)> riesci a schivare la lama, ma poi resti senza difese quando la stessa Slegata si fa sotto "
        "con un'altra e cala il fendente. Si ferma all'ultimo istante possibile, con la delusione evidente sul volto.",
    12: "\"È così che 'combatti', capitano? Ti nascondi? Schivi? Ti rifiuti di impadronirti delle nostre armi, quindi "
        "non le avrai.\"",
    13: "<as before (flee)> fuggi dalla lama senza alcuna difficoltà, ma l'Hai che l'ha lanciata ti raggiunge in pochi "
        "secondi e ti immobilizza con la lama alla gola.",
    14: "\"Mi deludi, capitano. In battaglia è di grande importanza individuare i propri vantaggi sul nemico e non "
        "mostrare debolezza fuggendo, altrimenti ti verranno a prendere per ucciderti. Hai fallito in entrambi i modi. "
        "Non avresti mai potuto superarmi in velocità. Hai solo mostrato paura.\"",
    15: "\"Continui davvero a deludermi, capitano. Una volta hai cercato di evitare uno scontro da cui non potevi "
        "fuggire, e l'altra di schivare un'arma che ti era offerta bell'e pronta? Forse davvero non sei un guerriero e "
        "lasci che siano i tuoi subordinati a fare il lavoro sporco.\"",
    16: "\"Non continuerò a insegnarti la stessa lezione! Hai avuto la tua occasione. Non possiamo accettare chi non "
        "impara dai propri errori. A quanto pare non possiamo fidarci di te per le nostre armi più avanzate.\" Poi se ne "
        "va, visibilmente irritata.",
    17: "<leave> L'ingegnere, che aveva assistito allo scontro, spiega poi: \"Dato che non hai superato la prova, non "
        "possiamo ancora darti accesso alla nostra camera blindata. Le nostre armi sono destinate solo ai guerrieri "
        "più capaci. Potrai naturalmente continuare a scambiare motori di salto in cambio di denaro, ma finché non "
        "dimostrerai il contrario, questo è quanto.\"",
    18: "\"Questo errore non è definitivo; sono certo che ti perdonerà volentieri, se solo ci porterai altri motori di "
        "salto. Un altro ingegnere ti aspetterà al portello quando sarà il caso.\"",
    19: "\"Anzi, la tua fama di portatore di motori di salto è tale che non avrà altra scelta che perdonarti nel "
        "prossimo futuro. Un altro ingegnere ti aspetterà al portello quando sarà il caso.\"",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 17, 'UI_LABEL': 2}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 17
assert sum(u['english'].count('"') for u in SRC) == 28
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == []
assert [(u['idx'], ENG[u['idx']]) for u in SRC if u['kind'] == 'UI_LABEL'] == [(1, 'back to choose'), (8, 'buy tripulse')]
assert [(u['idx'], ENG[u['idx']]) for u in SRC if u['kind'] == 'VALUE'] == []
assert collections.Counter(u['context'] for u in SRC) == {'mission:Unfettered Jump Drive Trading': 19}
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert dict(tok) == {'<origin>': 1, '<as before (run)>': 1, '<as before (flee)>': 1, '<leave>': 1}, dict(tok)
assert [u['idx'] for u in SRC if TAGS.findall(u['english'])] == [9, 11, 13, 17]
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (460, 530)
assert db.execute('select max(line) from units where path=?', (SRC[0]['path'],)).fetchone()[0] == 530
assert sorted(D) == list(range(1, 20)), [i for i in range(1, 20) if i not in D]
assert D[1] == L1 and D[8] == L2 and KEY[1] == L1 and KEY[8] == L2

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
    if idx in (1, 8):
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 19, len(dup)
assert T[9].count('<origin>') == 1 and 'su <origin>, dato che' in T[9]
assert T[11].lstrip('\t').startswith('<as before (run)> riesci')
assert T[13].lstrip('\t').startswith('<as before (flee)> fuggi')
assert T[17].lstrip('\t').startswith("<leave> L'ingegnere")

for n, (lo, hi) in enumerate(((1, 6), (7, 12), (13, 19))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('19 unita (6+6+7) · 17 MISSION_TEXT + 2 UI_LABEL · 1 contesto · 19 testi distinti')
print('4 token in 4 unita (9, 11, 13, 17) · 28 virgolette, ZERO dispari · 17 tab')
print('CHIUDE IL FILE: ultima unita alla riga 530 = max(line) del file')
