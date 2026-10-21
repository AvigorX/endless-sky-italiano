"""mkparts.py — L144: `data/hai/unfettered 0 prologue.txt`, righe 367-420 (20 unita').

**Arrivano i token**: `<hood>` (unita' 1, incollato a «Slegato» come nell'inglese «Hai<hood>») e `<learned>`
(unita' 20, a inizio frase dopo un punto, quindi con la maiuscola che segue). Sono segnaposto del motore: restano
**dove stanno** e la frase italiana si costruisce **intorno** a loro.

`outfitter` -> **fornitore** (45 occorrenze gia' in staging, contro 2 di «equipaggiatore» e 1 di «armiere»).
Le due scelte `(No.)` e `(Yes.)` compaiono ancora: `(No.)` identico in `ID_OK`, `(Yes.)` -> «(Sì.)».
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

NO = "(No.)"
YES = "(Sì.)"

D = {
    1: "Mentre esci dalla nave per andare allo spazioporto, vedi che un Hai Slegato<hood> ti aspetta al portello.",
    2: "Avvicinandoti, deduci che sia un ingegnere, a giudicare dalla tavoletta e dall'attrezzatura che porta. Forse "
       "intende scambiare qualcosa di diverso dal denaro. Vuoi trattare con loro per un altro motore?",
    3: "Probabilmente intendono offrirti lo stesso accordo di prima: motori di salto in cambio di armi. Vuoi provare a "
       "dimostrare il tuo valore questa volta, e trattare per un motore di salto?",
    4: NO,
    5: YES,
    6: "Appena metti piede sul mondo, la presunta ingegnera lascia cadere la propria attrezzatura e ti lancia una lama, "
       "proprio come l'altra volta: sembra che non voglia più perdere tempo con te.",
    7: "Esci dalla nave, ma prima ancora di raggiungere l'ingegnere, un altro Slegato grida per attirare la tua "
       "attenzione e poi ti lancia una lama, senza altri avvertimenti né cerimonie.",
    8: "Esci dalla nave e subito l'ingegnere ti conduce dal fornitore. \"Abbiamo armi da mostrarti, per il tuo aiuto "
       "nel procurarci motori di salto. Per ora potrai commerciare solo per una, ma se continuerai ad assisterci, "
       "potresti dimostrarti degno di accedere alle altre.\" Non si fermano mai a chiedere se le nuove armi ti "
       "interessano davvero.",
    9: "(Seguili.)",
    10: "\"Le armi Hai non mi interessano davvero.\"",
    11: "\"Non ho davvero voglia di farlo adesso.\"",
    12: "\"Che maleducazione. Meglio che speri ci sia qualcun altro a guidarti la prossima volta!\" dice l'ingegnere "
        "mentre torni alla tua nave.",
    13: "\"Queste non sono armi Hai standard, capitano, credimi. E sarebbe poco saggio giudicare prima di vederle, "
        "no?\"",
    14: "Ti conducono attraverso il solito fornitore, ma poi vanno in una zona che non avevi mai notato, probabilmente "
        "perché non dovevi. Mentre stai per passare quello che supponi essere un controllo di sicurezza, uno Slegato ti "
        "lancia una lama in faccia!",
    15: "Riconosci la stessa Slegata dell'altra volta; deve adorare lanciare lame alla gente.",
    16: "(Prova ad afferrarla.)",
    17: "(Prova a schivarla.)",
    18: "(Balza di lato e usa la mia arma.)",
    19: "(Fuggi.)",
    20: "Balzi di lato, afferrando la tua arma appena in tempo per minacciare lo Slegato che ti ha lanciato la lama. "
        "Sembrando un po' sorpreso dalle tue tattiche poco ortodosse, abbassa la propria arma. \"Ben fatto! In verità, "
        "non c'è onore più alto che sopravvivere sul campo di battaglia, perché solo allora puoi portare il bottino a "
        "chi ne ha bisogno! Una tattica è buona solo se riesci a trovarla ed eseguirla abbastanza in fretta da darti "
        "un vantaggio, e tu l'hai fatto. <learned>Sono Desneeparu, ed è un piacere conoscerti, capitano.\"",
}

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'MISSION_TEXT': 20}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 19
assert sum(u['english'].count('"') for u in SRC) == 12
assert [u['idx'] for u in SRC if u['english'].count('"') % 2] == []
assert collections.Counter(u['context'] for u in SRC) == {'mission:Unfettered Jump Drive Trading': 20}
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert dict(tok) == {'<hood>': 1, '<learned>': 1}, dict(tok)
assert [u['idx'] for u in SRC if TAGS.findall(u['english'])] == [1, 20]
assert [u['idx'] for u in SRC if u['kind'] in ('VALUE', 'UI_LABEL', 'LOGBOOK')] == []
assert (min(u['line'] for u in SRC), max(u['line'] for u in SRC)) == (367, 420)
assert sorted(D) == list(range(1, 21)), [i for i in range(1, 21) if i not in D]
assert D[4] == NO and KEY[4] == '(No.)' and D[5] == YES

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
    if idx == 4:
        assert txt.lstrip('\t') == '(No.)', idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

dup = {}
for u in SRC:
    dup.setdefault(KEY[u['idx']], set()).add(T[u['idx']])
assert not [(k, v) for k, v in dup.items() if len(v) > 1]
assert len(dup) == 20, len(dup)
assert T[1].count('<hood>') == 1 and T[20].count('<learned>') == 1
assert '<hood>' in T[1] and 'Slegato<hood>' in T[1]
assert '. <learned>Sono Desneeparu' in T[20]
assert ' '.join(T.values()).count('(Sì.)') == 1

for n, (lo, hi) in enumerate(((1, 7), (8, 14), (15, 20))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('20 unita (7+7+6) · 1 contesto · 20 testi distinti · (No.) identico · (Sì.) una volta')
print('2 token in 2 unita (1 = 1 ciascuno) · 19 tab · 12 virgolette')
