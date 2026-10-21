"""mkparts.py — L118: costruisce `parts/part01-04.json` (104 unita', righe 1627-2955).

Stesso file di L117, forma diversa: **36 `DIALOG`**, **33 `VALUE`**, **33 `DESCRIPTION`**, solo **2
`MISSION_TEXT`**, e **192 token in nove famiglie** (compaiono `<system>`, `<day>`, `<npc>`, `<date>`).

Regole applicate:
- **33 `VALUE` identici al sorgente**: sono nomi di missione (`Transfer slaves to <planet>`,
  `Merchants near <system>`…) e alcuni contengono un token; decisione 259/L103.
- **tre testi sono gia' tradotti in L117** (il criminale galattico e la sua irruzione): la resa si **rilegge**
  da `staging/editorial/L117_*/translation.json` invece di riscriverla, e si **asserisce** che sia la stessa.
- **25 testi nuovi** si scrivono **una volta** in `UNIQ` e si assegnano per firma univoca: **39 testi distinti**
  per 104 unita'.

Premesse misurate e asserite:
- **104 unita'**, tutte `PENDING`, tipi `{'DIALOG': 36, 'VALUE': 33, 'DESCRIPTION': 33, 'MISSION_TEXT': 2}`;
- **33 contesti** (19 con quattro unita', 14 con due);
- **zero tab**, **zero quadre**, **zero virgolette** (asserzione vuota), **zero backtick**;
- **192 token**: `<planet>` 53, `<payment>` 52, `<destination>` 33, `<system>` 33, `<day>` 17, `<npc>` 9,
  `<date>` 9, `<bunks>` 5, `<cargo>` 2 — parita' per simbolo **e** per unita'.
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

# testi gia' resi in L117: la resa si rilegge, non si riscrive
PREV = {}
for f in glob.glob(os.path.join(L10N, 'staging/editorial/L117_*', 'translation.json')):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        PREV[u['english']] = u['italian']

UNIQ = [
    ("slaves in secure cells",
     "Un pirata su <planet> ha comprato degli schiavi da un signore della guerra locale. Trasferisci questi "
     "<bunks> schiavi in celle sicure su <destination> per <payment>. La schiavitù è punita con la morte in "
     "tutta la galassia, quindi potrebbe essere un lavoro pericoloso da accettare."),
    ("help them escape local law enforcement",
     "Il capitano della <npc> ti pagherà <payment> per aiutarla a sfuggire alle forze dell'ordine locali e a "
     "raggiungere <destination> entro <date>."),
    ("their illegal cargo safely",
     "Il capitano della <npc> ti pagherà <payment> per scortare lui e il suo carico illegale attraverso spazio "
     "controllato dalle forze dell'ordine, fino a raggiungere <destination> entro <date>."),
    ("their stolen vessel safely",
     "Il capitano della <npc> ti pagherà <payment> per scortare lui e la sua nave rubata attraverso spazio "
     "controllato dalle forze dell'ordine, fino a raggiungere <destination> entro <date>."),
    ("within four jumps",
     "Una flotta della Marina entro quattro salti dal sistema <system> ha fermato le nostre razzie. Distruggila "
     "e torna su <planet> entro <day> per un compenso di <payment>."),
    ("A large Navy fleet",
     "Una grande flotta della Marina vicino al sistema <system> ha fermato le nostre razzie. Distruggila e torna "
     "su <planet> entro <day> per un compenso di <payment>."),
    ("A Syndicate fleet near",
     "Una flotta del Sindacato vicino al sistema <system> ha fermato le nostre razzie. Distruggila e torna su "
     "<planet> entro <day> per un compenso di <payment>."),
    ("A large Syndicate fleet",
     "Una grande flotta del Sindacato vicino al sistema <system> ha fermato le nostre razzie. Distruggila e "
     "torna su <planet> entro <day> per un compenso di <payment>."),
    ("A militia fleet near",
     "Una flotta della milizia vicino al sistema <system> ha fermato le nostre razzie. Distruggila e torna su "
     "<planet> entro <day> per un compenso di <payment>."),
    ("A large militia fleet",
     "Una grande flotta della milizia vicino al sistema <system> ha fermato le nostre razzie. Distruggila e "
     "torna su <planet> entro <day> per un compenso di <payment>."),
    ("A small rival gang",
     "Una piccola banda rivale sta creando problemi vicino al sistema <system>. Eliminala e torna su <planet> "
     "entro <day> per un compenso di <payment>."),
    ("A large rival gang",
     "Una grande banda rivale sta diventando troppo potente. Il suo capo si trova vicino al sistema <system>. "
     "Elimina lui e le sue scorte e torna su <planet> entro <day> per un compenso di <payment>."),
    ("A small marauder gang",
     "Una piccola banda di predoni sta creando problemi vicino al sistema <system>. Eliminala e torna su "
     "<planet> entro <day> per un compenso di <payment>."),
    ("A marauder gang is gaining",
     "Una banda di predoni sta diventando troppo potente. Il suo capo si trova vicino al sistema <system>. "
     "Elimina lui e le sue scorte e torna su <planet> entro <day> per un compenso di <payment>."),
    ("grown dissatisfied with the actions",
     "I pirati del sistema <system> sono sempre più scontenti delle azioni della banda di predoni che lo "
     "governa. Eliminala e torna su <planet> entro <day> per un compenso di <payment>."),
    ("in Republic space",
     "Una flotta mercantile è stata avvistata in spazio della Repubblica. Unisciti allo scontro per distruggerla "
     "e torna su <planet>, nel sistema <system>, entro <day> per una parte del bottino (<payment>)."),
    ("in Syndicate space",
     "Una flotta mercantile è stata avvistata in spazio del Sindacato. Unisciti allo scontro per distruggerla e "
     "torna su <planet>, nel sistema <system>, entro <day> per una parte del bottino (<payment>)."),
    ("The fleet has been eliminated",
     "La flotta è stata eliminata. Puoi riscuotere il compenso tornando su <destination>."),
    ("for eliminating the Navy fleet",
     "I pirati di <planet> ti pagano con gratitudine <payment> per aver eliminato la flotta della Marina."),
    ("for eliminating the Syndicate fleet",
     "I pirati di <planet> ti pagano con gratitudine <payment> per aver eliminato la flotta del Sindacato."),
    ("for eliminating the militia fleet",
     "I pirati di <planet> ti pagano con gratitudine <payment> per aver eliminato la flotta della milizia."),
    ("for eliminating the rival gang",
     "I pirati di <planet> ti pagano con gratitudine <payment> per aver eliminato la banda rivale."),
    ("for eliminating the ruling gang",
     "I pirati di <planet> ti pagano con gratitudine <payment> per aver eliminato la banda che governa il "
     "sistema."),
    ("The merchants have been eliminated",
     "I mercanti sono stati eliminati. Torna su <destination> per la tua parte del bottino."),
    ("After counting up the loot",
     "Dopo aver contato il bottino della flotta mercantile distrutta, ti viene data la tua parte. <payment>"),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
STATES = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(STATES.values()) == {'PENDING'}, {k: v for k, v in STATES.items() if v != 'PENDING'}
assert len(UNIQ) == 25, len(UNIQ)

names = {u['english'] for u in SRC if u['kind'] == 'VALUE'}
prose = [e for e in dict.fromkeys(u['english'] for u in SRC) if e not in names]
assert len(names) == 11 and len(prose) == 28, (len(names), len(prose))
reused = [e for e in prose if e in PREV]
assert len(reused) == 3, len(reused)


def resolve(eng):
    if eng in PREV:
        return PREV[eng]
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:80], hits)
    return hits[0]


cover = {e: resolve(e) for e in prose}
assert len(set(cover.values())) == 28, 'due testi distinti con la stessa resa'
T = {u['idx']: (u['english'] if u['kind'] == 'VALUE' else cover[u['english']]) for u in SRC}

# --- premesse strutturali ------------------------------------------------------------------
assert sum(1 for u in SRC if '\t' in u['english']) == 0
assert sum(u['english'].count('`') for u in SRC) == 0
assert sum(u['english'].count('"') for u in SRC) == 0            # asserzione vuota: zero virgolette
assert collections.Counter(u['kind'] for u in SRC) == {'DIALOG': 36, 'VALUE': 33,
                                                       'DESCRIPTION': 33, 'MISSION_TEXT': 2}
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 33 and collections.Counter(ctx.values()) == {4: 19, 2: 14}
tok = collections.Counter(t for u in SRC for t in TAGS.findall(u['english']))
assert tok == {'<planet>': 53, '<payment>': 52, '<destination>': 33, '<system>': 33, '<day>': 17,
               '<npc>': 9, '<date>': 9, '<bunks>': 5, '<cargo>': 2}, tok

for idx, txt in T.items():
    eng = ENG[idx]
    assert '\t' not in txt, idx
    assert txt.count('"') == 0 == eng.count('"'), idx
    assert TAGS.findall(txt) == TAGS.findall(eng), (idx, TAGS.findall(txt), TAGS.findall(eng))
    assert '[' not in txt and ']' not in txt and '`' not in txt, idx
    if KIND[idx] == 'VALUE':
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:50], txt[:50])

# --- parti canoniche ----------------------------------------------------------------------
for n, (lo, hi) in enumerate(((1, 26), (27, 52), (53, 78), (79, 104))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('104 unita (26x4) · 33 VALUE identici · 28 testi prosaici (3 da L117) · 33 contesti · 192 token in 9 famiglie')
