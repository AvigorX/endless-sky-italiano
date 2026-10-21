# -*- coding: utf-8 -*-
"""Adatta il verify.py di L61 a L62 (30 unita', righe 566-611, NT positivo su 4/15/26)."""
p = 'verify.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep('''r"""verify.py — L61 (data/human/culture conversations.txt, 26 unita', righe 511-552)

**Segmento interno**: 116 unita' prima (L58+L59+L60), **232 dopo** la 552, file di 374,
`max(line) = 1122`. La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L60, tutte asserite:
  - **`NT` vuoto** (0 `UI_LABEL`): assenza dichiarata, dopo il `NT` positivo di L60;
  - **1 token `<origin>`**: parita' esatta 1/1, nello stesso punto (unita' 11);
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **25 tab**, **38 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **2 gruppi di duplicati inglesi** (18/24, 20/26), resa identica asserita.''',
    '''r"""verify.py — L62 (data/human/culture conversations.txt, 30 unita', righe 566-611)

**Segmento interno**: 142 unita' prima (L58–L61), **202 dopo** la 611, file di 374, `max(line) = 1122`.
La finestra di export era 555-611 ma la prima unita' sta sulla **566**: si asserisce il valore misurato
(decisione 196). La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L61, tutte asserite:
  - **`NT` positivo: 3 `UI_LABEL`** (4 `overheard scientists 1`, 15 `… 2`, 26 `… 3`), identiche al sorgente;
  - **0 token** `<…>`: assenza dichiarata, dopo l'unico `<origin>` di L61;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **26 tab**, **36 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **0 gruppi di duplicati inglesi**: controllo negativo dichiarato.''')

rep("""  5. collocazione: 26 unita', righe 511-552
  6. segmento interno: 116 prima, 232 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [511, 552] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 26 `MISSION_TEXT`""",
    """  5. collocazione: 30 unita', righe 566-611
  6. segmento interno: 142 prima, 202 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [566, 611] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 27 `MISSION_TEXT` + 3 `UI_LABEL`""")

rep("""  9. `NT` vuoto; assenze dichiarate per `DIALOG`, `LOGBOOK`, `CONVERSATION`, `TEXT`, quadre, backtick
 10. 25 tab e 38 virgolette""",
    """  9. `NT` positivo su 4, 15, 26; assenze dichiarate per `DIALOG`, `LOGBOOK`, `CONVERSATION`, `TEXT`,
     token, quadre, backtick
 10. 26 tab e 36 virgolette""")

rep(" 14. duplicati inglesi: 2 gruppi, resa identica; nessuna resa ripetuta fra inglesi diversi",
    " 14. duplicati inglesi: **nessun gruppo** (controllo negativo) e nessuna resa ripetuta")

rep("NT = set()", "NT = set([4, 15, 26])")

rep("   len(tu) == 26 and (first, last) == (511, 552), (len(tu), first, last))",
    "   len(tu) == 30 and (first, last) == (566, 611), (len(tu), first, last))")

rep("""ck('segmento interno: 116 prima, 232 dopo, 374 totali',
   before == 116 and after == 232 and tot == 374, (before, after, tot))""",
    """ck('segmento interno: 142 prima, 202 dopo, 374 totali',
   before == 142 and after == 202 and tot == 374, (before, after, tot))""")

rep("""ck('copertura del segmento: righe 511-552 continue',
   lrows[0] == 511 and lrows[-1] == 552)""",
    """ck('copertura del segmento: righe 566-611 continue',
   lrows[0] == 566 and lrows[-1] == 611)""")

rep("ck('nessun altra unita nel DB dentro 511-552 (%d)' % inrange, inrange == len(tu), inrange)",
    "ck('nessun altra unita nel DB dentro 566-611 (%d)' % inrange, inrange == len(tu), inrange)")

rep("""ck('distribuzione dei kind: 26 MISSION_TEXT', dict(kinds) == {'MISSION_TEXT': 26}, dict(kinds))""",
    """ck('distribuzione dei kind: 27 MISSION_TEXT + 3 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 27, 'UI_LABEL': 3}, dict(kinds))""")

rep("""ck('UI_LABEL: nessuna nel segmento (assenza dichiarata)', ui == [] and NT == set(), ui)""",
    """ck('UI_LABEL: 3 attese, tutte elencate', ui == sorted(NT) == [4, 15, 26], ui)
notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('NT: le 3 label identiche al sorgente', not notid, notid)""")

rep("""ck('token <...>: 1 nel sorgente e 1 in italiano', tok_en == 1 and tok_it == 1, (tok_en, tok_it))""",
    """ck('token <...>: 0 nel sorgente e 0 in italiano (assenza dichiarata)',
   tok_en == 0 and tok_it == 0, (tok_en, tok_it))""")

rep("ck('tab e virgolette: parita per unita (26 unita)', per_unit == [], per_unit[:10])",
    "ck('tab e virgolette: parita per unita (30 unita)', per_unit == [], per_unit[:10])")

rep("ck('tab iniziale presente dove il sorgente lo ha (25)', ntab == 25 and lead == [], (ntab, lead[:5]))",
    "ck('tab iniziale presente dove il sorgente lo ha (26)', ntab == 26 and lead == [], (ntab, lead[:5]))")

rep("""(('\\t', 'tab', 25), ('"', 'virgolette', 38))""",
    """(('\\t', 'tab', 26), ('"', 'virgolette', 36))""")

rep("""ck('duplicati inglesi (2 gruppi, 4 unita): resa italiana identica',
   len(dup_en) == 2 and dup_ok, (len(dup_en), dup_ok))""",
    """ck('duplicati inglesi: nessun gruppo (controllo negativo)', len(dup_en) == 0 and dup_ok,
   (len(dup_en), dup_ok))""")

rep("'verify L61 superato' if not fail else 'verify L61 fallito'",
    "'verify L62 superato' if not fail else 'verify L62 fallito'")

open(p, 'w', encoding='utf-8').write(s)
print('verify.py adattato a L62')
