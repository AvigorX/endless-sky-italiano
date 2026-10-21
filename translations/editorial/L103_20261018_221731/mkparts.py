"""mkparts.py — L103: costruisce `parts/part01-02.json` (42 unita', righe 118-249).

**Quattro tipi** in un lotto: 28 `MISSION_TEXT`, 8 `DIALOG`, 3 `DESCRIPTION`, 3 `VALUE`.

Regola dei `VALUE` (unita' 1, 21, 39): sono **nomi di missione e di carico** — *riferimenti di dato*. Restano
**identici all'inglese**, come le `UI_LABEL` di L95-L96; tradurli lotto per lotto creerebbe un tabellone misto.
`DESCRIPTION` e `DIALOG` sono testo mostrato al giocatore e si traducono per intero.

**19 token** in sei famiglie, riprodotti per unita' e nell'ordine. **Una citazione aperta e non chiusa**
(unita' 30). **Cinque ripetizioni** da costanti uniche: 8/12, 10/13, 21/39 (`VALUE`), 22/40 (`DESCRIPTION`),
36/41 (`DIALOG`).
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

HELP_WHERE = '''"Allora mi piacerebbe aiutare. Dove li dispiego?"'''
HEADED = '''"In realtà adesso sono diretto in un'altra parte della galassia, mi dispiace."'''
DESC_CARGO = '''Andate su <stopovers> a ritirare <cargo>, poi portate tutto su <destination>, dove i Quarg si preparano ad aprire ai visitatori umani la prima sezione del loro mondo ad anello.'''
LOADED = '''Il <cargo> viene caricato sulla vostra nave sotto stretta sorveglianza, ogni cassa accuratamente contata.'''
VALUE_1 = 'Deploy Quarg Scanners'
VALUE_2 = 'Human Construction Materials'

P1 = {
 1: VALUE_1,
 2: '''Dirigetevi verso ciascuno dei sistemi segnalati per dispiegare i satelliti di scansione Quarg, poi andate su <destination> a ritirare il pagamento.''',
 3: '''Un Quarg si avvicina lentamente quando vi nota nello spazioporto. "Salute, amico umano. Avresti per caso il tempo di ascoltare una proposta? Cerchiamo un pilota disposto ad aiutarci a dispiegare alcuni satelliti di scansione."''',
 4: '''"Certo, dove li dispiego?"''',
 5: '''"A che servono i satelliti?"''',
 6: '''"Non ho tempo, no."''',
 7: '''"Per aiutare gli umani dall'altra parte di questa regione, a Sud, a essere meglio preparati contro gli attacchi in arrivo, e ad aiutarli a tenere traccia delle navi che passano per i loro sistemi."''',
 8: HELP_WHERE,
 9: '''"Aiutare? Perché volete aiutare la gente laggiù all'improvviso?"''',
 10: HEADED,
 11: '''"Perché?" Si ferma un secondo. "Di certo avrai visto gli stolti teppisti che infestano tutta questa regione. Qui possiamo occuparcene noi, ma di solito non viaggiamo lontano. Per promuovere la pace dappertutto, senza un altro inutile massacro, fornire qualche misura che scoraggi ulteriori attacchi è solo una cortesia."''',
 12: HELP_WHERE,
 13: HEADED,
 14: '''"Su <waypoints>. Quando avrai finito, torna qui e riceverai <payment>."''',
 15: '''Appena arrivate alla vostra nave, trovate vari Quarg con robot caricatori che infilano i quattro satelliti nella stiva. I satelliti hanno la forma di piramidi triangolari, e ogni punta della piramide principale è sormontata da un'altra piramide triangolare più piccola. Da questa distanza non riuscite a distinguerlo bene, ma vi chiedete se anche le piramidi più piccole siano sormontate da piramidi ancora più piccole. Ognuno dei dispositivi è all'incirca grande la metà di voi, ma probabilmente pesa molto più di voi.''',
 16: '''Aprite la stiva e lasciate che uno scanner Quarg esca alla deriva nel vuoto.''',
 17: '''Guardando il pianeta che fu colonia di schiavi mentre dispiegate il loro scanner, vi chiedete se i Quarg abbiano saputo della storia di Poisonwood, e se sia per questo che hanno deciso di aiutare con la sorveglianza.''',
 18: '''Liberate uno scanner Quarg e lo lasciate andare via dalla nave.''',
 19: '''Sebbene chi vive sul pianeta qui non sembri preoccuparsi dei pirati che ogni tanto chiedono un tributo, forse arriveranno ad apprezzare la presenza pirata ridotta, ammesso che lo scanner Quarg serva davvero a questo.''',
 20: '''Atterrate e trovate un Quarg che vi aspetta proprio sulla banchina. Vi consegna <payment> e vi ringrazia per l'aiuto.''',
 21: VALUE_2,
}

P2 = {
 22: DESC_CARGO,
 23: '''Nello spazioporto un gruppo di Quarg sta parlando con decine di capitani umani. Alcuni annuiscono e tornano subito alle loro navi, mentre pochi altri restano e sembrano discutere ancora un po' con i Quarg.''',
 24: '''(Unitevi a loro per vedere cosa succede.)''',
 25: '''(Ignorateli.)''',
 26: '''Vi unite al gruppo, e uno dei Quarg rivolge la sua attenzione a voi, mentre gli altri continuano a parlare con i mercanti umani.''',
 27: '''"Anche tu saresti qualcuno disposto a fornirci un servizio di trasporto merci, Capitano?" chiede, continuando intanto a controllare un datapad che sembra riguardare le navi attraccate qui. "Non molti di voi umani in questa regione hanno lo spazio di carico necessario, e ancor meno difese adeguate per i convogli merci. Siamo disposti a pagare adeguatamente chi soddisfa i criteri ed è disposto ad aiutarci."''',
 28: '''"Anche gli altri capitani lo stanno facendo? Perché vi serve tanto carico?"''',
 29: '''"Non cerco altri lavori di trasporto adesso, mi dispiace."''',
 30: '''"Molti hanno già accettato di aiutarci, ma ne servono molti altri. Quelli che hanno accettato sono diretti in parti diverse dello spazio umano, per portarci in sicurezza i materiali che abbiamo ordinato.''',
 31: '''"Il nostro mondo ad anello, in costruzione intorno alla stella di <system>, avrà presto una sezione speciale aperta ai visitatori umani. Vorremmo che lo stile e l'arredamento interno di quella sezione fossero più vicini agli standard umani, quindi chiediamo a ogni capitano capace di aiutarci. Tu sei uno di questi capitani: sei disposto ad aiutarci?"''',
 32: '''"Va bene, mi interessa. Dove devo andare a ritirare il carico?"''',
 33: '''"Mi dispiace, non cerco lavori di trasporto adesso, ero solo curioso."''',
 34: '''Armeggia ancora un po' con il datapad, poi dice: "Devi ritirare <cargo> su <stopovers>, poi consegnare quel carico su <destination>. Sarai pagato <payment> per il servizio. Stammi bene, umano."''',
 35: '''Vi fa un inchino con un gesto, poi si allontana a parlare con un altro capitano mercantile che è diventato curioso anche lui.''',
 36: LOADED,
 37: '''Proprio come la vostra nave, diversi altri mercantili umani e convogli stanno arrivando, e il carico viene meticolosamente controllato dai Quarg, che usano i propri macchinari per scaricare quello che devono essere decine di migliaia di tonnellate da tutte le navi.''',
 38: '''A metà circa dello scarico del vostro carico, un Quarg si avvicina e vi consegna <payment>.''',
 39: VALUE_2,
 40: DESC_CARGO,
 41: LOADED,
 42: '''A metà circa del meticoloso scarico del carico, un Quarg si avvicina e vi consegna <payment>.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
for idx, txt in list(P1.items()) + list(P2.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]), (idx, TAGS.findall(eng[idx]), TAGS.findall(txt))
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx
    if kind[idx] == 'VALUE':
        # riferimento di dato: nome di missione o di carico, resta identico
        assert txt == eng[idx], (idx, txt, eng[idx])
assert sorted(P1) == list(range(1, 22)) and sorted(P2) == list(range(22, 43))
assert [i for i in range(1, 43) if kind[i] == 'VALUE'] == [1, 21, 39]
assert [i for i in range(1, 43) if kind[i] == 'DESCRIPTION'] == [2, 22, 40]
assert [i for i in range(1, 43) if kind[i] == 'DIALOG'] == [16, 17, 18, 19, 20, 36, 41, 42]
assert P1[8] is P1[12] is HELP_WHERE and P1[10] is P1[13] is HEADED
assert P1[21] is P2[39] is VALUE_2 and P2[22] is P2[40] is DESC_CARGO and P2[36] is P2[41] is LOADED
assert eng[30].count('"') == 1 and P2[30].count('"') == 1

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (21 + 21)' % (len(P1) + len(P2)))
