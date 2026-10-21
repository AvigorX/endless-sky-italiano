# -*- coding: utf-8 -*-
"""Adatta il verify.py di L64 a L65 (43 unita', righe 819-920, NT {10,12,14,16}, 2 token, 0 dispari)."""
p = 'verify.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep('''r"""verify.py — L64 (data/human/culture conversations.txt, 42 unita', righe 723-810)

**Segmento interno**: 209 unita' prima (L58–L63), **123 dopo** la 810, file di 374, `max(line) = 1122`.
La finestra di export era 712-810 ma la prima unita' sta sulla **723**: si asserisce il valore misurato
(decisione 196). La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L63, tutte asserite:
  - **`NT` positivo: 4 `UI_LABEL`** (15 `no credits`, 18 `leave tent`, 22 `after tent`, 24 `end`);
  - **0 token** `<…>`: assenza dichiarata;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **36 tab**, **23 virgolette**, **3 dispari** (35, 36, 37): tre discorsi aperti e non chiusi, riprodotti;
  - **0 gruppi di duplicati inglesi**: controllo negativo dichiarato.''',
    '''r"""verify.py — L65 (data/human/culture conversations.txt, 43 unita', righe 819-920)

**Segmento interno**: 251 unita' prima (L58–L64), **80 dopo** la 920, file di 374, `max(line) = 1122`.
La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L64, tutte asserite:
  - **`NT` positivo: 4 `UI_LABEL`** (10 `war ongoing`, 12 `war over`, 14 `zenith bombed`,
    16 `sestor beaten at farpoint`);
  - **2 token diversi**: `<origin>` (7) e `<ship>` (21), parita' 2/2 simbolo per simbolo;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **45 tab**, **22 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **1 gruppo di duplicati inglesi** (26/30, `"No thanks."`), resa identica.''')

rep("""  5. collocazione: 42 unita', righe 723-810
  6. segmento interno: 209 prima, 123 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [723, 810] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 38 `MISSION_TEXT` + 4 `UI_LABEL`""",
    """  5. collocazione: 43 unita', righe 819-920
  6. segmento interno: 251 prima, 80 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [819, 920] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 39 `MISSION_TEXT` + 4 `UI_LABEL`""")

rep(" 10. 36 tab e 23 virgolette, **3 dispari riprodotte** (35, 36, 37)",
    " 10. 45 tab e 22 virgolette, **0 dispari**; 2 token distinti con parita' per simbolo")
rep(" 14. duplicati inglesi: **nessun gruppo** (controllo negativo) e nessuna resa ripetuta",
    " 14. duplicati inglesi: 1 gruppo (26/30), resa identica; nessuna resa ripetuta fra diversi")

rep("NT = set([15, 18, 22, 24])", "NT = set([10, 12, 14, 16])")

rep("   len(tu) == 42 and (first, last) == (723, 810), (len(tu), first, last))",
    "   len(tu) == 43 and (first, last) == (819, 920), (len(tu), first, last))")

rep("""ck('segmento interno: 209 prima, 123 dopo, 374 totali',
   before == 209 and after == 123 and tot == 374, (before, after, tot))""",
    """ck('segmento interno: 251 prima, 80 dopo, 374 totali',
   before == 251 and after == 80 and tot == 374, (before, after, tot))""")

rep("""ck('copertura del segmento: righe 723-810 continue',
   lrows[0] == 723 and lrows[-1] == 810)""",
    """ck('copertura del segmento: righe 819-920 continue',
   lrows[0] == 819 and lrows[-1] == 920)""")

rep("ck('nessun altra unita nel DB dentro 723-810 (%d)' % inrange, inrange == len(tu), inrange)",
    "ck('nessun altra unita nel DB dentro 819-920 (%d)' % inrange, inrange == len(tu), inrange)")

rep("""ck('distribuzione dei kind: 38 MISSION_TEXT + 4 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 38, 'UI_LABEL': 4}, dict(kinds))""",
    """ck('distribuzione dei kind: 39 MISSION_TEXT + 4 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 39, 'UI_LABEL': 4}, dict(kinds))""")

rep("""ck('UI_LABEL: 4 attese, tutte elencate', ui == sorted(NT) == [15, 18, 22, 24], ui)""",
    """ck('UI_LABEL: 4 attese, tutte elencate', ui == sorted(NT) == [10, 12, 14, 16], ui)""")

rep("""ck('token <...>: 0 nel sorgente e 0 in italiano (assenza dichiarata)',
   tok_en == 0 and tok_it == 0, (tok_en, tok_it))""",
    """fam_en = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
fam_it = collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))
ck('token <...>: 2 in inglese e 2 in italiano, stesse famiglie (%s)' % dict(fam_en),
   tok_en == 2 and tok_it == 2 and fam_en == fam_it, (tok_en, tok_it, dict(fam_en), dict(fam_it)))""")

rep("ck('tab e virgolette: parita per unita (42 unita)', per_unit == [], per_unit[:10])",
    "ck('tab e virgolette: parita per unita (43 unita)', per_unit == [], per_unit[:10])")

rep("ck('tab iniziale presente dove il sorgente lo ha (36)', ntab == 36 and lead == [], (ntab, lead[:5]))",
    "ck('tab iniziale presente dove il sorgente lo ha (35)', ntab == 35 and lead == [], (ntab, lead[:5]))")

rep("""(('\\t', 'tab', 36), ('"', 'virgolette', 23))""",
    """(('\\t', 'tab', 45), ('"', 'virgolette', 22))""")

rep("""ck('virgolette dispari: 3 unita (35, 36, 37) riprodotte, non chiuse',
   odd_en == (35, 36, 37) and odd_it == (35, 36, 37), (odd_en, odd_it))""",
    """ck('virgolette dispari: nessuna nel lotto (assenza dichiarata)', odd_en == () and odd_it == (),
   (odd_en, odd_it))""")

rep("""ck('duplicati inglesi: nessun gruppo (controllo negativo)', len(dup_en) == 0 and dup_ok,
   (len(dup_en), dup_ok))""",
    """ck('duplicati inglesi (1 gruppo, 2 unita): resa italiana identica',
   len(dup_en) == 1 and dup_ok, (len(dup_en), dup_ok))""")

rep("'verify L64 superato' if not fail else 'verify L64 fallito'",
    "'verify L65 superato' if not fail else 'verify L65 fallito'")

open(p, 'w', encoding='utf-8').write(s)
print('verify.py adattato a L65')
