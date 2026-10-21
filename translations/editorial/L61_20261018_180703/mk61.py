# -*- coding: utf-8 -*-
"""Adatta il verify.py di L60 a L61 (26 unita', righe 511-552, NT vuoto, 1 token <origin>)."""
p = 'verify.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep('''r"""verify.py — L60 (data/human/culture conversations.txt, 31 unita', righe 437-495)

**Segmento interno**: 85 unita' prima (L58+L59), **258 dopo** la 495, file di 374, `max(line) = 1122`.
La finestra di export era 429-495 ma la prima unita' sta sulla **437**: si asserisce il valore **misurato**
(decisione 196). La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L59, tutte asserite:
  - **`NT` positivo: 2 `UI_LABEL`** (6 `pass by`, 20 `get out`), identiche al sorgente;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **0 token** `<…>`: parita' 0/0 asserita su ogni unita';
  - **27 tab**, **40 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **0 gruppi di duplicati inglesi**: controllo negativo dichiarato.''',
    '''r"""verify.py — L61 (data/human/culture conversations.txt, 26 unita', righe 511-552)

**Segmento interno**: 116 unita' prima (L58+L59+L60), **232 dopo** la 552, file di 374,
`max(line) = 1122`. La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L60, tutte asserite:
  - **`NT` vuoto** (0 `UI_LABEL`): assenza dichiarata, dopo il `NT` positivo di L60;
  - **1 token `<origin>`**: parita' esatta 1/1, nello stesso punto (unita' 11);
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **25 tab**, **38 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **2 gruppi di duplicati inglesi** (18/24, 20/26), resa identica asserita.''')

rep("""  5. collocazione: 31 unita', righe 437-495
  6. segmento interno: 85 prima, 258 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [437, 495] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 29 `MISSION_TEXT` + 2 `UI_LABEL`""",
    """  5. collocazione: 26 unita', righe 511-552
  6. segmento interno: 116 prima, 232 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [511, 552] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 26 `MISSION_TEXT`""")

rep("""  9. `NT` positivo su 6 e 20; assenze dichiarate per `DIALOG`, `LOGBOOK`, `CONVERSATION`, `TEXT`, token,
     quadre, backtick
 10. 27 tab e 40 virgolette""",
    """  9. `NT` vuoto; assenze dichiarate per `DIALOG`, `LOGBOOK`, `CONVERSATION`, `TEXT`, quadre, backtick
 10. 25 tab e 38 virgolette""")

rep(" 14. duplicati inglesi: **nessun gruppo** (controllo negativo) e nessuna resa ripetuta",
    " 14. duplicati inglesi: 2 gruppi, resa identica; nessuna resa ripetuta fra inglesi diversi")

rep("NT = set([6, 20])", "NT = set()")

rep("   len(tu) == 31 and (first, last) == (437, 495), (len(tu), first, last))",
    "   len(tu) == 26 and (first, last) == (511, 552), (len(tu), first, last))")

rep("""ck('segmento interno: 85 prima, 258 dopo, 374 totali',
   before == 85 and after == 258 and tot == 374, (before, after, tot))""",
    """ck('segmento interno: 116 prima, 232 dopo, 374 totali',
   before == 116 and after == 232 and tot == 374, (before, after, tot))""")

rep("""ck('copertura del segmento: righe 437-495 continue',
   lrows[0] == 437 and lrows[-1] == 495)""",
    """ck('copertura del segmento: righe 511-552 continue',
   lrows[0] == 511 and lrows[-1] == 552)""")

rep("ck('nessun altra unita nel DB dentro 437-495 (%d)' % inrange, inrange == len(tu), inrange)",
    "ck('nessun altra unita nel DB dentro 511-552 (%d)' % inrange, inrange == len(tu), inrange)")

rep("""ck('distribuzione dei kind: 29 MISSION_TEXT + 2 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 29, 'UI_LABEL': 2}, dict(kinds))""",
    """ck('distribuzione dei kind: 26 MISSION_TEXT', dict(kinds) == {'MISSION_TEXT': 26}, dict(kinds))""")

rep("""ck('UI_LABEL: 2 attese, tutte elencate', ui == sorted(NT) == [6, 20], ui)
notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('NT: le 2 label identiche al sorgente', not notid, notid)""",
    """ck('UI_LABEL: nessuna nel segmento (assenza dichiarata)', ui == [] and NT == set(), ui)""")

rep("""ck('token <...>: 0 nel sorgente e 0 in italiano (assenza dichiarata)',
   tok_en == 0 and tok_it == 0, (tok_en, tok_it))""",
    """ck('token <...>: 1 nel sorgente e 1 in italiano', tok_en == 1 and tok_it == 1, (tok_en, tok_it))""")

rep("ck('tab e virgolette: parita per unita (31 unita)', per_unit == [], per_unit[:10])",
    "ck('tab e virgolette: parita per unita (26 unita)', per_unit == [], per_unit[:10])")

rep("ck('tab iniziale presente dove il sorgente lo ha (27)', ntab == 27 and lead == [], (ntab, lead[:5]))",
    "ck('tab iniziale presente dove il sorgente lo ha (25)', ntab == 25 and lead == [], (ntab, lead[:5]))")

rep("""(('\\t', 'tab', 27), ('"', 'virgolette', 40))""",
    """(('\\t', 'tab', 25), ('"', 'virgolette', 38))""")

rep("""ck('duplicati inglesi: nessun gruppo (controllo negativo)', len(dup_en) == 0 and dup_ok,
   (len(dup_en), dup_ok))""",
    """ck('duplicati inglesi (2 gruppi, 4 unita): resa italiana identica',
   len(dup_en) == 2 and dup_ok, (len(dup_en), dup_ok))""")

rep("'verify L60 superato' if not fail else 'verify L60 fallito'",
    "'verify L61 superato' if not fail else 'verify L61 fallito'")

open(p, 'w', encoding='utf-8').write(s)
print('verify.py adattato a L61')
