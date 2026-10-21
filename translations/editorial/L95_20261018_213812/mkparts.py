"""mkparts.py — L95: costruisce `parts/part01-03.json` (24 unita' tradotte, righe 148-190).

Terzo lotto di `coalition culture conversations.txt`, contesto `Coalition Folklore: Kimek`.
Le unita' **18 (`defend r`), 23 (`defend rw`) e 25 (`defend w`) sono `UI_LABEL` di salto**: NON entrano nelle
parti, le scrive `check.py` dal sorgente e le asserisce identiche (tradurle romperebbe i `goto`).

Il parlato dei Kimek ha la stessa sintassi invertita di Saryd e Arach: ordine marcato italiano.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

MAIN_GATE = '''(Aiuta a tenere chiuso il cancello principale.)'''

P1 = {
 1: '''Un Kimek vi ferma appena entrate nello spazioporto. "Occupato, Capitano?", chiede. "Oggi in corso, un festival culturale è, e parteciparvi, chiunque può. Una rievocazione della vecchia fiaba dell''Assedio di Primavera', è. Interpretare uno dei personaggi, chiunque può."''',
 2: '''"Sembra divertente. Dove si tiene?"''',
 3: '''"Mi dispiace, in questo momento ho troppo da fare."''',
 4: '''Vi chiede di seguirlo e insieme prendete un treno che porta in un'altra zona della città; scendete al limitare di un grande parco. Lì vedete molti gruppi di accampamenti sparsi nella savana e altrettanti forti di legno che dominano dalla cima di un lungo pendio. Ogni "gruppo" di forte e accampamento è separato dagli altri da molte chiazze di vegetazione che salgono lungo il pendio.''',
 5: '''Seguite il Kimek ancora per un po', finché non trova una coppia di accampamento e forte con un posto libero da entrambe le parti. "Beh Capitano, scegliere una parte da interpretare, dovete. Prenderci la mano, ci riuscirete, una volta iniziato, l'evento è, ma come rapido riassunto: prendere i 'raccolti' dentro il forte prima che il tempo scada, la squadra attaccante deve. Impedirglielo, i difensori devono. Alla fine, premiati, i vincitori sono."''',
 6: '''"Mi unisco agli attaccanti."''',
 7: '''"Mi unisco ai difensori."''',
 8: '''"Un momento: se questa è una fiaba, come mai la rievocate come se potesse vincere una parte qualsiasi?"''',
 9: '''Cinguetta, come se si aspettasse la domanda. "Vista da un menestrello, la battaglia fu. Viaggiando su campi come questi, lui era, quando il forte e l'accampamento dei predoni scorse in lontananza. Nascosto nel fogliame vicino alla scena, si era, e scrivendola e dipingendola mentre accadeva, stava. Quando la battaglia raggiunse il suo culmine, sollevati dal vento, molti fiori furono, e la vista gli bloccarono. Quando il vento si placò, finita, la battaglia era. Primavera era, così 'Assedio di Primavera' divenne il titolo della storia."''',
}

P2 = {
 10: '''Vedendo che avete ancora domande, continua. "Sciocca e priva di senso, a volte, la storia è. Lo sappiamo, noi, e che il menestrello cercasse solo di intrattenere il pubblico, ma con ogni forma di racconto classico, non è forse così?" Cinguetta ancora, guarda il gruppo in cima al pendio e l'altro nell'accampamento, poi riprende. "Per quanto estraneo possa sembrare, partecipare, non lo farete? Forse divertirvi, potreste."''',
 11: '''"Va bene, mi unisco agli attaccanti."''',
 12: '''"Va bene, mi unisco ai difensori."''',
 13: '''Vi conduce al piccolo forte in cima al pendio. I cancelli si aprono mentre quelli dentro (per lo più Kimek, come previsto, ma anche un paio di Arach e un Saryd solitario) si stanno ancora preparando. Al centro c'è una piccola "fattoria", con riproduzioni di plastica al posto dei raccolti. Le mura del forte sono fatte di grossi tronchi, fittamente coperti da ciuffi di spine rossastre e insidiose, lunghe quasi quanto un braccio. All'interno vedete che un livello superiore con merli è raggiungibile da scale ai due lati del cortile; notate anche che i difensori indossano tutti una striscia di stoffa verde sopra i vestiti. Un altro organizzatore Kimek, con un gilet di cuoio grezzo che immaginate essere l'equivalente Kimek dell'armatura medievale, vi viene incontro al cancello. Saluta il collega, che vi presenta e dice che avete scelto di unirvi ai difensori, poi torna giù per il pendio.''',
 14: '''"Lieti di avervi nella guarnigione, il nostro forte è", esordisce il Kimek corazzato. "Informati sull'obiettivo del nemico, immagino che siate. Proteggere la nostra fattoria, dobbiamo, quindi lasciare che i raccolti vengano rubati, non possiamo." Vi dice di seguirlo fino al "maschio", una baracca troppo piccola per chiunque non sia Kimek, e vi consegna un lungo pezzo di stoffa verde. Vi spiega poi che va indossato, così che gli altri capiscano a quale squadra appartenete. Mentre ve lo avvolgete come una sciarpa, notate che dietro la baracca c'è un cancello più piccolo, che dà accesso al forte. Quando avete finito, vi fa fare un breve giro del resto del forte, portandovi sui merli e sopra il cancello principale, dove vedete secchi con quello che a prima vista sembra acqua. La guida vi spiega che il liquido dentro è in realtà piuttosto scivoloso e che durante la rievocazione viene versato lungo il pendio per rallentare gli attaccanti.''',
 15: '''Quando ha finito, vi dice di aspettare nel cortile, perché la "battaglia" comincerà presto. Passano alcuni minuti prima che risuoni un fischietto acuto, e il Kimek a capo del forte annuncia a tutti che l'altra parte ha iniziato l'attacco. Il cancello principale è chiuso e alcuni difensori cominciano a sistemare oggetti pesanti dietro per sbarrare l'ingresso; altri sono già sui merli, in attesa del momento giusto per usare i secchi di liquido scivoloso.''',
 16: '''(Aiuta a rinforzare il cancello principale.)''',
 17: '''(Vai ad aiutare a rallentare gli attaccanti.)''',
}

P3 = {
 19: '''Vi unite agli altri nel radunare e spostare oggetti pesanti e trovate presto alcune casse dietro la baracca, che un paio di Arach aiutano a portare al cancello. Alcuni Kimek prendono tronchi che trovano accatastati sotto una scala e li portano a loro volta, conficcandone un'estremità nel terreno e appoggiando l'altra contro la porta. Il liquido versato sugli attaccanti li rallenta per qualche minuto, ma quando avete finito stanno già martellando il cancello. Quasi tutti quelli dentro il forte, in particolare il Saryd che si è unito, corrono al cancello principale per cercare di tenerlo chiuso, ma alcuni Kimek girano dietro a controllare il cancello più piccolo.''',
 20: MAIN_GATE,
 21: '''(Vai con gli altri a controllare il cancello posteriore.)''',
 22: '''Arrivati al cancello posteriore, voi e i Kimek restate in silenzio e tendete l'orecchio a chiunque si avvicini da quel lato del forte. In effetti, sentite le zampe Kimek frusciare nell'erba mentre gli attaccanti aggirano il forte. Per fortuna non molti sono venuti a questo cancello, così, con il vostro aiuto, i compagni Kimek non fanno molta fatica a tenerlo chiuso. Grazie al fatto che il cancello principale è stato rinforzato, il gruppo là tiene abbastanza bene che altri vengono sul retro a dare una mano, e dopo qualche minuto di lotta con gli attaccanti sul cancello risuona un altro fischietto. Segna che il tempo è scaduto e che i difensori hanno vinto.''',
 24: '''Con le fortificazioni di prima che aiutano a tenerlo chiuso, difendere il cancello principale si rivela abbastanza facile. Dopo qualche minuto, però, sentite un trambusto da dietro la baracca. Andate a controllare con gli altri e arrivate a vedere il cancello piccolo aperto: gli attaccanti, che portano fasce blu al posto del verde della vostra squadra, sono già entrati. Il fischietto risuona di nuovo, segnando la fine della battaglia e la vittoria degli attaccanti.''',
 26: '''Salite le scale e ricevete uno dei secchi con la sostanza scivolosa. Notate però che quassù sono tutti Kimek e Arach, e che versano il liquido solo direttamente davanti al cancello. Quando vedete alcuni attaccanti con le fasce blu avanzare dai lati, dove il liquido non è stato versato, lanciate un secchio nella loro direzione. Questo lascia una striscia di liquido su quel lato, e quelli che attaccano da lì perdono l'appoggio, inciampando e cadendo più e più volte. Quando i compagni capiscono cosa avete fatto, cominciano a incitarvi, spingendovi a lanciare altri secchi per coprire i lati mentre loro continuano a inondare il centro. Nonostante i vostri sforzi, però, gli attaccanti riescono alla fine a salire il pendio e cominciano a martellare il cancello. Quasi tutti quelli dentro il forte, compreso il Saryd, corrono al cancello principale per cercare di tenerlo chiuso, ma alcuni Kimek girano invece dietro a controllare il cancello più piccolo.''',
 27: MAIN_GATE,
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
NT = [18, 23, 25]
for idx, txt in list(P1.items()) + list(P2.items()) + list(P3.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert idx not in NT and kind[idx] == 'MISSION_TEXT', idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert txt.strip(), idx
assert sorted(P1) == list(range(1, 10)), sorted(P1)
assert sorted(P2) == list(range(10, 18)), sorted(P2)
assert sorted(P3) == [19, 20, 21, 22, 24, 26, 27], sorted(P3)
assert P3[20] == P3[27] == MAIN_GATE
assert [i for i in range(1, 28) if kind[i] == 'UI_LABEL'] == NT

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2), ('part03.json', P3)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (9 + 8 + 7) + 3 UI_LABEL dal sorgente' % (len(P1) + len(P2) + len(P3)))
