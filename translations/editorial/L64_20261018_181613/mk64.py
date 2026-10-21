# -*- coding: utf-8 -*-
"""Adatta il verify.py di L63 a L64 (42 unita', righe 723-810, NT {15,18,22,24}, dispari 35-37)."""
p = 'verify.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep('''r"""verify.py — L63 (data/human/culture conversations.txt, 37 unita', righe 624-711)

**Segmento interno**: 172 unita' prima (L58–L62), **165 dopo** la 711, file di 374, `max(line) = 1122`.
La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L62, tutte asserite:
  - **`NT` positivo: 1 `UI_LABEL`** (30 `way in`);
  - **0 token** `<…>`: assenza dichiarata;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **35 tab**, **51 virgolette**, **3 dispari** (18, 29, 31): si **riproducono**, non si chiudono;
  - **0 gruppi di duplicati inglesi**: controllo negativo dichiarato.''',
    '''r"""verify.py — L64 (data/human/culture conversations.txt, 42 unita', righe 723-810)

**Segmento interno**: 209 unita' prima (L58–L63), **123 dopo** la 810, file di 374, `max(line) = 1122`.
La finestra di export era 712-810 ma la prima unita' sta sulla **723**: si asserisce il valore misurato
(decisione 196). La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L63, tutte asserite:
  - **`NT` positivo: 4 `UI_LABEL`** (15 `no credits`, 18 `leave tent`, 22 `after tent`, 24 `end`);
  - **0 token** `<…>`: assenza dichiarata;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **36 tab**, **23 virgolette**, **3 dispari** (35, 36, 37): tre discorsi aperti e non chiusi, riprodotti;
  - **0 gruppi di duplicati inglesi**: controllo negativo dichiarato.''')

rep("""  5. collocazione: 37 unita', righe 624-711
  6. segmento interno: 172 prima, 165 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [624, 711] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 36 `MISSION_TEXT` + 1 `UI_LABEL`""",
    """  5. collocazione: 42 unita', righe 723-810
  6. segmento interno: 209 prima, 123 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [723, 810] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 38 `MISSION_TEXT` + 4 `UI_LABEL`""")

rep(""" 10. 35 tab e 51 virgolette, **3 dispari riprodotte** (18, 29, 31)""",
    """ 10. 36 tab e 23 virgolette, **3 dispari riprodotte** (35, 36, 37)""")

rep("NT = set([30])", "NT = set([15, 18, 22, 24])")

rep("   len(tu) == 37 and (first, last) == (624, 711), (len(tu), first, last))",
    "   len(tu) == 42 and (first, last) == (723, 810), (len(tu), first, last))")

rep("""ck('segmento interno: 172 prima, 165 dopo, 374 totali',
   before == 172 and after == 165 and tot == 374, (before, after, tot))""",
    """ck('segmento interno: 209 prima, 123 dopo, 374 totali',
   before == 209 and after == 123 and tot == 374, (before, after, tot))""")

rep("""ck('copertura del segmento: righe 624-711 continue',
   lrows[0] == 624 and lrows[-1] == 711)""",
    """ck('copertura del segmento: righe 723-810 continue',
   lrows[0] == 723 and lrows[-1] == 810)""")

rep("ck('nessun altra unita nel DB dentro 624-711 (%d)' % inrange, inrange == len(tu), inrange)",
    "ck('nessun altra unita nel DB dentro 723-810 (%d)' % inrange, inrange == len(tu), inrange)")

rep("""ck('distribuzione dei kind: 36 MISSION_TEXT + 1 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 36, 'UI_LABEL': 1}, dict(kinds))""",
    """ck('distribuzione dei kind: 38 MISSION_TEXT + 4 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 38, 'UI_LABEL': 4}, dict(kinds))""")

rep("""ck('UI_LABEL: 1 attesa, elencata', ui == sorted(NT) == [30], ui)
notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('NT: la label identica al sorgente', not notid, notid)""",
    """ck('UI_LABEL: 4 attese, tutte elencate', ui == sorted(NT) == [15, 18, 22, 24], ui)
notid = [i for i in NT if by_idx[i]['italian'] != by_idx[i]['english']]
ck('NT: le 4 label identiche al sorgente', not notid, notid)""")

rep("ck('tab e virgolette: parita per unita (37 unita)', per_unit == [], per_unit[:10])",
    "ck('tab e virgolette: parita per unita (42 unita)', per_unit == [], per_unit[:10])")

rep("ck('tab iniziale presente dove il sorgente lo ha (35)', ntab == 35 and lead == [], (ntab, lead[:5]))",
    "ck('tab iniziale presente dove il sorgente lo ha (36)', ntab == 36 and lead == [], (ntab, lead[:5]))")

rep("""(('\\t', 'tab', 35), ('"', 'virgolette', 51))""",
    """(('\\t', 'tab', 36), ('"', 'virgolette', 23))""")

rep("""ck('virgolette dispari: 3 unita (18, 29, 31) riprodotte, non chiuse',
   odd_en == (18, 29, 31) and odd_it == (18, 29, 31), (odd_en, odd_it))""",
    """ck('virgolette dispari: 3 unita (35, 36, 37) riprodotte, non chiuse',
   odd_en == (35, 36, 37) and odd_it == (35, 36, 37), (odd_en, odd_it))""")

rep("'verify L63 superato' if not fail else 'verify L63 fallito'",
    "'verify L64 superato' if not fail else 'verify L64 fallito'")

open(p, 'w', encoding='utf-8').write(s)
print('verify.py adattato a L64')
