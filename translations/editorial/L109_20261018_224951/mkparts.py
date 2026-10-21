"""mkparts.py — L109: costruisce `parts/part01-02.json` (33 unita', righe 338-451).

Quattro contesti: coda di `Efreti: Distress Call 2` (338-340), `Distress Call 3` (345-376), `Distress Call 4`
(388-434), `Distress Call 5` (437-451).

**27 `MISSION_TEXT` + 3 `VALUE` + 3 `DESCRIPTION`**: i `VALUE` restano **identici** (sono nomi di missione con
`<EDC-ship>` dentro), le `DESCRIPTION` si traducono. **`<origin>` e' la partenza**, non `<destination>`.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

P1 = {
 1: '''Squadre mediche vi aspettano appena atterrate, e ci vogliono diverse ore per evacuare i feriti. Dottori, o forse paramedici, si riversano su di loro per il triage, le cure e i preparativi per il trasporto. Tre che sono morti durante il volo vengono trattati con rispetto e portati fuori dalla <ship>.''',
 2: '''Quando arrivate allo spazioporto, trovate un messaggio dei Quarg. "Umano audace! Con copiosa gratitudine vi ricompensiamo per aver aiutato i Korath rimasti in secca. I Korath piangono da sempre la perdita dei loro mondi e, di tanto in tanto, sfidano i loro pericoli. Recuperano ciò che possono fra le rovine e cercano mondi dove un giorno possano vivere di nuovo. Ai giovani questo dà speranza, ma a volte vengono presi, e agli Efreti si ricorda perché vivono pigiati intorno a queste poche stelle."''',
 3: '''Il vostro comunicatore vi notifica un pagamento di <payment>.''',
 4: '''Recover the fallen crew of the <EDC-ship>''',
 5: '''Recupera i corpi dell'equipaggio morto della <EDC-ship> su <destination> e riportali a <origin>.''',
 6: '''Prima che possiate partire, una delegazione di Korath vi si avvicina con una certa esitazione. Indossano abiti che sembrano molto più raffinati di quelli della maggior parte dei Korath che avete incontrato, di certo nulla che mettereste per lavorare in uno spazioporto. Mentre fanno il tradizionale gesto di saluto, che ricambiate, siete incuriositi sia da ciò che vogliono sia da come lo chiederanno.''',
 7: '''Uno di loro tira fuori da una tasca una piccola custodia e ne estrae un dispositivo nero che sembra tre triangoli agganciati insieme. Ci sibila sopra per un momento e quello si solleva dalla sua mano. L'aria intorno comincia a tremolare, seguita dalla comparsa di un ologramma a grandezza naturale di un Quarg.''',
 8: '''"Salute, viaggiatore lontano," romba il Quarg. "Questi Amici dei Korath sono i principi del clan che avete soccorso. Grati per i vivi, non possono però piangere del tutto coloro che giacciono morti. Vi supplicano di tornare su <planet> e di riportare i loro perduti a casa, su <origin>."''',
 9: '''"Li riporterò a casa."''',
 10: '''"Lo farò, se mi pagano."''',
 11: '''"Non rischio la mia nave per i morti."''',
 12: '''Il capo del gruppo si affloscia visibilmente mentre il Quarg traduce le vostre parole. Due Korath più giovani lo sorreggono mentre il gruppo si volta e se ne va.''',
 13: '''Non avevate capito quanto fosse teso il gruppo finché non li avete visti rilassarsi appena le vostre parole li raggiungono. Sembrano sollevati dalla vostra risposta.''',
 14: '''Il gruppo si distende in fretta, e vedete passare tra loro un'onda di sollievo e di orgoglio.''',
 15: '''Il capo si volta e parla direttamente a voi. I suoi occhi non si staccano mai dai vostri mentre aspettate la traduzione. "Gli equipaggi Efreti hanno famiglie, perché i bambini imparano lavorando con i genitori. Per alcune famiglie sono andate perdute tre generazioni. Non tenteremo di recuperare la nave, perché nessuno ha il cuore di pilotarla. Vi offriamo il titolo per recuperare la <EDC-ship> e per portare il nostro lutto lontano da qui."''',
 16: '''Recover the fallen of <EDC-ship>''',
 17: '''Riporta i corpi dell'equipaggio morto della <EDC-ship> su <planet>.''',
}

P2 = {
 18: '''Trovata la <EDC-ship>, voi e il vostro equipaggio vi entrate indossando tute ambientali. Sono passati diversi giorni dallo schianto, e le navi Korath sono roventi. Sarà un compito sgradevole con le tute, e forse impossibile senza.''',
 19: '''Trovata la <EDC-ship>, vi entrate indossando una tuta ambientale. Sono passati diversi giorni dallo schianto, e le navi Korath sono roventi. Sarà un compito sgradevole con la tuta, e forse impossibile senza, soprattutto senza nessuno del vostro equipaggio ad aiutarvi.''',
 20: '''Mentre il vostro ingegnere lavora per rinfrescare l'atmosfera con aria esterna, il resto dell'equipaggio raccoglie i corpi e li depone nelle bare fibrose e vagamente a forma di uovo che i Korath hanno fornito. Mentre le spostate nella stiva, scoprite che si incastrano insieme come una covata di uova in un nido.''',
 21: '''Mentre il vostro compagno di equipaggio lavora per rinfrescare l'atmosfera con aria esterna, voi raccogliete i corpi e li deponete nelle bare fibrose e vagamente a forma di uovo che i Korath hanno fornito. Mentre le spostate nella stiva, scoprite che si incastrano insieme come una covata di uova in un nido.''',
 22: '''Uno alla volta, raccogliete i corpi e li deponete in bare fibrose e vagamente a forma di uovo che i Korath hanno fornito. Mentre le spostate nella stiva, scoprite che si incastrano insieme come una covata di uova in un nido. Ci vuole un po' perché l'aria esterna rinfreschi l'atmosfera e l'odore diventi tollerabile.''',
 23: '''Tornati sulla nave Korath, raccogliete con cura tutti gli effetti personali che riuscite a trovare negli alloggi e li imballate per il trasporto. Non avete modo di sapere se i Korath delle fotografie che trovate si stiano ora riprendendo al sicuro o giacciano nella vostra stiva.''',
 24: '''L'equipaggio fa un ultimo giro per spostare le macerie, sia per valutare eventuali riparazioni future sia per assicurarsi di non aver dimenticato nessuno, o parti di qualcuno. Pulite e disinfettate come meglio potete e tornate alla vostra nave per il viaggio verso <destination>.''',
 25: '''Per precauzione, fate un ultimo giro per spostare le macerie, sia per valutare eventuali riparazioni future sia per assicurarvi di non aver dimenticato nessuno, o parti di qualcuno. Pulite e disinfettate come meglio potete e tornate alla vostra nave per il viaggio verso <destination>.''',
 26: '''Una folla si riversa dallo spazioporto quando atterrate. Ci vuole un po' perché gli operai stabiliscano sbarramenti e aprano un passaggio per far arrivare i trasporti alla vostra stiva. Una squadra in uniforme vi saluta formalmente quando aprite il portello, e contate le bare insieme a loro. Poi mostrate loro le scatole degli effetti personali, che maneggiano con cura. Un ufficiale vi ringrazia e vi consegna un chip dati che vi ricorda vagamente una licenza.''',
 27: '''La folla è stata composta, ma quando la prima bara esce dalla nave scoppia in una cacofonia di suoni che abbaiano. Alcuni Korath cercano di precipitarsi avanti ma vengono trattenuti da altri, presumibilmente i loro familiari.''',
 28: '''Invece di intromettervi nel loro dolore, tornate alla vostra nave e inserite il chip dati ricevuto nei vostri sistemi. Purtroppo le informazioni sono in una lingua aliena, così lo mettete da parte e lavorate a un piano per recuperare la <EDC-ship>. Mettendo insieme qualche nota sulla nave e sul numero di persone che trasportava, è chiaro che vi serviranno almeno 66 membri d'equipaggio in più con cui poter comunicare per riuscire a recuperarla. Il sistema più vicino che vi venga in mente con molti parlanti umani è su Greenwater, nello spazio Hai.''',
 29: '''<EDC-ship> salvage team''',
 30: '''Assolda una squadra di recupero di <bunks> persone su <destination> per recuperare la nave Efreti <EDC-ship>.''',
 31: '''Vi servono <bunks> cuccette libere per trasportare la squadra di recupero.''',
 32: '''Molte storie parlano di Hai a cui piacciono il cambiamento e l'eccitazione, ma il loro entusiasmo sembra morto. Il pensiero della specie che li ha invasi ispira ancora paura. Nessun Hai ha il coraggio di recuperare una nave finita nel fuoco incrociato della guerra fra Mereti e Sestor.''',
 33: '''Per fortuna ci sono molti umani disposti a rischiare per il giusto compenso, anche con la vita comoda che hanno nello spazio Hai. Accompagnate i nuovi membri dell'equipaggio alle loro cuccette e vi preparate a recuperare la <EDC-ship>.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
ALL = {}
for d in (P1, P2):
    ALL.update(d)
for idx, txt in ALL.items():
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]), (idx, TAGS.findall(eng[idx]), TAGS.findall(txt))
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx

assert sorted(P1) == list(range(1, 18)) and sorted(P2) == list(range(18, 34))
assert [i for i in range(1, 34) if kind[i] == 'VALUE'] == [4, 16, 29]
assert [i for i in range(1, 34) if kind[i] == 'DESCRIPTION'] == [5, 17, 30]
for i in (4, 16, 29):
    assert ALL[i] == eng[i], (i, ALL[i], eng[i])
assert [i for i in ALL if ALL[i].strip() == eng[i].strip()] == [4, 16, 29]
# <origin> e' la partenza, <destination> l'arrivo: non si scambiano
assert TAGS.findall(ALL[5]) == ['<EDC-ship>', '<destination>', '<origin>']
assert TAGS.findall(ALL[17]) == ['<EDC-ship>', '<planet>']
assert TAGS.findall(ALL[8]) == ['<planet>', '<origin>']
# <bunks> e' un numero: regge sia "squadra di N persone" sia "N cuccette"
assert TAGS.findall(ALL[30]) == ['<bunks>', '<destination>', '<EDC-ship>']
assert TAGS.findall(ALL[31]) == ['<bunks>']
# i tre quasi-duplicati non sono identici: cambiano soggetto e coda
assert len({ALL[20], ALL[21], ALL[22]}) == 3
assert len({ALL[18], ALL[19]}) == 2 and len({ALL[24], ALL[25]}) == 2

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (17 + 16)' % len(ALL))
