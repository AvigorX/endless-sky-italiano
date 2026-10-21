# -*- coding: utf-8 -*-
"""Adatta il verify.py di L59 a L60 (31 unita', righe 437-495, NT positivo su 6 e 20)."""
p = 'verify.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep('''r"""verify.py — L59 (data/human/culture conversations.txt, 42 unita', righe 225-423)

**Segmento interno**: 43 unita' prima (L58), **289 dopo** la 423, file di 374, `max(line) = 1122`.
La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L58, tutte asserite:
  - tipi: 42 `MISSION_TEXT` e nient'altro;
  - **`NT` vuoto**, **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **0 token** `<…>`: parita' 0/0 asserita su ogni unita';
  - **32 tab**, **34 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **0 gruppi di duplicati inglesi**: controllo negativo dichiarato.''',
    '''r"""verify.py — L60 (data/human/culture conversations.txt, 31 unita', righe 437-495)

**Segmento interno**: 85 unita' prima (L58+L59), **258 dopo** la 495, file di 374, `max(line) = 1122`.
La finestra di export era 429-495 ma la prima unita' sta sulla **437**: si asserisce il valore **misurato**
(decisione 196). La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L59, tutte asserite:
  - **`NT` positivo: 2 `UI_LABEL`** (6 `pass by`, 20 `get out`), identiche al sorgente;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **0 token** `<…>`: parita' 0/0 asserita su ogni unita';
  - **27 tab**, **40 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **0 gruppi di duplicati inglesi**: controllo negativo dichiarato.''')

rep("""  5. collocazione: 42 unita', righe 225-423
  6. segmento interno: 43 prima, 289 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [225, 423] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 42 `MISSION_TEXT`""",
    """  5. collocazione: 31 unita', righe 437-495
  6. segmento interno: 85 prima, 258 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [437, 495] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 29 `MISSION_TEXT` + 2 `UI_LABEL`""")

rep("  9. assenze dichiarate: `NT`, `DIALOG`, `LOGBOOK`, `CONVERSATION`, `TEXT`, token, quadre, backtick\n 10. 32 tab e 34 virgolette",
    "  9. `NT` positivo su 6 e 20; assenze dichiarate per `DIALOG`, `LOGBOOK`, `CONVERSATION`, `TEXT`, token,\n     quadre, backtick\n 10. 27 tab e 40 virgolette")

rep("   len(tu) == 42 and (first, last) == (225, 423), (len(tu), first, last))",
    "   len(tu) == 31 and (first, last) == (437, 495), (len(tu), first, last))")

rep("""ck('segmento interno: 43 prima, 289 dopo, 374 totali',
   before == 43 and after == 289 and tot == 374, (before, after, tot))""",
    """ck('segmento interno: 85 prima, 258 dopo, 374 totali',
   before == 85 and after == 258 and tot == 374, (before, after, tot))""")

rep("""ck('copertura del segmento: righe 225-423 continue',
   lrows[0] == 225 and lrows[-1] == 423)""",
    """ck('copertura del segmento: righe 437-495 continue',
   lrows[0] == 437 and lrows[-1] == 495)""")

rep("ck('nessun altra unita nel DB dentro 225-423 (%d)' % inrange, inrange == len(tu), inrange)",
    "ck('nessun altra unita nel DB dentro 437-495 (%d)' % inrange, inrange == len(tu), inrange)")

rep("ck('distribuzione dei kind: 42 MISSION_TEXT', dict(kinds) == {'MISSION_TEXT': 42}, dict(kinds))",
    "ck('distribuzione dei kind: 29 MISSION_TEXT + 2 UI_LABEL',\n   dict(kinds) == {'MISSION_TEXT': 29, 'UI_LABEL': 2}, dict(kinds))")

rep("ck('UI_LABEL: nessuna nel segmento (assenza dichiarata)', ui == [] and NT == set(), ui)",
    "ck('UI_LABEL: 2 attese, tutte elencate', ui == sorted(NT) == [6, 20], ui)\n"
    "notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]\n"
    "ck('NT: le 2 label identiche al sorgente', not notid, notid)")

rep("ck('tab e virgolette: parita per unita (42 unita)', per_unit == [], per_unit[:10])",
    "ck('tab e virgolette: parita per unita (31 unita)', per_unit == [], per_unit[:10])")

rep("ck('tab iniziale presente dove il sorgente lo ha (32)', ntab == 32 and lead == [], (ntab, lead[:5]))",
    "ck('tab iniziale presente dove il sorgente lo ha (27)', ntab == 27 and lead == [], (ntab, lead[:5]))")

rep("""(('\\t', 'tab', 32), ('"', 'virgolette', 34))""",
    """(('\\t', 'tab', 27), ('"', 'virgolette', 40))""")

rep("'verify L59 superato' if not fail else 'verify L59 fallito'",
    "'verify L60 superato' if not fail else 'verify L60 fallito'")

open(p, 'w', encoding='utf-8').write(s)
print('verify.py adattato a L60')
