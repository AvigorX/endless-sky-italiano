"""mkparts.py — L119: chiude `data/human/pirate jobs.txt` (77 unita', righe 2958-3706, confine `fine file`).

Terza forma dello stesso file: **32 `DIALOG`**, **17 `DESCRIPTION`**, **16 `VALUE`**, **12 `CONVERSATION`** —
quest'ultimo tipo non compariva nei due lotti precedenti, e porta **9 unita' che iniziano con tab** e **6
virgolette** (due per ciascuna scena, dentro le battute).

Regole:
- **16 `VALUE` identici al sorgente** (4 nomi distinti: `Merchants near <system>`, `Defend <planet>`,
  `Convoy near <system>`, `Assassinate a political target`).
- **2 testi vengono da L118** (`The merchants have been eliminated…`, `After counting up the loot…`): la resa si
  **rilegge** dal suo `translation.json`.
- **41 testi nuovi** in `UNIQ`, assegnati per firma univoca: **47 testi distinti** per 77 unita'.
- **Una deroga dichiarata**: l'unita' 73 ha nel sorgente «thanks you for eliminating the politician **pays** you»
  (manca «and»). E' un refuso, e la resa e' **identica** a quella dell'unita' 65: anziche' inventare una
  differenza, la si dichiara in `EXC` e il controllo la ammette.
"""
import collections
import glob
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

PREV = {}
for lot in ('L117_*', 'L118_*'):
    for f in glob.glob(os.path.join(L10N, 'staging/editorial', lot, 'translation.json')):
        for u in json.load(open(f, encoding='utf-8'))['units']:
            PREV[u['english']] = u['italian']

# unita' con resa identica a un'altra pur avendo un inglese diverso: refuso del sorgente, dichiarato
EXC = {73: 'sorgente: «eliminating the politician pays you», manca «and»; resa uguale all\'unita\' 65'}

UNIQ = [
    # --- Raid on Merchants (South): la flotta meridionale ---
    ("in Southern space. Join in destroying",
     "Una flotta mercantile è stata avvistata in spazio meridionale. Unisciti allo scontro per distruggerla e "
     "torna su <planet>, nel sistema <system>, entro <day> per una parte del bottino (<payment>)."),
    # --- Difesa dei pirati: Marina ---
    ("Local Navy forces are attacking",
     "Forze della Marina locale stanno attaccando <destination>! Sconfiggile per difendere l'anarchia!"),
    ("The Navy fleets have been defeated",
     "Le flotte della Marina sono state sconfitte. Torna su <destination>."),
    ("collectively pay you <payment> for helping to drive off the Navy",
     "Molti abitanti di <planet> ti ringraziano e ti pagano collettivamente <payment> per aver contribuito a "
     "respingere la Marina."),
    ("thank you for helping to drive off the Navy.",
     "Molti abitanti di <planet> ti ringraziano per aver contribuito a respingere la Marina."),
    ('"We are under attack! <planet> is under attack by the Navy!',
     "All'improvviso senti voci concitate e grida fuori: \"Siamo sotto attacco! <planet> è sotto attacco della "
     "Marina! Ci serve ogni nave in grado di combattere per le difese!\" Potrebbe essere un modo facile per farti "
     "uccidere, e non hai nemmeno la garanzia di essere pagato per il tuo lavoro."),
    ("(Stay here until the fight is over.)",
     "(Resta qui finché la battaglia non è finita.)"),
    ("(Join the defense fleet.)",
     "(Unisciti alla flotta di difesa.)"),
    ("repel the Navy attack",
     "Le forze piratesche locali si preparano a respingere l'attacco della Marina. Ti unisci a loro e decollate "
     "insieme..."),
    # --- Difesa dei pirati: Sindacato ---
    ("Local Syndicate forces are attacking",
     "Forze del Sindacato locale stanno attaccando <destination>! Sconfiggile per difendere l'anarchia!"),
    ("The Syndicate fleets have been defeated",
     "Le flotte del Sindacato sono state sconfitte. Torna su <destination>."),
    ("collectively pay you <payment> for helping to drive off the Syndicate",
     "Molti abitanti di <planet> ti ringraziano e ti pagano collettivamente <payment> per aver contribuito a "
     "respingere il Sindacato."),
    ("thank you for helping to drive off the Syndicate.",
     "Molti abitanti di <planet> ti ringraziano per aver contribuito a respingere il Sindacato."),
    ('"We are under attack! <planet> is under attack by the Syndicate!',
     "All'improvviso senti voci concitate e grida fuori: \"Siamo sotto attacco! <planet> è sotto attacco del "
     "Sindacato! Ci serve ogni nave in grado di combattere per le difese!\" Potrebbe essere un modo facile per "
     "farti uccidere, e non hai nemmeno la garanzia di essere pagato per il tuo lavoro."),
    ("repel the Syndicate attack",
     "Le forze piratesche locali si preparano a respingere l'attacco del Sindacato. Ti unisci a loro e decollate "
     "insieme..."),
    # --- Difesa dei pirati: milizia ---
    ("Local militia forces are attacking",
     "Forze della milizia locale stanno attaccando <destination>! Sconfiggile per difendere l'anarchia!"),
    ("The militia fleets have been defeated",
     "Le flotte della milizia sono state sconfitte. Torna su <destination>."),
    ("collectively pay you <payment> for helping to drive off the militia",
     "Molti abitanti di <planet> ti ringraziano e ti pagano collettivamente <payment> per aver contribuito a "
     "respingere la milizia."),
    ("thank you for helping to drive off the militia forces.",
     "Molti abitanti di <planet> ti ringraziano per aver contribuito a respingere la milizia."),
    ('"We are under attack! <planet> is under attack by the militia!',
     "All'improvviso senti voci concitate e grida fuori: \"Siamo sotto attacco! <planet> è sotto attacco della "
     "milizia! Ci serve ogni nave in grado di combattere per le difese!\" Potrebbe essere un modo facile per farti "
     "uccidere, e non hai nemmeno la garanzia di essere pagato per il tuo lavoro."),
    ("repel the militia attack",
     "Le forze piratesche locali si preparano a respingere l'attacco della milizia. Ti unisci a loro e decollate "
     "insieme..."),
    # --- carico segreto ---
    ("Cargo stolen from a merchant ship",
     "Carico rubato a una nave mercantile, che ha attirato l'interesse di un signore della guerra pirata."),
    ("in Republic space near the <system> system. A local warlord",
     "Un convoglio mercantile è stato avvistato in spazio della Repubblica vicino al sistema <system>. Un signore "
     "della guerra locale è interessato a impossessarsi del carico della <npc>. Saccheggialo e torna su <planet> "
     "entro <day> per un compenso di <payment>."),
    ("in Syndicate space near the <system> system. A local warlord",
     "Un convoglio mercantile è stato avvistato in spazio del Sindacato vicino al sistema <system>. Un signore "
     "della guerra locale è interessato a impossessarsi del carico della <npc>. Saccheggialo e torna su <planet> "
     "entro <day> per un compenso di <payment>."),
    ("in Southern space near the <system> system. A local warlord",
     "Un convoglio mercantile è stato avvistato in spazio meridionale vicino al sistema <system>. Un signore della "
     "guerra locale è interessato a impossessarsi del carico della <npc>. Saccheggialo e torna su <planet> entro "
     "<day> per un compenso di <payment>."),
    ("but you don't have the secret cargo",
     "Atterri su <planet>, ma non hai il carico segreto! Torna alla <npc> e riporta il carico su <planet>."),
    ("take the secret cargo from your cargo hold",
     "I pirati di <planet> prendono il carico segreto dalla tua stiva e ti pagano <payment>."),
    # --- assassinii politici ---
    ("worrying local slave traders",
     "Un politico dei Mondi Liberi che sta preoccupando i trafficanti di schiavi locali è stato avvistato mentre "
     "attraversava lo spazio dei Mondi Liberi vicino al sistema <system> sulla sua nave, la <npc>. Assassinalo "
     "entro <day> per mandare un messaggio ai Mondi Liberi. Il compenso è <payment>. Attenzione: potrebbe avere "
     "delle scorte."),
    ("angered a pirate warlord",
     "Un politico dei Mondi Liberi che ha fatto arrabbiare un signore della guerra pirata è stato avvistato mentre "
     "attraversava lo spazio dei Mondi Liberi vicino al sistema <system> sulla sua nave, la <npc>. Assassinalo "
     "entro <day> per mandare un messaggio ai Mondi Liberi. Il compenso è <payment>. Attenzione: potrebbe essere "
     "pesantemente difeso."),
    ("A Syndicate politician was spotted",
     "Un politico del Sindacato è stato avvistato mentre attraversava lo spazio del Sindacato vicino al sistema "
     "<system> sulla sua nave, la <npc>. Assassinalo entro <day> per mandare un messaggio al Sindacato. Il "
     "compenso è <payment>. Attenzione: potrebbe avere delle scorte."),
    ("plans that worry local pirate gangs",
     "Un politico del Sindacato con progetti che preoccupano le bande piratesche locali è stato avvistato mentre "
     "attraversava lo spazio del Sindacato vicino al sistema <system> sulla sua nave, la <npc>. Assassinalo entro "
     "<day> per mandare un messaggio al Sindacato. Il compenso è <payment>. Attenzione: potrebbe essere "
     "pesantemente difeso."),
    ("worrying local pirate gangs",
     "Un politico della Repubblica che sta preoccupando le bande piratesche locali è stato avvistato mentre "
     "attraversava lo spazio abitato della Repubblica vicino al sistema <system> sulla sua nave, la <npc>. "
     "Assassinalo entro <day> per mandare un messaggio alla Repubblica. Il compenso è <payment>. Attenzione: "
     "potrebbe avere delle scorte."),
    ("worrying local drug traders",
     "Un politico della Repubblica che sta preoccupando i trafficanti di droga locali è stato avvistato mentre "
     "attraversava lo spazio abitato della Repubblica vicino al sistema <system> sulla sua nave, la <npc>. "
     "Assassinalo entro <day> per mandare un messaggio alla Repubblica. Il compenso è <payment>. Attenzione: "
     "potrebbe essere pesantemente difeso."),
    ("for your payment.",
     "L'obiettivo è stato distrutto. Torna su <destination> per il tuo compenso."),
    ("for payment.",
     "L'obiettivo è stato distrutto. Torna su <destination> per il compenso."),
    ("band of slave traders thank you",
     "Una banda di trafficanti di schiavi ti ringrazia per aver eliminato il politico e ti paga <payment>."),
    ("eliminating the politician that threatened them",
     "Il signore della guerra pirata ti ringrazia per aver eliminato il politico che lo minacciava e ti paga "
     "<payment>."),
    ("A pirate warlord thanks you for eliminating the politician and pays",
     "Un signore della guerra pirata ti ringrazia per aver eliminato il politico e ti paga <payment>."),
    ("A band of pirates thank you",
     "Una banda di pirati ti ringrazia per aver eliminato il politico e ti paga <payment>."),
    ("eliminating the politician pays you",
     "Un signore della guerra pirata ti ringrazia per aver eliminato il politico e ti paga <payment>."),
    ("band of drug traders thank you",
     "Una banda di trafficanti di droga ti ringrazia per aver eliminato il politico e ti paga <payment>."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'DIALOG': 32, 'VALUE': 16,
                                                       'DESCRIPTION': 17, 'CONVERSATION': 12}
names = {u['english'] for u in SRC if u['kind'] == 'VALUE'}
prose = [e for e in dict.fromkeys(u['english'] for u in SRC) if e not in names]
assert len(names) == 4 and len(prose) == 43, (len(names), len(prose))
reused = [e for e in prose if e in PREV]
assert len(reused) == 2, reused
assert len({e for e in prose if e not in PREV}) == 41, len([e for e in prose if e not in PREV])


def resolve(eng):
    if eng in PREV:
        return PREV[eng]
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:90], hits)
    return hits[0]


cover = {e: resolve(e) for e in prose}
assert len(set(cover.values())) == len(cover) - 1, 'un solo doppio di resa, quello dichiarato (unita 73)'
T = {}
for u in SRC:
    eng = u['english']
    if u['kind'] == 'VALUE':
        T[u['idx']] = eng
    else:
        # il testo della parte non porta tab: il costruttore li antepone dal sorgente
        T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + cover[eng].lstrip('\t')

# --- premesse strutturali ------------------------------------------------------------------
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 9, 'unita con tab iniziale'
assert sum(u['english'].count('"') for u in SRC) == 6
assert sum(u['english'].count('`') for u in SRC) == 0
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 20 and collections.Counter(ctx.values()) == {4: 19, 1: 1}, collections.Counter(ctx.values())
TOK = {'<planet>': 28, '<payment>': 23, '<destination>': 19, '<system>': 14, '<npc>': 12, '<day>': 10}
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == TOK

for idx, txt in T.items():
    eng = ENG[idx]
    assert '\t\t' not in txt, idx
    assert (txt.startswith('\t'), txt.count('\t')) == (eng.startswith('\t'), eng.count('\t')), idx
    assert txt.count('"') == eng.count('"'), (idx, txt.count('"'), eng.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if KIND[idx] == 'VALUE':
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for n, (lo, hi) in enumerate(((1, 20), (21, 40), (41, 60), (61, 77))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('77 unita (20+20+20+17) · 16 VALUE identici (4 nomi) · 43 testi prosaici (2 da L118) · 20 contesti')
print('9 unita con tab · 6 virgolette · 106 token in 6 famiglie · 1 deroga dichiarata (unita 73)')
