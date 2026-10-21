"""mkparts.py — L101: costruisce `parts/part01-02.json` (26 unita', righe 321-386).

**Ultimo segmento di `hai culture conversations.txt`: chiude il file a 147/147.**
Due contesti: `Hai Film Release` (321-331) e `Sick of Acorn Bread` (346-386).

**0 token.** **1 coppia di quadre** (unita' 13): `[seat, rest]`, la voce del dispositivo di traduzione che elenca
alternative — si riproduce, non si toglie. **Nessuna virgoletta dispari**, **nessuna ripetizione**.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

P1 = {
 1: '''Entrando nello spazioporto, notate la locandina di un film in Hai. Riconoscete che è ambientato su Darkrest e capite subito che dev'essere il film che Likeet aveva fatto. Il titolo in lingua Hai è stato tradotto con "L'ultimo riposo", ma il film completo non sembra ancora sottotitolato nella vostra lingua.''',
 2: '''(Vado a vederlo.)''',
 3: '''(Passo.)''',
 4: '''Trovate un cinema che proietta il film di Likeet. Non siete del tutto sicuri di cosa stia succedendo: qualcosa che ha a che fare con un mostro invisibile che abita la stazione e fa lentamente impazzire chi incontra. Sembra però un successo presso il pubblico Hai, e uscite dalla sala decisamente scossi.''',
 5: '''Trovate un cinema che proietta il film di Likeet, ma il vostro traduttore qui serve a poco. Il film è scarso di dialoghi, e le poche battute pronunciate sembrano riferimenti criptici alla letteratura e alla filosofia Hai. Il massimo che riuscite a capire è che il film parla di un mostro invisibile che abita la stazione e fa lentamente impazzire chi incontra. Sembra però un successo presso il pubblico Hai, e uscite dalla sala decisamente scossi.''',
 6: '''Con un po' di tempo da ammazzare mentre gli addetti Hai vi fanno la manutenzione alla nave, entrate nello spazioporto in cerca di qualcosa da mangiare. I ristoranti pubblicizzano i loro menù sulle vetrine con colori vivaci e accattivanti; fra la scelta ne notate uno che promette "autentica cucina Hai", insieme a un grande testo scritto in lingua Hai. Accanto c'è un venditore ambulante umano che offre snack e pasti già pronti.''',
 7: '''(Entro nel ristorante.)''',
 8: '''(Compro qualcosa dal venditore umano.)''',
 9: '''(Ripensandoci, non ho poi così fame.)''',
 10: '''Il cibo fatto dagli umani è di certo l'opzione più sicura. Il venditore vi vende un piatto di verdure al vapore, insieme a un filetto di un pesce dalla tinta giallastra che vi assicura essere perfettamente commestibile. Il pasto è alquanto insipido, ma il pesce è burroso e tenero. Smaltite gli avanzi in un contenitore della spazzatura lì vicino, e lo guardate emettere un bip melodioso mentre incenerisce i rifiuti.''',
 11: '''Un ristorante Hai offrirà di sicuro un'esperienza più originale. La porta fa un breve motivetto quando entrate, e una Hai di mezza età con le spalle voltate verso di voi grida qualcosa in lingua Hai.''',
 12: '''Restate immobili per un secondo, perché non è chiaro cosa voglia da voi.''',
 13: '''Il vostro traduttore cinguetta ubbidiente: "Si accomodi [a sedere, a riposare] dove preferisce! Arrivo subito."''',
}

P2 = {
 14: '''Solo un attimo dopo, la stessa cameriera vi guarda e cinguetta in quello che immaginate sia imbarazzo. "Mi dispiace tanto. Non sapevo che oggi avrei avuto il piacere di servire un umano. Prego, si sieda pure al bancone. Vengo subito a prendere l'ordine."''',
 15: '''Date un'occhiata in giro e notate che il ristorante è in realtà piuttosto affollato. Ci sono Hai in smoking eleganti, in abiti alla moda, in tenuta casual, e persino alcuni con certe tute da lavoro con un buco dietro per la coda; non sembra esserci nessun altro umano. Con pochi posti liberi, ne scegliete uno all'estremità, accanto a un Hai piuttosto grande con una tuta verde e un cappello di paglia arancione. Grugnisce in modo evasivo mentre vi sedete su uno sgabello chiaramente progettato per un organismo con la coda. Poco dopo la cameriera si avvicina e vi chiede l'ordine.''',
 16: '''"Prendo il piatto del giorno."''',
 17: '''"Vorrei della zuppa, per favore."''',
 18: '''"Lei è fortunato," dice. "Solo per oggi, ogni pasto è servito con un contorno gratuito di pane di ghiande." Sgambetta via per registrare e ritirare il vostro ordine.''',
 19: '''L'Hai accanto a voi grugnisce di nuovo, questa volta con evidente frustrazione, e si volta a parlare. "Pane di ghiande! Qui non servono altro, ormai. Da quando voi umani siete arrivati nel nostro spazio, è tutto quello che ci tocca mangiare. La panificazione tradizionale Hai è diventata un'arte perduta."''',
 20: '''"Mi può parlare della panificazione tradizionale Hai?"''',
 21: '''"Mi dispiace. Non volevo offendere la vostra cultura."''',
 22: '''Sembra in qualche modo calmato dal vostro interesse.''',
 23: '''L'espressione del suo viso si addolcisce. "Dovrei essere io a scusarmi. Non è colpa vostra se i menù dei nostri spazioporti sono cambiati sotto questo aspetto. Gli umani hanno anche portato nuova vita in molte parti della società Hai. È solo un peccato che si debba viaggiare lontano per trovare i tipi di pane che avevamo anni fa."''',
 24: '''"Mi può parlare di altri tipi di pane?" chiedete.''',
 25: '''"Oh sì." Si sposta sul suo sgabello. "Sono abbastanza vecchio da ricordare il pane hayipp, il pane yur ki e altri ancora. Hayipp è un cereale, simile al vostro 'granturco' umano, che macinato dà una farina integra di un bruno rossastro. Il pane era sostanzioso ma squisito." Notate il suo sguardo malinconico. "Yur ki è un latte, che ricaviamo dal bestiame che alleviamo. Forse ne avete visto un po' su Newhome; mi dicono che la vostra specie ha un animale simile chiamato 'pecora'. Il pane fatto con lo yur ki è ricco e sontuoso. È fra i miei cibi preferiti per colazione." Si ferma un momento e sembra un po' abbattuto. "Il pane di ghiande un tempo era raro nella cucina Hai. Troppo dolce. Ma da quando gli umani si sono uniti a noi sui nostri pianeti, vogliono solo pane di ghiande. La grande richiesta ha spostato tutti i pani tradizionali con cui sono cresciuto dalle zone ad alto passaggio come questo ristorante dello spazioporto. Mi manca averli facilmente a disposizione."''',
 26: '''Come se fosse una battuta, la cameriera arriva con i pasti di entrambi. L'Hai accanto a voi, di cui ancora non sapete il nome, sospira vedendo il suo pane di ghiande gratuito, ma lo mangia comunque. Finite i vostri pasti in silenzio e ve ne andate.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
for idx, txt in list(P1.items()) + list(P2.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]) == [], idx
    # le quadre sono la voce del dispositivo di traduzione: parita' esatta, non rimozione
    assert txt.count('[') == eng[idx].count('[') and txt.count(']') == eng[idx].count(']'), idx
    assert txt.strip(), idx
assert sorted(P1) == list(range(1, 14)) and sorted(P2) == list(range(14, 27))
assert [i for i in eng if '[' in eng[i]] == [13]
assert P1[13].count('[') == 1 and P1[13].count(']') == 1
assert all(eng[i].count('"') % 2 == 0 for i in eng)
assert eng[25].count('"') == 8 and P2[25].count('"') == 8

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (13 + 13)' % (len(P1) + len(P2)))
