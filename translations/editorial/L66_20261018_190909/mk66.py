# -*- coding: utf-8 -*-
"""Adatta il verify.py di L65 a L66 (45 unita', righe 930-1053, NT vuoto, dispari 10/34, 1 dup)."""
p = 'verify.py'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep('''r"""verify.py — L65 (data/human/culture conversations.txt, 43 unita', righe 819-920)

**Segmento interno**: 251 unita' prima (L58–L64), **80 dopo** la 920, file di 374, `max(line) = 1122`.
La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L64, tutte asserite:
  - **`NT` positivo: 4 `UI_LABEL`** (10 `war ongoing`, 12 `war over`, 14 `zenith bombed`,
    16 `sestor beaten at farpoint`);
  - **2 token diversi**: `<origin>` (7) e `<ship>` (21), parita' 2/2 simbolo per simbolo;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **45 tab**, **22 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **1 gruppo di duplicati inglesi** (26/30, `"No thanks."`), resa identica.''',
    '''r"""verify.py — L66 (data/human/culture conversations.txt, 45 unita', righe 930-1053)

**Segmento interno**: 294 unita' prima (L58–L65), **35 dopo** la 1053, file di 374, `max(line) = 1122`.
La finestra di export era 921-1053 ma la prima unita' sta sulla **930**: si asserisce il valore misurato
(decisione 196). La copertura del file NON e' un invariante qui (decisione 158).

Differenze rispetto a L65, tutte asserite:
  - **`NT` vuoto**: assenza dichiarata, dopo i 4 `UI_LABEL` di L64 e L65;
  - **0 token** `<…>`: assenza dichiarata;
  - **`DIALOG` 0**, **`LOGBOOK` 0**, **`CONVERSATION` 0`, **`TEXT` 0**: assenze dichiarate;
  - **41 tab**, **52 virgolette**, **2 dispari** (10, 34): due discorsi aperti e non chiusi, riprodotti;
  - **1 gruppo di duplicati inglesi** (2 unita'), resa identica.''')

rep("""  5. collocazione: 43 unita', righe 819-920
  6. segmento interno: 251 prima, 80 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [819, 920] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 39 `MISSION_TEXT` + 4 `UI_LABEL`""",
    """  5. collocazione: 45 unita', righe 930-1053
  6. segmento interno: 294 prima, 35 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [930, 1053] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 45 `MISSION_TEXT`""")

rep(" 10. 45 tab e 22 virgolette, **0 dispari**; 2 token distinti con parita' per simbolo",
    " 10. 41 tab e 52 virgolette, **2 dispari riprodotte** (10, 34); 0 token")
rep(" 14. duplicati inglesi: 1 gruppo (26/30), resa identica; nessuna resa ripetuta fra diversi",
    " 14. duplicati inglesi: 1 gruppo, resa identica; nessuna resa ripetuta fra inglesi diversi")

rep("NT = set([10, 12, 14, 16])", "NT = set()")

rep("   len(tu) == 43 and (first, last) == (819, 920), (len(tu), first, last))",
    "   len(tu) == 45 and (first, last) == (930, 1053), (len(tu), first, last))")

rep("""ck('segmento interno: 251 prima, 80 dopo, 374 totali',
   before == 251 and after == 80 and tot == 374, (before, after, tot))""",
    """ck('segmento interno: 294 prima, 35 dopo, 374 totali',
   before == 294 and after == 35 and tot == 374, (before, after, tot))""")

rep("""ck('copertura del segmento: righe 819-920 continue',
   lrows[0] == 819 and lrows[-1] == 920)""",
    """ck('copertura del segmento: righe 930-1053 continue',
   lrows[0] == 930 and lrows[-1] == 1053)""")

rep("ck('nessun altra unita nel DB dentro 819-920 (%d)' % inrange, inrange == len(tu), inrange)",
    "ck('nessun altra unita nel DB dentro 930-1053 (%d)' % inrange, inrange == len(tu), inrange)")

rep("""ck('distribuzione dei kind: 39 MISSION_TEXT + 4 UI_LABEL',
   dict(kinds) == {'MISSION_TEXT': 39, 'UI_LABEL': 4}, dict(kinds))""",
    """ck('distribuzione dei kind: 45 MISSION_TEXT', dict(kinds) == {'MISSION_TEXT': 45}, dict(kinds))""")

rep("""ck('UI_LABEL: 4 attese, tutte elencate', ui == sorted(NT) == [10, 12, 14, 16], ui)""",
    """ck('UI_LABEL: nessuna nel segmento (assenza dichiarata)', ui == [] and NT == set(), ui)""")

rep("""fam_en = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
fam_it = collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))
ck('token <...>: 2 in inglese e 2 in italiano, stesse famiglie (%s)' % dict(fam_en),
   tok_en == 2 and tok_it == 2 and fam_en == fam_it, (tok_en, tok_it, dict(fam_en), dict(fam_it)))""",
    """ck('token <...>: 0 nel sorgente e 0 in italiano (assenza dichiarata)',
   tok_en == 0 and tok_it == 0, (tok_en, tok_it))""")

rep("ck('tab e virgolette: parita per unita (43 unita)', per_unit == [], per_unit[:10])",
    "ck('tab e virgolette: parita per unita (45 unita)', per_unit == [], per_unit[:10])")

rep("ck('tab iniziale presente dove il sorgente lo ha (35)', ntab == 35 and lead == [], (ntab, lead[:5]))",
    "ck('tab iniziale presente dove il sorgente lo ha (40)', ntab == 40 and lead == [], (ntab, lead[:5]))")

rep("""(('\\t', 'tab', 45), ('"', 'virgolette', 22))""",
    """(('\\t', 'tab', 41), ('"', 'virgolette', 52))""")

rep("""ck('virgolette dispari: nessuna nel lotto (assenza dichiarata)', odd_en == () and odd_it == (),
   (odd_en, odd_it))""",
    """ck('virgolette dispari: 2 unita (10, 34) riprodotte, non chiuse',
   odd_en == (10, 34) and odd_it == (10, 34), (odd_en, odd_it))""")

rep("'verify L65 superato' if not fail else 'verify L65 fallito'",
    "'verify L66 superato' if not fail else 'verify L66 fallito'")

open(p, 'w', encoding='utf-8').write(s)
print('verify.py adattato a L66')
