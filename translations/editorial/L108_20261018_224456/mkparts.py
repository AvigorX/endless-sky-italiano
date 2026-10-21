"""mkparts.py — L108: costruisce `parts/part01-02.json` (36 unita', righe 216-335).

**14 `TEXT` sono FRAMMENTI `phrase:` composti a runtime** (unita' 1-14): soggetto + verbo + oggetto +
destinazione + frase finale. Non sono frasi: sono pezzi. Il vincolo e' **per casella** — maiuscola/minuscola e
punteggiatura — altrimenti il gioco mostra «...chiede di. portare...».

**3 `VALUE` identici** (15, 18, 29). **3 `DESCRIPTION`** (16, 19, 30) e **1 `DIALOG`** (17) tradotti.
**15 `MISSION_TEXT`** tradotti. **23 token** in sei famiglie, fra cui `<EDC-ship>` x8 (nuovo).
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

P1 = {
 1: '''Un Korath''',
 2: '''Un Kor Efret''',
 3: '''Un locale''',
 4: '''con gesti ti comunica che devi''',
 5: '''con gesti ti chiede di''',
 6: '''portare una piccola cassa''',
 7: '''portare un pacco''',
 8: '''accettare una spedizione che pesa meno di una tonnellata''',
 9: '''portare una scatola''',
 10: '''a <destination> per <payment>.''',
 11: '''Non dovrebbe occupare spazio di rilievo sulla vostra nave.''',
 12: '''È abbastanza piccolo da stare sotto il vostro sedile.''',
 13: '''L'oggetto è abbastanza piccolo da stare nelle vostre mani.''',
 14: '''È abbastanza piccolo da non occupare spazio di carico.''',
 15: '''Package to <planet>''',
 16: '''Porta una piccola consegna a <destination> per <payment> per un Kor Efret.''',
 17: '''Trovate un Korath che sembra avervi atteso nello spazioporto. Vi saluta mostrando i palmi, poi tende le mani come se aspettasse di ricevere il pacco. Consegnate la piccola spedizione e ricevete in cambio un piccolo pagamento di <payment>.''',
 18: '''Distress call from the <EDC-ship>''',
}

P2 = {
 19: '''I Quarg vi hanno chiesto di rispondere a una chiamata di soccorso della nave Efreti <EDC-ship>, precipitata su <destination>. Ci sono 40 superstiti da salvare.''',
 20: '''I lampi azzurri occasionali delle navi Quarg non sono una novità mentre attraversate lo spazio Efreti. Di solito è tutto ciò che vedete di questi alieni enigmatici. Oggi però, mentre atterrate, ricevete una chiamata urgente da una di loro.''',
 21: '''"Salute, Capitano della <ship>. Vittime di sorte incerta esigono il vostro zelo più diligente, perché molte famiglie non abbiano a piangere i morti. I droni Mereti hanno teso un agguato alla nave Efreti <EDC-ship> presso <planet> prima che potesse sottrarsi. Quaranta Korath vivono ancora, in attesa di soccorso."''',
 22: '''"Vado subito lì."''',
 23: '''"Non possono intervenire i Quarg?"''',
 24: '''"I Korath non mi interessano."''',
 25: '''"Abbiamo vinto i Mereti, ma al suo atterraggio la <EDC-ship> è caduta oltre la nostra portata. Senza una corazza robusta, su un mondo pesante si patisce assai. Un umano può raggiungerli giorni prima di una spedizione da Kuwaru Efreti."''',
 26: '''"Allora vado ad aiutarli."''',
 27: '''"Non rischio la mia nave per i Korath."''',
 28: '''Il Quarg tace per un po'. Alla fine risponde: "La vita è rara e preziosa nella vastità dello spazio. Guarda i mondi Korath e vedi ciò che resta quando non ci si cura di ciò che gli altri soffrono."''',
 29: '''Return the <EDC-ship> survivors''',
 30: '''Trasporta i <bunks> superstiti della <EDC-ship> su <planet>.''',
 31: '''Guardando la <EDC-ship> abbattuta, vi rendete conto all'improvviso di aver dimenticato le <bunks> cuccette che vi servono per gli evacuati.''',
 32: '''Vi serve un po' di tempo per trovare la <EDC-ship>. Vi aspettavate un qualche faro di segnalazione, ma o tacciono per non attirare i Mereti, oppure non ci sono superstiti. Quando riuscite ad aprire il portello, vi trovate di fronte un fucile termico puntato.''',
 33: '''Il Korath vi urla qualcosa addosso, e voi allungate le mani con i palmi in avanti. Zoppicando indietreggia di qualche passo, ma tiene l'arma puntata su di voi. Tirando fuori lentamente un comunicatore, riproducete una registrazione della trasmissione Quarg ricevuta prima. Appena il Korath sente la voce del Quarg, si entusiasma e abbassa il fucile. "<planet>?" chiede più volte. Fate un cenno col capo e mostrate di nuovo i palmi.''',
 34: '''Vi conduce dentro la nave, urlando in un comunicatore il cui messaggio viene poi diffuso dagli altoparlanti in tutta la nave. Mentre attraversate la sezione di ingegneria riuscite solo a dare un'occhiata intorno, ma è chiaro che vanno con l'energia di emergenza, e diversi sistemi dall'aria importante sono distrutti. La zona abitativa è un ospedale di fortuna. Non vedete corpi, ma qui ci sono molti meno Korath di quanti ne servirebbero per equipaggiare una nave di questa dimensione. È evidente che tutto l'equipaggio superstite è ferito in qualche misura, e più della metà è inabile o incosciente. Anche se la nave è in grado di volare nello spazio, non c'è equipaggio abbastanza per pilotarla.''',
 35: '''Contate in fretta i superstiti e comunicate alla vostra guida che potete portarli tutti. Lui imita il vostro cenno del capo, vi mostra i palmi e traccia cerchi rapidi. Pensate che sia d'accordo e che voglia fare in fretta. Chiamate il vostro equipaggio ad aiutare, e i superstiti vengono trasferiti a bordo della <ship>. Nel giro di un paio d'ore siete pronti a partire.''',
 36: '''Contate in fretta i superstiti e comunicate alla vostra guida che potete portarli tutti. Lui imita il vostro cenno del capo, vi mostra i palmi e traccia cerchi rapidi. Pensate che sia d'accordo e che voglia fare in fretta. Senza nessuno del vostro equipaggio ad aiutarvi, ci vogliono diverse ore per trasferire i superstiti sulla <ship>.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
ALL = {}
for d in (P1, P2):
    ALL.update(d)
SUBJ, VERB, OBJ, DEST, TAIL = [1, 2, 3], [4, 5], [6, 7, 8, 9], [10], [11, 12, 13, 14]
for idx, txt in ALL.items():
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]), (idx, TAGS.findall(eng[idx]), TAGS.findall(txt))
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx

# --- vincoli di composizione, per casella -------------------------------------------------
for i in SUBJ:
    assert ALL[i][0].isupper() and not ALL[i].endswith('.'), ('soggetto', i, ALL[i])
    assert kind[i] == 'TEXT'
for i in VERB:
    assert ALL[i][0].islower() and not ALL[i].endswith('.'), ('verbo', i, ALL[i])
    assert ALL[i].endswith('di') or ALL[i].endswith('devi'), ('verbo che regge un infinito', i, ALL[i])
    assert eng[i][0].islower()
for i in OBJ:
    assert ALL[i][0].islower() and not ALL[i].endswith('.'), ('oggetto', i, ALL[i])
    assert ALL[i].split()[0].endswith('are'), ('oggetto all infinito (prima parola)', i, ALL[i])
for i in DEST:
    assert ALL[i].startswith('a ') and ALL[i].endswith('.'), ('destinazione', i, ALL[i])
    assert eng[i].startswith('to ') and eng[i].endswith('.')
for i in TAIL:
    assert ALL[i][0].isupper() and ALL[i].endswith('.'), ('frase finale', i, ALL[i])
# ogni combinazione compone una frase leggibile: soggetto + verbo + oggetto + destinazione
probe = ' '.join([ALL[1], ALL[5], ALL[7], ALL[10], ALL[11]])
assert 'chiede di portare un pacco a <destination> per <payment>. Non dovrebbe' in probe, probe
assert '  ' not in probe and '. ' in probe
print('frase composta (prova):', probe)
assert kind[1] == kind[14] == 'TEXT' and [i for i in range(1, 15) if kind[i] != 'TEXT'] == []

# --- tipi e VALUE -------------------------------------------------------------------------
assert sorted(P1) == list(range(1, 19)) and sorted(P2) == list(range(19, 37))
assert [i for i in range(1, 37) if kind[i] == 'VALUE'] == [15, 18, 29]
assert [i for i in range(1, 37) if kind[i] == 'DESCRIPTION'] == [16, 19, 30]
assert [i for i in range(1, 37) if kind[i] == 'DIALOG'] == [17]
assert [i for i in range(1, 37) if kind[i] == 'TEXT'] == list(range(1, 15))
for i in (15, 18, 29):
    assert ALL[i] == eng[i], (i, ALL[i], eng[i])
# uniche identiche: i tre VALUE (per regola); nessuna altra coincidenza
assert [i for i in ALL if kind[i] != 'VALUE' and ALL[i].strip() == eng[i].strip()] == []
assert '<EDC-ship>' in ALL[18] and '<EDC-ship>' in ALL[29] and '<planet>' in ALL[15]

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (18 + 18)' % len(ALL))
