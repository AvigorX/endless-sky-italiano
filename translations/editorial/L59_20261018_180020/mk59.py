# -*- coding: utf-8 -*-
"""Adatta il verify.py di L58 a L59 (segmento interno, 42 unita', righe 225-423)."""
p = 'verify.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep('''r"""verify.py — L58 (data/human/culture conversations.txt, 43 unita', righe 25-209)

**Apre il file** (0 unita' prima della 25) e **non lo chiude**: **331 unita' dopo** la 209, file di 374,
`max(line) = 1122`. La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L57, tutte asserite:
  - **`NT` vuoto**: 0 `UI_LABEL` (assenza dichiarata, non insieme ereditato);
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **0 token** `<…>`: parita' 0/0 asserita su ogni unita';
  - **34 tab**, **8 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - tipi: 43 `MISSION_TEXT` e nient'altro;
  - 3 gruppi di duplicati inglesi (6 unita': 1/3, 2/4, 21/24).''',
    '''r"""verify.py — L59 (data/human/culture conversations.txt, 42 unita', righe 225-423)

**Segmento interno**: 43 unita' prima (L58), **289 dopo** la 423, file di 374, `max(line) = 1122`.
La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L58, tutte asserite:
  - tipi: 42 `MISSION_TEXT` e nient'altro;
  - **`NT` vuoto**, **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **0 token** `<…>`: parita' 0/0 asserita su ogni unita';
  - **32 tab**, **34 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **0 gruppi di duplicati inglesi**: controllo negativo dichiarato.''')

rep("""  5. collocazione: 43 unita', righe 25-209
  6. apre il file: 0 prima, 331 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [25, 209] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 43 `MISSION_TEXT`""",
    """  5. collocazione: 42 unita', righe 225-423
  6. segmento interno: 43 prima, 289 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [225, 423] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 42 `MISSION_TEXT`""")

rep(" 10. 34 tab e 8 virgolette", " 10. 32 tab e 34 virgolette")
rep(" 14. duplicati inglesi: resa italiana identica; nessuna resa ripetuta fra inglesi diversi",
    " 14. duplicati inglesi: **nessun gruppo** (controllo negativo) e nessuna resa ripetuta")

rep("   len(tu) == 43 and (first, last) == (25, 209), (len(tu), first, last))",
    "   len(tu) == 42 and (first, last) == (225, 423), (len(tu), first, last))")

rep("""ck('apre il file: 0 prima della 25, 331 dopo la 209',
   before == 0 and after == 331 and tot == 374, (before, after, tot))""",
    """ck('segmento interno: 43 prima, 289 dopo, 374 totali',
   before == 43 and after == 289 and tot == 374, (before, after, tot))""")

rep("""ck('copertura del segmento: righe 25-209 continue',
   lrows[0] == 25 and lrows[-1] == 209)""",
    """ck('copertura del segmento: righe 225-423 continue',
   lrows[0] == 225 and lrows[-1] == 423)""")

rep("ck('nessun altra unita nel DB dentro 25-209 (%d)' % inrange, inrange == len(tu), inrange)",
    "ck('nessun altra unita nel DB dentro 225-423 (%d)' % inrange, inrange == len(tu), inrange)")

rep("ck('distribuzione dei kind: 43 MISSION_TEXT', dict(kinds) == {'MISSION_TEXT': 43}, dict(kinds))",
    "ck('distribuzione dei kind: 42 MISSION_TEXT', dict(kinds) == {'MISSION_TEXT': 42}, dict(kinds))")

rep("""(('\\t', 'tab', 34), ('"', 'virgolette', 8))""",
    """(('\\t', 'tab', 32), ('"', 'virgolette', 34))""")

rep("ck('tab e virgolette: parita per unita (43 unita)', per_unit == [], per_unit[:10])",
    "ck('tab e virgolette: parita per unita (42 unita)', per_unit == [], per_unit[:10])")

rep("ck('tab iniziale presente dove il sorgente lo ha (34)', ntab == 34 and lead == [], (ntab, lead[:5]))",
    "ck('tab iniziale presente dove il sorgente lo ha (32)', ntab == 32 and lead == [], (ntab, lead[:5]))")

rep("""ck('duplicati inglesi (3 gruppi, 6 unita): resa italiana identica',
   len(dup_en) == 3 and dup_ok, (len(dup_en), dup_ok))""",
    """ck('duplicati inglesi: nessun gruppo (controllo negativo)', len(dup_en) == 0 and dup_ok,
   (len(dup_en), dup_ok))""")

rep("'verify L58 superato' if not fail else 'verify L58 fallito'",
    "'verify L59 superato' if not fail else 'verify L59 fallito'")

open(p, 'w', encoding='utf-8').write(s)
print('verify.py adattato a L59')
