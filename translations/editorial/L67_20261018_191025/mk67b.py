# -*- coding: utf-8 -*-
"""Adatta il verify.py di L66 a L67 (35 unita', righe 1062-1122, CHIUDE il file: 374/374).

Sostituisce l'intero docstring per non dipendere dalla punteggiatura esatta, poi applica le modifiche.
"""
p = 'verify.py'
s = open(p, encoding='utf-8').read()

end = s.index('"""', 3) + 3
new_doc = '''r"""verify.py — L67 (data/human/culture conversations.txt, 35 unita', righe 1062-1122)

**Chiude il file**: L58–L66 (339 unita') + L67 (35) = **374/374**, `max(line) = 1122`, 0 unita' dopo la
1122. Qui l'invariante «di file» torna legittimo (decisione 181) ed e' asserito **insieme**: chiusura,
`max(line)` e copertura 374/374.

Differenze rispetto a L66, tutte asserite:
  - **`LOGBOOK` 1** (unita' 1, riga 1062): unico diario del file, controllo **positivo**;
  - **`NT` vuoto**, **`DIALOG` 0**, **`CONVERSATION` 0**, **`TEXT` 0**: assenze dichiarate;
  - **2 token** `<ship>` (unita' 2 e 17): parita' 2/2, stesso simbolo;
  - **32 tab**, **68 virgolette**, **0 dispari**, **0 quadre**, **0 backtick**;
  - **0 gruppi di duplicati inglesi**: controllo negativo dichiarato.
"""'''
s = new_doc + s[end:]


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b)


rep("""  5. collocazione: 45 unita', righe 930-1053
  6. segmento interno: 294 prima, 35 dopo, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [930, 1053] senza buchi, nessuna unita' del DB fuori da quelle
  8. distribuzione dei kind misurata: 45 `MISSION_TEXT`""",
    """  5. collocazione: 35 unita', righe 1062-1122
  6. chiude il file: 339 prima, **0 dopo**, 374 totali, `max(line) = 1122`
  7. copertura del segmento: righe [1062, 1122] continue; copertura del file 374/374
  8. distribuzione dei kind misurata: 34 `MISSION_TEXT` + 1 `LOGBOOK`""")

rep(" 10. 41 tab e 52 virgolette, **2 dispari riprodotte** (10, 34); 0 token",
    " 10. 32 tab e 68 virgolette, **0 dispari**; 2 token `<ship>` con parita' 2/2")
rep(" 14. duplicati inglesi: 1 gruppo, resa identica; nessuna resa ripetuta fra inglesi diversi",
    " 14. duplicati inglesi: **nessun gruppo** (controllo negativo) e nessuna resa ripetuta")

rep("NT = set()", "NT = set()\nLOG = {1}")

rep("   len(tu) == 45 and (first, last) == (930, 1053), (len(tu), first, last))",
    "   len(tu) == 35 and (first, last) == (1062, 1122), (len(tu), first, last))")

rep("""ck('segmento interno: 294 prima, 35 dopo, 374 totali',
   before == 294 and after == 35 and tot == 374, (before, after, tot))""",
    """ck('chiude il file: 339 prima, 0 dopo, 374 totali',
   before == 339 and after == 0 and tot == 374, (before, after, tot))""")

rep("""ck('copertura del segmento: righe 930-1053 continue',
   lrows[0] == 930 and lrows[-1] == 1053)""",
    """ck('copertura del segmento: righe 1062-1122 continue',
   lrows[0] == 1062 and lrows[-1] == 1122)
infile = db.execute('select count(*) from units where path = ? and line between ? and ?',
                    (PATH, 25, 1122)).fetchone()[0]
ck('copertura del file 374/374 su L58-L67 (%d)' % infile, infile == 374, infile)""")

rep("ck('nessun altra unita nel DB dentro 930-1053 (%d)' % inrange, inrange == len(tu), inrange)",
    "ck('nessun altra unita nel DB dentro 1062-1122 (%d)' % inrange, inrange == len(tu), inrange)")

rep("ck('distribuzione dei kind: 45 MISSION_TEXT', dict(kinds) == {'MISSION_TEXT': 45}, dict(kinds))",
    "ck('distribuzione dei kind: 34 MISSION_TEXT + 1 LOGBOOK',\n"
    "   dict(kinds) == {'MISSION_TEXT': 34, 'LOGBOOK': 1}, dict(kinds))")

rep("""for kind in ('LOGBOOK', 'CONVERSATION', 'TEXT'):
    got = [u['idx'] for u in tu if u['kind'] == kind]
    ck('%s: nessuna unita nel segmento (assenza dichiarata)' % kind, got == [], got)""",
    """log_units = sorted(u['idx'] for u in tu if u['kind'] == 'LOGBOOK')
ck('LOGBOOK: 1 unita (controllo positivo)', log_units == sorted(LOG) == [1], log_units)
ck('LOGBOOK: il testo e tradotto, non lasciato in inglese',
   by_idx[1]['italian'].strip() != by_idx[1]['english'].strip())
for kind in ('CONVERSATION', 'TEXT'):
    got = [u['idx'] for u in tu if u['kind'] == kind]
    ck('%s: nessuna unita nel segmento (assenza dichiarata)' % kind, got == [], got)""")

rep("""ck('token <...>: 0 nel sorgente e 0 in italiano (assenza dichiarata)',
   tok_en == 0 and tok_it == 0, (tok_en, tok_it))""",
    """fam_en = collections.Counter(t for u in su for t in TAGS.findall(u['english']))
fam_it = collections.Counter(t for u in tu for t in TAGS.findall(u['italian']))
ck('token <...>: 2 in inglese e 2 in italiano, stesso simbolo (%s)' % dict(fam_en),
   tok_en == 2 and tok_it == 2 and fam_en == fam_it == collections.Counter({'<ship>': 2}),
   (tok_en, tok_it, dict(fam_en), dict(fam_it)))""")

rep("ck('tab e virgolette: parita per unita (45 unita)', per_unit == [], per_unit[:10])",
    "ck('tab e virgolette: parita per unita (35 unita)', per_unit == [], per_unit[:10])")

rep("ck('tab iniziale presente dove il sorgente lo ha (40)', ntab == 40 and lead == [], (ntab, lead[:5]))",
    "ck('tab iniziale presente dove il sorgente lo ha (32)', ntab == 32 and lead == [], (ntab, lead[:5]))")

rep("""(('\\t', 'tab', 41), ('"', 'virgolette', 52))""",
    """(('\\t', 'tab', 32), ('"', 'virgolette', 68))""")

rep("""ck('virgolette dispari: 2 unita (10, 34) riprodotte, non chiuse',
   odd_en == (10, 34) and odd_it == (10, 34), (odd_en, odd_it))""",
    """ck('virgolette dispari: nessuna nel lotto (assenza dichiarata)', odd_en == () and odd_it == (),
   (odd_en, odd_it))""")

rep("""ck('duplicati inglesi (1 gruppo, 2 unita): resa italiana identica',
   len(dup_en) == 1 and dup_ok, (len(dup_en), dup_ok))""",
    """ck('duplicati inglesi: nessun gruppo (controllo negativo)', len(dup_en) == 0 and dup_ok,
   (len(dup_en), dup_ok))""")

rep("'verify L66 superato' if not fail else 'verify L66 fallito'",
    "'verify L67 superato' if not fail else 'verify L67 fallito'")

open(p, 'w', encoding='utf-8').write(s)
print('verify.py adattato a L67')
