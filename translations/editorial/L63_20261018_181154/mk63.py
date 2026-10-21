# -*- coding: utf-8 -*-
"""Adatta il verify.py di L62 a L63 (37 unita', righe 624-711, NT {30}, 3 virgolette dispari)."""
p = 'verify.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep('''r"""verify.py — L62 (data/human/culture conversations.txt, 30 unita', righe 566-611)

**Segmento interno**: 142 unita' prima (L58–L61), **202 dopo** la 611, file di 374, `max(line) = 1122`.
La finestra di export era 555-611 ma la prima unita' sta sulla **566**: si asserisce il valore misurato
(decisione 196). La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L61, tutte asserite:
  - **`NT` positivo: 3 `UI_LABEL`** (4 `overheard scientists 1`, 15 `… 2`, 26 `… 3`), identiche al sorgente;
  - **0 token** `<…>`: assenza dichiarata, dopo l'unico `<origin>` di L61;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **26 tab**, **36 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **0 gruppi di duplicati inglesi**: controllo negativo dichiarato.''',
    '''r"""verify.py — L63 (data/human/culture conversations.txt, 37 unita', righe 624-711)

**Segmento interno**: 172 unita' prima (L58–L62), **165 dopo** la 711, file di 374, `max(line) = 1122`.
La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L62, tutte asserite:
  - **`NT` positivo: 1 `UI_LABEL`** (30 `way in`);
  - **0 token** `<…>`: assenza dichiarata;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **35 tab**, **51 virgolette**, **3 dispari** (18, 29, 31): si **riproducono**, non si chiudono;
  - **0 gruppi di duplicati inglesi**: controllo negativo dichiarato.''')

rep("""  5. collocazione: 30 unita', righe 566-611
  6. segmento interno: 142 prima, 202 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [566, 611] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 27 `MISSION_TEXT` + 3 `UI_LABEL`""",
    """  5. collocazione: 37 unita', righe 624-711
  6. segmento interno: 172 prima, 165 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [624, 711] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 36 `MISSION_TEXT` + 1 `UI_LABEL`""")

rep(""" 10. 26 tab e 36 virgolette""", """ 10. 35 tab e 51 virgolette, **3 dispari riprodotte** (18, 29, 31)""")

rep("NT = set([4, 15, 26])", "NT = set([30])")

rep("   len(tu) == 30 and (first, last) == (566, 611), (len(tu), first, last))",
    "   len(tu) == 37 and (first, last) == (624, 711), (len(tu), first, last))")

rep("""ck('segmento interno: 142 prima, 202 dopo, 374 totali',
   before == 142 and after == 202 and tot == 374, (before, after, tot))""",
    """ck('segmento interno: 172 prima, 165 dopo, 374 totali',
   before == 172 and after == 165 and tot == 374, (before, after, tot))""")

rep("""ck('copertura del segmento: righe 566-611 continue',
   lrows[0] == 566 and lrows[-1] == 611)""",
    """ck('copertura del segmento: righe 624-711 continue',
   lrows[0] == 624 and lrows[-1] == 711)""")

rep("ck('nessun altra unita nel DB dentro 566-611 (%d)' % inrange, inrange == len(tu), inrange)",
    "ck('nessun altra unita nel DB dentro 624-711 (%d)' % inrange, inrange == len(tu), inrange)")

rep("""ck('distribuzione dei kind: 27 MISSION_TEXT + 3 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 27, 'UI_LABEL': 3}, dict(kinds))""",
    """ck('distribuzione dei kind: 36 MISSION_TEXT + 1 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 36, 'UI_LABEL': 1}, dict(kinds))""")

rep("""ck('UI_LABEL: 3 attese, tutte elencate', ui == sorted(NT) == [4, 15, 26], ui)
notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('NT: le 3 label identiche al sorgente', not notid, notid)""",
    """ck('UI_LABEL: 1 attesa, elencata', ui == sorted(NT) == [30], ui)
notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('NT: la label identica al sorgente', not notid, notid)""")

rep("ck('tab e virgolette: parita per unita (30 unita)', per_unit == [], per_unit[:10])",
    "ck('tab e virgolette: parita per unita (37 unita)', per_unit == [], per_unit[:10])")

rep("ck('tab iniziale presente dove il sorgente lo ha (26)', ntab == 26 and lead == [], (ntab, lead[:5]))",
    "ck('tab iniziale presente dove il sorgente lo ha (35)', ntab == 35 and lead == [], (ntab, lead[:5]))")

rep("""(('\\t', 'tab', 26), ('"', 'virgolette', 36))""",
    """(('\\t', 'tab', 35), ('"', 'virgolette', 51))""")

rep("""ck('virgolette dispari: nessuna nel lotto (assenza dichiarata)', odd_en == () and odd_it == (),
   (odd_en, odd_it))""",
    """ck('virgolette dispari: 3 unita (18, 29, 31) riprodotte, non chiuse',
   odd_en == (18, 29, 31) and odd_it == (18, 29, 31), (odd_en, odd_it))""")

rep("'verify L62 superato' if not fail else 'verify L62 fallito'",
    "'verify L63 superato' if not fail else 'verify L63 fallito'")

open(p, 'w', encoding='utf-8').write(s)
print('verify.py adattato a L63')
