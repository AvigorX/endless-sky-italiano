"""mkparts.py — L129: `data/human/boarding missions.txt` (89 unita', righe 15-386).

Forma nuova: **48 `TEXT`** sono **frammenti di frase** che il gioco concatena (`${assist merchant 1} <origin>${assist
merchant 2} ${assist merchant 3} <payment>${assist merchant 4}`). Per questo il lotto assume un invariante che gli
altri non avevano: **spazi iniziali e finali identici al sorgente**, unita' per unita', altrimenti la frase composta
si rompe. Due difetti del sorgente si **riproducono**, non si correggono: il frammento `` the `` non ha lo spazio
finale (quindi «theits» in inglese, «ilil» in italiano) e i testi composti sono sgrammaticati per costruzione.

Quattro unita' **non si traducono** perche' non sono testo: le due `CONVERSATION` (1, 2) sono **template di
riferimento** `${...}` e i due `TEXT` 27 e 28 sono **nomi di frase** citati da `phrase`. Restano identici, elencati.
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
KIND = {u['idx']: u['kind'] for u in SRC}
TAGS = re.compile(r'<[^<>]+>')

UNIQ = [
    # --- frammenti di frase: gli spazi finali sono parte del testo ---
    ("Knowing that ", "Sapendo che "),
    ("Since ", "Dal momento che "),
    ("Understanding that ", "Comprendendo che "),
    ("Considering that ", "Considerando che "),
    ("Seeing how ", "Visto che "),
    ("Knowing how ", "Sapendo come "),
    ("you altered course ", "hai cambiato rotta "),
    ("you went out of your way ", "ti sei scomodato "),
    ("you may have altered your own flight plans ", "potresti aver cambiato i tuoi piani di volo "),
    ("you risked your life ", "hai rischiato la vita "),
    ("you risked your ship ", "hai rischiato la nave "),
    ("you risked your own ship ", "hai rischiato la tua nave "),
    ("you braved enemy fire ", "hai affrontato il fuoco nemico "),
    ("you braved danger ", "hai affrontato il pericolo "),
    ("in order to ", "al fine di "),
    ("so that you could ", "così che potessi "),
    ("save ", "salvare "),
    ("repair ", "riparare "),
    ("rescue ", "trarre in salvo "),
    ("secure ", "mettere in sicurezza "),
    ("assist ", "soccorrere "),
    ("help ", "aiutare "),
    ("the", "il"),
    (" and ", " e "),
    ("save its cargo, ", "salvare il suo carico, "),
    ("secure its cargo, ", "mettere in sicurezza il suo carico, "),
    ("save its crew, ", "salvare il suo equipaggio, "),
    ("rescue its crew, ", "trarre in salvo il suo equipaggio, "),
    ("its ", "il suo "),
    ("the ship's ", "della nave "),
    ("the vessel's ", "del vascello "),
    ("relieved ", "sollevato "),
    ("captain ", "capitano "),
    ("gives you", "ti dà"),
    ("offers you", "ti offre"),
    ("rewards you with", "ti ricompensa con"),
    (" in gratitude.", " in segno di gratitudine."),
    (" in appreciation.", " in segno di riconoscenza."),
    (" as an expression of their gratitude.", " come espressione della loro gratitudine."),
    (" in thanks.", " in ringraziamento."),
    (" as thanks.", " come ringraziamento."),
    (" for your assistance.", " per il tuo aiuto."),
    # --- missioni ---
    ("Transport the remaining crew of a destroyed ship",
     "Trasporta l'equipaggio rimasto di una nave distrutta, <bunks> persone che lavoravano sulla <origin>, fino a "
     "<destination>."),
    ("is about to be slammed by a huge asteroid",
     "Mentre ti avvicini alla <origin>, i tuoi sensori radar rilevano che la nave che stai assistendo sta per essere "
     "colpita in pieno da un gigantesco asteroide! In un volo normale non sarebbe un gran problema, ma una nave già "
     "gravemente danneggiata e incapace di schivare potrebbe essere distrutta del tutto."),
    ("Shoot the asteroid", "(Spara all'asteroide.)"),
    ("Maneuver my ship to shield", "(Manovra la mia nave per fare scudo alla <origin>.)"),
    ("Attempt to repair the <origin> so that it can dodge",
     "(Prova a riparare la <origin> così che possa schivare l'asteroide.)"),
    ("Interrupt the docking maneuvers", "(Interrompi le manovre di attracco e vola via.)"),
    ("tearing it to shreds",
     "Giri la nave e attivi i propulsori, cercando di allontanarti il più possibile dalla nave in avaria. Pochi "
     "secondi dopo, l'asteroide si scontra con la <origin>, facendola a pezzi e uccidendo tutti i membri "
     "dell'equipaggio, mentre sulla superficie dell'asteroide lascia poco più che un graffio."),
    ("you've only made things worse",
     "Sparisci all'asteroide nel tentativo di distruggerlo, ma sembra che tu abbia solo peggiorato le cose. "
     "L'asteroide si è ormai spezzato in decine di frammenti più piccoli che volano ancora dritti verso la <origin>. "
     "Prima che tu possa reagire per rimediare all'errore, la maggior parte dei frammenti ha già colpito la "
     "<origin>, che ora si sta rapidamente depressurizzando. Non c'è altro da fare che allontanarsi a una distanza "
     "di sicurezza dalla nave che esplode..."),
    ("The shots you fire quickly break the asteroid",
     "I colpi che spari spezzano rapidamente l'asteroide, i cui frammenti sembrano aver cambiato rotta abbastanza da "
     "mancare del tutto la <origin>. Dopo averla riparata, chiami il suo capitano, che ti ringrazia con un pagamento "
     "di 30.000 crediti."),
    ("hoping to get out of this alive, but as soon as you reach the hatch",
     "Attracchi alla <origin>, sperando di uscirne vivo, ma appena raggiungi il portello l'asteroide colpisce e una "
     "serie di esplosioni comincia a venire dalla nave in avaria. Riesci a raggiungere la cabina di pilotaggio e a "
     "sganciarti, ma l'equipaggio dell'altra nave non ha fatto in tempo a raggiungerti..."),
    ("Most of the other ship's crew has been able to reach",
     "Attracchi alla <origin>, sperando di uscirne vivo, ma, appena raggiungi il portello, l'asteroide colpisce e una "
     "serie di esplosioni comincia a venire dalla nave in avaria. Quando ti sganci, la maggior parte dell'equipaggio "
     "dell'altra nave è riuscita a raggiungere la tua, e ti chiede di portarli su <destination>."),
    ("Okay, it's not far",
     "\"Va bene, non è lontano.\""),
    ("How much can you pay me",
     "\"Quanto potete pagarmi?\""),
    ("I have a few hundred thousand credits",
     "\"Ho qualche centinaio di migliaia di crediti\", dice uno di loro, presumibilmente il capitano. \"Devo "
     "metterne da parte abbastanza per comprare una nuova astronave, ma riceverai comunque una paga decente.\""),
    ("breaks into a million fragments",
     "L'asteroide, dopo aver colpito il tuo scudo, si spezza in un milione di frammenti che si allontanano dalla "
     "<origin>. Dopo averla riparata, chiami il suo capitano, che ti ringrazia con un pagamento di 30.000 crediti."),
    ("hands you <payment>",
     "Il capitano con cui avevi parlato ti ringrazia di nuovo per aver salvato lui e il suo equipaggio, e ti "
     "consegna <payment>."),
    ("Deliver <cargo> to <destination>",
     "Consegna <cargo> a <destination>. Il pagamento è <payment>."),
    ("the fourth time I've nearly died",
     "Quando ripari la <origin>, il capitano ti chiama. \"È la quarta volta che quasi ci lascio le penne questa "
     "settimana facendo questo lavoro! Tieni, porta questo <cargo> a <destination> e finisci il lavoro al posto "
     "mio. Hanno detto che il pagamento è <payment>.\""),
    ("Take the cargo", "(Prendi il carico.)"),
    ("Don't take the cargo", "(Non prendere il carico.)"),
    ("begins loudly swearing",
     "Il capitano comincia a imprecare ad alta voce, così interrompi la comunicazione. Speriamo che arrivi a "
     "destinazione tutto intero."),
    ("You drop off your cargo of <commodity>",
     "Scarichi il tuo carico di <commodity>, spieghi che il mercante che aveva accettato il lavoro ha rinunciato e ti "
     "ha passato il carico, e incassi il pagamento di <payment>."),
    ("only a smaller part of a fleet",
     "Il capitano della <origin> ti ringrazia per la riparazione, ma ti informa che i pirati che li hanno messi fuori "
     "uso sono solo una piccola parte di una flotta che attacca <destination>."),
    ("The authorities of <planet> will probably pay you quite well",
     "Le autorità di <planet> probabilmente ti pagheranno bene se le assisti, ma potrebbe anche essere un modo "
     "facile di farti ammazzare."),
    ("Don't join the fight", "(Non unirti allo scontro.)"),
    ("Join the defense fleet", "(Unisciti alla flotta di difesa.)"),
    ("Defeat a pirate raid on <destination>", "Sconfiggi un'incursione piratesca su <destination>."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'TEXT': 48, 'MISSION_TEXT': 21, 'VALUE': 6, 'DESCRIPTION': 6,
                                                        'CONVERSATION': 6, 'DIALOG': 2}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 22
assert sum(u['english'].count('"') for u in SRC) == 10
ctx = collections.Counter(u['context'] for u in SRC)
print("contesti misurati:", len(ctx), list(ctx.values()))
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {
    '<origin>': 17, '<destination>': 9, '<planet>': 7, '<payment>': 6, '<cargo>': 2, '<bunks>': 1, '<commodity>': 1}

# unita' che NON sono testo: template `${...}` e nomi di frase citati da `phrase`
IDENT = [1, 2, 27, 28]
assert [ENG[i] for i in IDENT] == [
    '${assist merchant 1} <origin>${assist merchant 2} ${assist merchant 3} <payment>${assist merchant 4}',
    '${assist merchant 1 hazardous} <origin>${assist merchant 2} ${assist merchant 3} <payment>${assist merchant 4}',
    'assist merchant 2 simple', 'assist merchant 2 complex']
VAL = [u['idx'] for u in SRC if u['kind'] == 'VALUE']
assert VAL == [51, 71, 82, 84, 86, 88], VAL
assert [ENG[i] for i in VAL] == ['Passengers to <planet>', 'Delivery to <planet>'] + ['Defend <planet>'] * 4

KEY = {i: e.lstrip('	') for i, e in ENG.items()}   # il tab iniziale lo antepone il costruttore
distinct = list(dict.fromkeys(KEY.values()))
assert len(distinct) == 77, len(distinct)     # 80 testi grezzi, ma tre coppie con tab collassano
prose = [e for e in distinct if e not in {KEY[i] for i in IDENT} and e not in {KEY[i] for i in VAL}]
assert len(prose) == len(UNIQ) == 70, (len(prose), len(UNIQ), [e for e in prose if e not in [s for s, _ in UNIQ]])


def resolve(eng):
    hits = [t for s, t in UNIQ if s == eng]
    assert len(hits) == 1, (len(hits), eng[:90], hits)
    return hits[0]


cover = {e: resolve(e) for e in prose}
assert len(cover) == 70

T = {}
for u in SRC:
    eng = u['english']
    if u['idx'] in IDENT or u['kind'] == 'VALUE':
        T[u['idx']] = eng
    else:
        T[u['idx']] = '	' * (len(eng) - len(eng.lstrip('	'))) + cover[KEY[u['idx']]]

for idx, txt in T.items():
    eng, kind = ENG[idx], KIND[idx]
    assert txt.count('	') == eng.count('	'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    # invariante dei frammenti: spazio iniziale e finale identici (lo spazio finale e' parte del testo)
    assert len(txt) - len(txt.rstrip()) == len(eng) - len(eng.rstrip()),         ('spazio finale diverso', idx, repr(eng), repr(txt))
    assert len(txt.lstrip('	')) - len(txt.lstrip('	').lstrip(' ')) ==         len(eng.lstrip('	')) - len(eng.lstrip('	').lstrip(' ')), ('spazio iniziale diverso', idx)
    assert not re.search(r'[\[\]`’—–…]', txt), idx
    assert not re.search(r"(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if idx in IDENT or kind == 'VALUE':
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), repr(eng))

for n, (lo, hi) in enumerate(((1, 30), (31, 60), (61, 89))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('89 unita (30+30+29) · 70 testi tradotti + 4 identici (2 template, 2 nomi di frase) + 6 VALUE = 80 distinti')
print('spazi iniziali/finali identici al sorgente su tutte le 89 unita · 22 tab · 10 virgolette · 43 token in 7 famiglie')
