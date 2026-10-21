"""mkparts.py — L100: costruisce `parts/part01-03.json` (44 unita', righe 212-320).

Due contesti: `Academy Motto` (227-263) e `Robotic Musical 1` (278-306).

**Tre `UI_LABEL`** (unita' 5, 12, 14): `field trip`, `pleasant lunch`, `finishing chat` — etichette di salto,
lasciate **identiche** e asserite una per una. **1 token**: `<last>` nell'unita' 40. **Zero quadre**.
**Quattro citazioni aperte e non chiuse** (unita' 23, 24, 39, 41): il discorso continua nell'unita' successiva,
quindi ognuna ha **una** virgoletta. **Nessuna ripetizione**.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

LABELS = {5: 'field trip', 12: 'pleasant lunch', 14: 'finishing chat'}

P1 = {
 1: '''In questo giorno particolare, lo spazioporto è affollato oltre ogni credere da qualche arcana confluenza di caso e logistica. Dopo aver sbrigato la maggior parte dei vostri affari, le autorità portuali vi hanno informato che non c'è una finestra di partenza sicura libera per almeno sette ore (e nemmeno questa è una promessa). Restate quindi solo, a riempire quel pezzo di tempo inatteso nelle prime ore del mattino.''',
 2: '''(Gioco sulla mia nave.)''',
 3: '''(Do un'occhiata più in là.)''',
 4: '''Senza voglia di perdervi in un'enorme città Hai, caricate semplicemente una console di intrattenimento per tenervi occupati nelle ore successive.''',
 5: LABELS[5],
 6: '''La tendenza degli Hai a stipare le persone in spazi vivaci ma densamente popolati è in bella mostra mentre vi fate strada fra frotte di Hai che per lo più si sforzano educatamente di non urtarvi. Striscioni colorati, bandiere, murales e persino finestre offrono squarci brillanti agli stili architettonici spesso utilitaristici che ne stanno alla base. Insegne di benvenuto proiettate in ologramma ornano persino gli ingressi di diversi palazzi che oltrepassate, con avvertenze per i venditori porta a porta.''',
 7: '''Il recinto esterno di un complesso di appartamenti porta un cartello molto grande che, secondo il vostro traduttore, dice: "Niente contenuti meme qui, per favore."''',
 8: '''Dopo un po' trovate quello che sembra un caffè, o l'equivalente, e vi sedete dove potete avere una buona vista su uno dei complessi di edifici più imponenti nei paraggi. Dopo un momento un ologramma integrato nel tavolo vi chiede, in standard umano, se volete ordinare dal tavolo o parlare con un membro del personale.''',
 9: '''(Ordino dal tavolo.)''',
 10: '''(Ordino da una persona.)''',
 11: '''Una Hai cordiale emerge a prendere l'ordine e vi informa con cortesia che c'è un supplemento del 10% per mangiare sulla terrazza. Visto che per un capitano di nave non è una cifra significativa, fate cenno di sì e cercate di capire che cosa state mangiando. Alla fine optate per un panino con burro di ghiande e fette di verdure che sembrano speziate, o sottaceto, non ne siete sicuri. Era l'articolo più consigliato dal personale e non è arrivato con domande di follow-up sulle preferenze alimentari degli Hai a cui non sapreste rispondere.''',
 12: LABELS[12],
 13: '''L'interfaccia è piuttosto fastidiosa da usare con mani di misura umana, ma alla fine optate per un panino con burro di ghiande e fette di verdure che sembrano speziate, o sottaceto, non ne siete sicuri. Era l'articolo più consigliato e non è arrivato con domande di follow-up sulle preferenze alimentari degli Hai a cui non sapreste rispondere.''',
 14: LABELS[14],
 15: '''Mentre mangiate il vostro pranzo strano ma in realtà sorprendentemente gustoso, notate il grande testo scritto sopra il cancello d'ingresso del complesso di edifici di fronte. Dopo un momento il vostro traduttore nota dove state guardando e ve lo legge ad alta voce.''',
 16: '''"Conoscere è guidare, studiare è conoscere, servire è studiare, guidare è servire."''',
}

P2 = {
 17: '''Naturalmente il vostro traduttore non può rispondere alle domande, così finite il pranzo e lasciate perdere finché non arriva un membro del personale a ritirare il piatto.''',
 18: '''(Chiedo loro di cosa si tratta.)''',
 19: '''(Tengo per me i miei pensieri.)''',
 20: '''Il membro del personale prende il piatto e vi augura una bella giornata.''',
 21: '''Mentre ritirano il piatto dal tavolo chiedete loro del testo sul cancello.''',
 22: '''"Oh, quella è l'Academy cittadina. È una... ehm..." si ferma un momento e riferisce qualcosa in Hai che il vostro traduttore converte subito in "università non tecnica".''',
 23: '''Con uno sguardo sorpreso al dispositivo, sorride e continua in Hai: "Se vuoi diventare un dirigente, un politico, un assistente sociale, o anche solo un oratore pubblico, vai all'Academy e segui corsi di leadership e comunicazione. A rigor di termini non è necessario andarci, ma molti posti semplicemente non ti accettano in quel tipo di ruoli senza una qualche qualifica dell'Academy, e offrono davvero ottime competenze. Io ci andrò l'anno prossimo per fare un vero corso di lingua umana.''',
 24: '''"Tecnicamente le Academy sono tutte indipendenti, ma condividono tutte lo stesso motto. Ed è anche una cosa obbligatoria, ed è di questo che parla il motto. Mi dicono che la maggior parte degli umani lo trova al contrario, ma non lo è. Le Academy tengono d'occhio i loro diplomati: se guidi per interesse personale, servi senza studiare, studi senza imparare o sprechi le tue conoscenze senza applicarle, è noto che revocano le qualifiche. La frequenza è gratuita, quindi ci si aspetta che non si sprechi ciò che ti spendono tempo a insegnare.''',
 25: '''"Questa è piuttosto prestigiosa, ma quelle vicino agli spazioporti lo sono sempre." Ammicca. "L'esperienza che viene dall'esposizione naturale vale più di quanto il denaro possa comprare, dopotutto."''',
 26: '''Un momento dopo il vostro commpad vi avvisa che vi è stata assegnata una finestra di partenza dallo spazioporto in tempi relativamente brevi.''',
 27: '''"Bene, devo occuparmi di altri clienti. Le auguro una buona giornata!" dice, lasciandovi ai vostri affari.''',
 28: '''Percorrendo il viale principale di questo spazioporto quasi non badate a una pila di casse ammucchiate alla rinfusa nello spartitraffico. Non è raro che le casse appena scaricate restino temporaneamente davanti a diverse attività di un porto, sistemate ben in vista fuori dal flusso dei pedoni, ma è l'ammucchiamento disordinato che sembra fuori posto.''',
 29: '''Non fate in tempo a rallentare il passo per prestarvi attenzione che la pila di casse prende vita all'istante.''',
 30: '''Parte la musica e una mezza dozzina di caricature robotiche di Hai in abiti esagerati saltano fuori da varie casse e si mettono a sgambettare in una serie di interazioni presumibilmente pensate per far ridere, a giudicare almeno da come continuano a voltarsi l'una dall'altra per "guardare" il pubblico e ammiccare. Striscioni e glifi olografici, presumibilmente informazioni pubblicitarie, scorrono attraverso una serie di schermate mentre il ciclo procede, finché l'intero gruppo sembra concludere; ogni spettatore riceve una qualche supplica da almeno un robot, prima che tutti si arrampichino di nuovo dentro le casse.''',
 31: '''Per tutto il tempo una manciata di Hai si è fermata a guardare, e un paio ridacchiano alla conclusione prima di proseguire. I più si limitano a roteare gli occhi e tirare dritto. Un bambino si avvicina troppo mentre i genitori gli girano intorno e un piccolo cartello olografico rosso lampeggia verso di loro. Nessuno sembra avere voglia di spiegarvi cosa avete appena visto, e per il momento le casse restano ostinatamente chiuse.''',
}

P3 = {
 32: '''Ora che ci pensate, non siete sicuri che siano tutti rientrati nelle stesse casse da cui erano usciti.''',
 33: '''Parte la musica e una mezza dozzina di caricature robotiche di Hai in abiti esagerati saltano fuori da varie casse e si mettono a sgambettare in una serie di interazioni. Il vostro traduttore fatica a stare dietro a una raffica di battute che presumibilmente sono giochi di parole spiritosi e che si traducono male. L'umorismo sembra improvvisato all'inizio, ma l'illusione è così buona che vi rendete conto dell'impossibilità che dei robot improvvisino solo dopo. Il tutto è accompagnato da una partitura musicale, con pause di battuta in vari punti in cui gli Hai animatronici continuano a voltarsi l'uno dall'altro per 'guardare' il pubblico e ammiccare. Striscioni e glifi olografici scorrono in una serie di schermate che vi informano che questa è la pubblicità di un musical comico completamente robotico intitolato "Le regole della nonna". Sostiene di essere completo di risposte interattive alle provocazioni del pubblico e fornisce un elenco di date e locali, tutti in un futuro lontano, in cui sarà in scena.''',
 34: '''Alla fine ognuno dei robot fa una posa e invita una diversa fascia di pubblico a venire a "vivere il decennio della propria vita", con biglietti a partire da 73 crediti, prima che l'intero gruppo concluda e si arrampichi subito di nuovo nelle casse. Non siete sicuri che siano tutti rientrati nelle stesse casse da cui erano usciti.''',
 35: '''Per tutto il tempo una manciata di Hai si è fermata a guardare, e un paio ridacchiano alla conclusione prima di proseguire. I più si limitano a roteare gli occhi e tirare dritto.''',
 36: '''Un Hai di mezza età nella folla, con un grigio da procione intorno agli occhi, indossa il tipo di abbigliamento tipico dei loro capitani mercantili. Vi scruta con curiosità e vi si avvicina. "Bene, bene, Capitano, che scatola notevole che ha lì. Non sapevo che avessero iniziato a fare dispositivi di traduzione dal vivo! È riuscita a starci dietro?"''',
 37: '''"Oh, è il primo del suo genere."''',
 38: '''"Credo di aver capito il senso, anche se legge solo se guardo direttamente le cose."''',
 39: '''"Ah sì, suppongo che sia una funzione logica," dice. "Immagino che sarebbe piuttosto scomodo se provasse a leggere ogni testo nei paraggi.''',
 40: '''"Il primo?" Vi studia per un secondo. "Oh, lei è il Capitano <last>! Che piacere conoscerla."''',
 41: '''Vi guarda da capo a piedi con un sorriso sornione. "In qualche modo è più basso di quanto immaginassi.''',
 42: '''"Beh, se ne ha l'occasione, le consiglio lo spettacolo. L'ho visto qualche mese fa ed è davvero molto bello. Particolarmente popolare sui nostri mondi con molti umani."''',
 43: '''Vi saluta con un cenno amichevole. "Devo andare. Non si avvicini troppo ai display, non amano essere toccati!"''',
 44: '''L'Hai sembra molto soddisfatto mentre si allontana, ridacchiando tra sé e sé mentre se ne va.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
for idx, txt in list(P1.items()) + list(P2.items()) + list(P3.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]), (idx, TAGS.findall(eng[idx]), TAGS.findall(txt))
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx
    # le tre UI_LABEL sono etichette di salto: identiche al sorgente, non tradotte
    if kind[idx] == 'UI_LABEL':
        assert txt == eng[idx], (idx, txt, eng[idx])
assert sorted(P1) == list(range(1, 17)) and sorted(P2) == list(range(17, 32)) and sorted(P3) == list(range(32, 45))
assert [i for i in range(1, 45) if kind[i] == 'UI_LABEL'] == [5, 12, 14]
# quattro citazioni aperte e non chiuse: il discorso continua nell'unita' dopo
assert [i for i in eng if eng[i].count('"') % 2] == [23, 24, 39, 41]
assert [i for i in (P1 | P2 | P3) if (P1 | P2 | P3)[i].count('"') % 2] == [23, 24, 39, 41]
assert eng[40].count('<last>') == 1 and P3[40].count('<last>') == 1

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2), ('part03.json', P3)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (16 + 15 + 13)' % (len(P1) + len(P2) + len(P3)))
