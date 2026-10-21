"""mkparts.py — L106: costruisce `parts/part01-02.json` (25 unita', righe 1-120).

Primo lotto di `korath missions.txt`. **Quattro tipi**: 22 `MISSION_TEXT`, 1 `LOGBOOK` (unita' 5: scheda dei
Korath), 1 `VALUE` (unita' 6: `Supplies to <planet>`, nome di missione — **identico**), 1 `DESCRIPTION` (unita'
7, tradotta).

**Le quadre sono la voce dei Wanderer**: sedici coppie nelle unita' 11 (3), 16 (7), 17 (1), 20 (4), 25 (1). Il
dispositivo di traduzione elenca **due rese possibili** dello stesso concetto, perche' la lingua dei Wanderer non
ha un equivalente diretto. Si traducono **entrambe** e la struttura resta: `[sollevato, felice]`.

**Una citazione aperta** (unita' 16). **Due ripetizioni**: 2/3/4 e 15/19.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

GREETING = '''Alcuni dei Korath in questo spazioporto vi salutano quando atterrate, sollevando entrambe le mani con i palmi verso di voi. Uno di loro dice qualcosa che suona come: "Humani efreti, naskoor amasavarkta." È chiaro che nessuno di loro parla la vostra lingua, ma sembrano amichevoli e disposti a commerciare con voi.'''
BUSY = '''"Mi dispiace, ma al momento sono troppo impegnato per prendere un altro lavoro."'''

P1 = {
 1: '''Alcuni dei Korath che abitano questa stazione vi salutano quando atterrate, sollevando entrambe le mani con i palmi verso di voi. Uno di loro dice qualcosa che suona come: "Humani efreti, naskoor amasavarkta." È chiaro che nessuno di loro parla la vostra lingua, ma sembrano amichevoli e disposti a commerciare con voi.''',
 2: GREETING,
 3: GREETING,
 4: GREETING,
 5: '''I Korath sono alieni rettiliani e bipedi, il cui territorio è quasi interamente in rovina: città distrutte e interi pianeti segnati da quella che sembra essere stata una feroce guerra civile. Sopravvivono diverse fazioni di Korath. I "Kor Efreti" vivono al riparo di un mondo ad anello dei Quarg e sono in rapporti pacifici con loro. Altri Korath, che vivono in esilio vicino al nucleo galattico, hanno saccheggiato i mondi umani per rubare cibo e provviste. E più in profondità nello spazio Korath, due enormi eserciti di droni da guerra automatici, noti come Kor Mereti e Kor Sestor, sono bloccati in una lotta senza fine. Attaccano chiunque visiti la loro regione di spazio, compresi i Quarg.''',
 6: '''Supplies to <planet>''',
 7: '''Porta <cargo> dai Wanderer ai Kor Efreti su <destination>. Il pagamento è <payment>.''',
 8: '''Mentre esplorate lo spazioporto, un Wanderer che non avete mai incontrato vi fa cenno di fermarvi. Dice: "Lei è il Capitano <last>, giusto?"''',
 9: '''"Sì, sono io."''',
 10: '''"L'unico e solo."''',
 11: '''"Sono [sollevato, felice] di vederla, Capitano. Abbiamo sentito del suo aiuto nella nostra migrazione qui, e [credo, suppongo] che abbia passato un po' di tempo sui mondi Korath. Le interesserebbe portare <tons> di [provviste, aiuti] su <planet>? Posso offrirle <payment>."''',
 12: '''"Posso farlo. Caricate, e sarò pronto a partire."''',
 13: '''"Solo <payment>? È un pagamento insolitamente basso per la quantità di carico che trasporterò."''',
}

P2 = {
 14: '''"Che cosa trasporterei esattamente?"''',
 15: BUSY,
 16: '''"Come di certo saprà, <planet> è freddo - scomodamente freddo per la maggior parte delle specie. In base alle nostre [ricerche, informazioni], il pianeta sta vivendo una [discesa, transizione] accelerata verso un'era glaciale. I Kor Efreti non hanno mezzi efficaci per fermarla, e il loro [orgoglio, onore] fa sì che non accetteranno il nostro aiuto nella terraformazione finché non avranno altre opzioni. Ci pagheranno però per attrezzature che compensino questa [discesa, transizione]. Le sue [provviste, aiuti] includerebbero indumenti più caldi, materiale per costruire serre, [isolamento, ripari] e altra tecnologia che i Korath potranno usare. Il pagamento, per quanto [purtroppo, tristemente] basso, è tutto ciò che i Korath sono riusciti a offrire.''',
 17: '''"Avevo intenzione di fare il viaggio io stesso, ma la mia nave ha avuto [errori, complicazioni] per un componente difettoso. Ho bisogno di qualcuno che vada al mio posto."''',
 18: '''"Ne sarei felice, soprattutto perché è per una buona causa. Può caricare sulla mia nave."''',
 19: BUSY,
 20: '''Il Wanderer ha un leggero sussulto, quasi avesse sperato che non lo chiedeste. "Beh... sì, è basso. Il resto del pagamento dei Kor Efreti è stato usato per [comprare, acquisire] le provviste, e sembra che non potessero permettersi di pagare molto più di quanto avessero già fatto. Vista la loro situazione, abbiamo trovato [ragionevole, giustificabile] accettare il pagamento più basso, dato che il carico è una [collezione, accozzaglia] di attrezzature per aiutare con il clima che si raffredda su <planet>, e senza di esso i Kor Efreti potrebbero... [perire? spegnersi?]."''',
 21: '''"Capisco, e i soldi non sono un problema enorme. Ero solo curioso. Caricate sulla mia nave, e sarò pronto a partire."''',
 22: '''"Oh. Beh, farò un'eccezione anch'io. Caricate, e parto."''',
 23: '''"Mi dispiace, ma non posso fare quel viaggio per soli <payment>. Dovrete trovare qualcun altro."''',
 24: '''Il Wanderer si sgonfia un po' quando sente la vostra risposta. "Oh. Capisco. Grazie del tempo, Capitano <last>," dice, poi si allontana in cerca di un altro pilota.''',
 25: '''Il Wanderer è felice di sentire la vostra risposta. "Meraviglioso! Farò in modo che le provviste siano caricate sulla vostra nave [subito, in fretta]. Grazie, Capitano." Si affretta verso un gruppo di Wanderer lì vicino e comincia a impartire ordini. Il gruppo si separa, e nel giro di pochi minuti sono alla vostra nave a caricare le provviste.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
ALL = {}
for d in (P1, P2):
    ALL.update(d)
BR = {11: 3, 16: 7, 17: 1, 20: 4, 25: 1}
for idx, txt in ALL.items():
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]), (idx, TAGS.findall(eng[idx]), TAGS.findall(txt))
    # le quadre: una coppia per alternativa, tante quante nel sorgente
    assert txt.count('[') == eng[idx].count('[') and txt.count(']') == eng[idx].count(']'), (
        idx, eng[idx].count('['), txt.count('['))
    assert txt.strip(), idx
    if kind[idx] == 'VALUE':
        # nome di missione, con un token dentro: resta identico
        assert txt == eng[idx], (idx, txt, eng[idx])
assert sorted(P1) == list(range(1, 14)) and sorted(P2) == list(range(14, 26))
assert [i for i in range(1, 26) if kind[i] == 'VALUE'] == [6]
assert [i for i in range(1, 26) if kind[i] == 'DESCRIPTION'] == [7]
assert [i for i in range(1, 26) if kind[i] == 'LOGBOOK'] == [5]
assert eng[5] != P1[5] and len(P1[5]) > 400, 'il LOGBOOK va tradotto per intero'
assert [i for i in range(1, 26) if eng[i].count('[')] == [11, 16, 17, 20, 25]
assert {i: ALL[i].count('[') for i in BR} == BR
assert P1[2] is P1[3] is P1[4] is GREETING and P2[15] is P2[19] is BUSY
assert [i for i in range(1, 26) if eng[i].count('"') % 2] == [16]
assert not P2[16].rstrip().endswith('"')
# le quadre contengono due alternative, non una parola sola
for i in BR:
    for frag in re.findall(r'\[([^\]]*)\]', ALL[i]):
        assert ',' in frag or '?' in frag, (i, frag)

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (13 + 12)' % len(ALL))
