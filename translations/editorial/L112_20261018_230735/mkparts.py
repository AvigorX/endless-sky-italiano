"""mkparts.py — L112: costruisce `parts/part01-04.json` (120 unita', righe 331-688).

**Tutte `PENDING`**: misurato prima di scrivere (`select state ... group by state`), non assunto — le 52 unita'
approvate del file stanno tutte fra le righe 16 e 172. Se una sola unita' risultasse `APPROVED` lo script
abortisce: in quel caso si riproduce alla lettera dal database (vedi `L111/mkparts2.py`).

Registro **fissato dal blocco approvato** (L111): «tu» al giocatore, «danni da …» al plurale con participio
concordato («resistiti»), «ammiraglia», «messa fuori uso», «ustione» (non «bruciatura»), «spazio equipaggiamenti» /
«spazio motori», iperguida per *hyperdrive*.
"""
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

T = {
 1: "Calore prodotto al secondo quando si ripara lo scafo.",
 2: "Calore aggiuntivo prodotto al secondo quando si ripara lo scafo dopo il periodo di ritardo della riparazione.",
 3: "Modifica del fattore indicato il calore prodotto quando si ripara lo scafo.",
 4: "Modifica del fattore indicato la robustezza totale dello scafo della nave.",
 5: "Quantità di robustezza dello scafo riparabile al secondo. Le riparazioni di solito consumano energia e possono generare calore.",
 6: "Robustezza dello scafo aggiuntiva riparabile al secondo dopo il periodo di ritardo della riparazione.",
 7: "Il numero di secondi necessari perché inizino riparazioni aggiuntive dello scafo dopo aver subito danni allo scafo.",
 8: "Il numero di secondi necessari perché inizino le riparazioni dello scafo dopo essere stati messi fuori uso.",
 9: "Il numero di secondi necessari perché una nave messa fuori uso si ripari da sola.",
 10: "Il costo in energia necessario perché una nave messa fuori uso si ripari da sola.",
 11: "Il costo in carburante necessario perché una nave messa fuori uso si ripari da sola.",
 12: "Il calore applicato quando una nave messa fuori uso si ripara da sola.",
 13: "I danni da ionizzazione applicati quando una nave messa fuori uso si ripara da sola.",
 14: "I danni da disturbo applicati quando una nave messa fuori uso si ripara da sola.",
 15: "I danni da disruzione applicati quando una nave messa fuori uso si ripara da sola.",
 16: "I danni da interferenza sui motori applicati quando una nave messa fuori uso si ripara da sola.",
 17: "I danni da scarica applicati quando una nave messa fuori uso si ripara da sola.",
 18: "I danni da corrosione applicati quando una nave messa fuori uso si ripara da sola.",
 19: "I danni da perdita di carburante applicati quando una nave messa fuori uso si ripara da sola.",
 20: "I danni da ustione applicati quando una nave messa fuori uso si ripara da sola.",
 21: "La robustezza dello scafo residua alla quale la nave viene messa fuori uso. Questo attributo ha la precedenza sugli altri attributi che modificano la soglia di messa fuori uso.",
 22: "Modifica il valore di robustezza dello scafo al quale la nave viene messa fuori uso.",
 23: "Modifica la percentuale di robustezza dello scafo residua alla quale la nave viene messa fuori uso.",
 24: "Protezione contro i danni diretti allo scafo. Aumenta del fattore indicato la quantità di danni allo scafo che la nave sopporta prima di perdere tanto scafo quanto una nave non protetta.",
 25: "Modifica del fattore indicato la quantità di robustezza dello scafo riparata al secondo.",
 26: "Modifica del fattore indicato la quantità di robustezza dello scafo riparata al secondo mentre un dispositivo di occultamento è attivo.",
 27: "Quantità di crediti per cui puoi essere multato se trasporti questo equipaggiamento.",
 28: "Crediti ricevuti al giorno quando possiedi questo equipaggiamento, anche se non è in uso attivo.",
 29: "Riduce la massa effettiva della nave. Aumenta del fattore indicato la rapidità con cui la nave accelera.",
 30: "Protezione contro i danni da ionizzazione. Modifica del fattore indicato la quantità di danni da ionizzazione che la nave sopporta prima di perdere tanta energia quanto una nave non protetta.",
 31: "Protezione contro i danni da disturbo delle armi. Aumenta del fattore indicato la quantità di danni da disturbo che la nave sopporta prima che le sue armi siano disturbate quanto quelle di una nave non protetta.",
 32: "Danni da ionizzazione resistiti al secondo.",
 33: "Energia consumata al secondo per resistere ai danni da ionizzazione.",
 34: "Carburante consumato al secondo per resistere ai danni da ionizzazione.",
 35: "Calore generato al secondo per resistere ai danni da ionizzazione.",
 36: "Velocità con cui questa nave sembra atterrare o attraversare un wormhole.",
 37: "Danni da disturbo resistiti al secondo.",
 38: "Energia consumata al secondo per resistere ai danni da disturbo.",
 39: "Carburante consumato al secondo per resistere ai danni da disturbo.",
 40: "Calore generato al secondo per resistere ai danni da disturbo.",
 41: "La velocità massima alla quale la nave può saltare.",
 42: "Carburante consumato quando si salta fra sistemi con questa iperguida.",
 43: "Carburante consumato quando si salta fra sistemi con questo motore di salto.",
 44: "La distanza massima alla quale questo motore può saltare.",
 45: "Carburante consumato ogni 100 tonnellate di massa quando si salta. Si somma al carburante del salto.",
 46: "Modifica l'effetto della massa della nave sul costo di massa del salto. Le navi sotto questa massa hanno un costo di salto inferiore a quello base, mentre quelle sopra hanno salti più costosi.",
 47: "Protezione contro i danni da perdita di carburante. Aumenta del fattore indicato la quantità di danni da perdita che la nave sopporta prima di perdere tanto carburante quanto una nave non protetta.",
 48: "Danni da perdita di carburante resistiti al secondo.",
 49: "Energia consumata al secondo per resistere ai danni da perdita di carburante.",
 50: "Carburante consumato al secondo per resistere ai danni da perdita di carburante.",
 51: "Calore generato al secondo per resistere ai danni da perdita di carburante.",
 52: "Crediti spesi al giorno per mantenere questo equipaggiamento. Anche se una nave è parcheggiata o un equipaggiamento è nel carico, devi comunque pagarne la manutenzione.",
 53: "Il numero di sistemi stellari inclusi in questa mappa.",
 54: "Massa di questa nave quando non trasporta carico né caccia. Il carico aumenta la massa, il che riduce l'accelerazione e la velocità di virata e aumenta il calore massimo prima del surriscaldamento.",
 55: "Massa, in tonnellate. La massa di una nave determina la rapidità con cui vira e accelera e il suo calore massimo prima del surriscaldamento.",
 56: "La velocità massima di questa nave usando i propulsori. Esclude l'effetto dei postbruciatori, a meno che non siano installati propulsori normali.",
 57: "Movimento quando sono attivi sia i propulsori principali sia i postbruciatori.",
 58: "Quanto rapidamente questa nave può accelerare e virare.",
 59: "Quanto rapidamente questa nave può accelerare e virare con la stiva piena rispetto a quando è vuota.",
 60: "Crediti spesi al giorno per mantenere questo equipaggiamento quando è in uso attivo.",
 61: "Crediti ricevuti al giorno quando questo equipaggiamento è in uso attivo.",
 62: "Consente la scansione degli equipaggiamenti della nave bersaglio fino a questa distanza.",
 63: "Consente la scansione degli equipaggiamenti della nave bersaglio. La portata di questo scanner è proporzionale alla radice quadrata di questo valore.",
 64: "Determina quanto tempo richiede una scansione degli equipaggiamenti. Un valore più alto corrisponde a una scansione più rapida.",
 65: "La velocità massima di questo scanner è proporzionale alla radice quadrata di questo valore. La velocità di scansione osservata dipende da più fattori: i bersagli più lontani o con più spazio per gli equipaggiamenti richiedono più tempo.",
 66: "Aumenta il tempo necessario alle altre navi per scansionare gli equipaggiamenti di questa nave. Un valore di uno ha lo stesso effetto sul tempo di una tonnellata in più di spazio equipaggiamenti da scansionare.",
 67: "Tonnellate di spazio generico fornite da questo equipaggiamento.",
 68: "Tonnellate di spazio generico occupate da questo equipaggiamento. Alcuni equipaggiamenti occupano anche spazio armi o spazio motori.",
 69: "Tonnellate di spazio di cui questa nave dispone per gli equipaggiamenti (armi e motori compresi).",
 70: "Danni allo scafo subiti al secondo quando si è surriscaldati. I danni da surriscaldamento crescono quanto più la nave supera la soglia di surriscaldamento.",
 71: "Aumenta la percentuale oltre il surriscaldamento alla quale iniziano i danni da surriscaldamento.",
 72: "Riduce la capacità dei missili a guida ottica di seguire la tua nave, cosa utile soprattutto alle navi grandi. Più disturbo ottico è installato, maggiore è la distanza alla quale i missili possono essere disturbati e maggiore la probabilità che un missile disturbato parta in una direzione casuale.",
 73: "Influenza la forza di tracciamento dei missili a guida ottica che puntano questa nave. Un valore più alto significa che la nave è più facile da seguire.",
 74: "Percentuale dei danni di questa arma che passa fino allo scafo mentre gli scudi del bersaglio sono ancora attivi.",
 75: "Protezione contro le armi perforanti. Aumenta del fattore indicato la perforazione necessaria perché la stessa porzione di danni oltrepassi gli scudi di una nave.",
 76: "Danni da perforazione resistiti su tutti i proiettili in arrivo, impedendo ai danni di passare dagli scudi allo scafo.",
 77: "Riduce la capacità dei missili a guida radar di seguire la tua nave. Più disturbo radar è installato, maggiore è la distanza alla quale i missili possono essere disturbati e maggiore la probabilità che un missile disturbato parta in una direzione casuale.",
 78: "Rifornisce carburante raccogliendo il vento stellare. I ramscoop sono più efficaci vicino a una stella. Se ne installi più di uno, ogni successivo è meno efficace: servono quattro ramscoop per ottenere il doppio della velocità di ricarica di uno solo.",
 79: "Membri dell'equipaggio necessari per far funzionare questa nave, e numero totale di cuccette disponibili. Le cuccette in più servono per passeggeri o equipaggio aggiuntivo.",
 80: "Cambia di questa quantità il numero di membri dell'equipaggio richiesti da questa nave.",
 81: "Cambia di questa quantità il numero di membri dell'equipaggio richiesti da questa nave. L'equipaggio obbligatorio non può essere sostituito dall'automazione.",
 82: "Spinta inversa generata dai motori. La spinta inversa permette a una nave di rallentare senza doversi girare.",
 83: "Energia consumata al secondo quando si attivano i propulsori di spinta inversa.",
 84: "Calore prodotto al secondo quando si attivano i propulsori di spinta inversa.",
 85: "Danni agli scudi inflitti alla nave al secondo quando si attivano i propulsori di spinta inversa.",
 86: "Danni allo scafo inflitti alla nave al secondo quando si attivano i propulsori di spinta inversa.",
 87: "Carburante consumato al secondo quando si attivano i propulsori di spinta inversa.",
 88: "Scarica accumulata sugli scudi al secondo quando si attivano i propulsori di spinta inversa.",
 89: "Corrosione accumulata sullo scafo al secondo quando si attivano i propulsori di spinta inversa.",
 90: "Ionizzazione accumulata al secondo quando si attivano i propulsori di spinta inversa.",
 91: "Disturbo accumulato al secondo quando si attivano i propulsori di spinta inversa.",
 92: "Perdita di carburante accumulata al secondo quando si attivano i propulsori di spinta inversa.",
 93: "Interazioni esotermiche accumulate al secondo quando si attivano i propulsori di spinta inversa.",
 94: "Interferenza sui motori accumulata al secondo quando si attivano i propulsori di spinta inversa.",
 95: "Interferenza sugli scudi accumulata al secondo quando si attivano i propulsori di spinta inversa.",
 96: "Capacità di sfuggire al rilevamento quando una nave trasporta equipaggiamenti o carico illegali. Un'interferenza di 1 blocca il 50% dei tentativi di scansione; 3 ne blocca il 75% e 9 il 90%.",
 97: "Ti permette di saltare senza fermarti, purché la tua velocità rientri in questo margine di allineamento con la direzione del salto.",
 98: "La probabilità che questa nave si autodistrugga quando provi ad abbordarla o a catturarla.",
 99: "Quanto vale questo equipaggiamento alla vendita, in crediti. Equipaggiamenti e navi si deprezzano (perdono valore di rivendita) col tempo, e il bottino parte sempre completamente deprezzato.",
 100: "Energia consumata al secondo quando si ricaricano gli scudi.",
 101: "Energia aggiuntiva consumata al secondo quando si ricaricano gli scudi dopo il periodo di ritardo degli scudi.",
 102: "Modifica del fattore indicato l'energia consumata quando si ricaricano gli scudi.",
 103: "Carburante consumato al secondo quando si ricaricano gli scudi.",
 104: "Carburante aggiuntivo consumato al secondo quando si ricaricano gli scudi dopo il periodo di ritardo degli scudi.",
 105: "Modifica del fattore indicato il carburante consumato quando si ricaricano gli scudi.",
 106: "Calore prodotto al secondo quando si ricaricano gli scudi.",
 107: "Calore aggiuntivo prodotto al secondo quando si ricaricano gli scudi dopo il periodo di ritardo degli scudi.",
 108: "Modifica del fattore indicato il calore prodotto quando si ricaricano gli scudi.",
 109: "Punti scudo ricaricati al secondo. Ricaricare gli scudi di solito consuma energia e può anche produrre calore.",
 110: "Punti scudo aggiuntivi ricaricati al secondo dopo il periodo di ritardo degli scudi.",
 111: "Modifica del fattore indicato la quantità di punti scudo ricaricati al secondo.",
 112: "Modifica del fattore indicato la quantità di punti scudo ricaricati al secondo mentre un dispositivo di occultamento è attivo.",
 113: "Questa percentuale di tutti i danni in arrivo oltrepassa gli scudi e colpisce direttamente lo scafo quando gli scudi sono al massimo.",
 114: "Questa percentuale di tutti i danni in arrivo oltrepassa gli scudi e colpisce direttamente lo scafo man mano che gli scudi si avvicinano a zero.",
 115: "Questa percentuale di tutti i danni in arrivo oltrepassa gli scudi e colpisce direttamente lo scafo mentre sei occultato.",
 116: "Robustezza totale degli scudi e velocità di rigenerazione al secondo.",
 117: "Robustezza totale degli scudi. La maggior parte delle armi non può danneggiare il tuo scafo finché gli scudi non sono esauriti. Alcuni effetti, come i danni da calore, diventano più gravi quando gli scudi sono abbassati.",
 118: "Modifica del fattore indicato la robustezza totale degli scudi della nave.",
 119: "Il numero di secondi necessari perché inizi una rigenerazione aggiuntiva degli scudi dopo aver subito danni agli scudi.",
 120: "Il numero di secondi necessari perché inizi una rigenerazione aggiuntiva degli scudi dopo che gli scudi sono stati esauriti.",
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
states = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in src}
assert set(states.values()) == {'PENDING'}, {k: v for k, v in states.items() if v != 'PENDING'}

assert sorted(T) == list(range(1, 121)) == sorted(eng), (len(T), len(eng))
for idx, txt in T.items():
    assert '\t' not in txt, idx
    assert txt.count('"') == eng[idx].count('"') == 0, (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]) == [], idx
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip() and txt.strip() != eng[idx].strip(), idx
    assert kind[idx] == 'TUTORIAL_TIP', (idx, kind[idx])
    assert not re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b', txt), (idx, txt)

g = {}
for u in src:
    g.setdefault(u['english'], []).append(u['idx'])
assert not [v for v in g.values() if len(v) > 1], 'nessuna ripetizione attesa'

os.makedirs(OUT, exist_ok=True)
for n in range(4):
    lo, hi = 1 + 30 * n, 30 + 30 * n
    d = {k: T[k] for k in range(lo, hi + 1)}
    assert len(d) == 30
    with open(os.path.join(OUT, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (30 x 4), tutte PENDING, 0 approvate' % len(T))
