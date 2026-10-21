"""mkparts.py — L113: costruisce `parts/part01-03.json` (96 unita', righe 691-973).

**Tutte `PENDING`** (misurato: `{'PENDING': 96}`), asserito prima di scrivere.

**Novità strutturale**: i **contesti sono meno delle unità** — 87 contesti su 96 unità, con **nove contesti che
ne contengono due** (`turning`, `outfitter: b/s/i/u/c/r`, `shipyard: b`, `capacity`).

Registro del blocco approvato (L111): «tu» al giocatore, «danni da …» al plurale con «resistiti», «messa fuori
uso», «spazio equipaggiamenti/armi/motori», iperguida, ramscoop invariato.

Refuso del sorgente normalizzato e dichiarato: unità 4 «before it **as** slowed» → «prima di essere rallentata».
"""
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

T = {
 1: "Protezione contro i danni agli scudi. Aumenta del fattore indicato la quantità di danni agli scudi che una nave sopporta prima di perdere tanti scudi quanto una nave non protetta.",
 2: "Impedisce a una nave di produrre i suoni dell'iperguida o del motore di salto quando entra o esce da un sistema.",
 3: "Impedisce a una nave di emettere i suoni della scansione.",
 4: "Protezione contro i danni da interferenza sui motori. Aumenta del fattore indicato la quantità di danni da interferenza che una nave sopporta prima di essere rallentata quanto una nave non protetta.",
 5: "Danni da interferenza sui motori resistiti al secondo.",
 6: "Energia consumata al secondo per resistere ai danni da interferenza sui motori.",
 7: "Carburante consumato al secondo per resistere ai danni da interferenza sui motori.",
 8: "Calore generato al secondo per resistere ai danni da interferenza sui motori.",
 9: "Energia prodotta in base alla distanza di questa nave dalla stella al centro del sistema.",
 10: "Calore prodotto in base alla distanza di questa nave dalla stella al centro del sistema.",
 11: "Gli scanner strategici ti permettono di vedere, quando il bersaglio è a portata, la sua distanza da te, la portata massima dei cannoni, la portata massima delle torrette, la velocità attuale, l'accelerazione massima e la velocità di virata. La portata è proporzionale alla radice quadrata di questo valore.",
 12: "Gli scanner tattici ti permettono di vedere, quando il bersaglio è a portata, il suo equipaggio a bordo e i livelli di carburante, calore ed energia. La portata è proporzionale alla radice quadrata di questo valore.",
 13: "Gli scanner di mobilità ti permettono di vedere, quando il bersaglio è a portata, la sua accelerazione massima attuale. La portata è proporzionale alla radice quadrata di questo valore.",
 14: "Gli scanner dell'equipaggio ti permettono di vedere, quando il bersaglio è a portata, il suo equipaggio a bordo. La portata è proporzionale alla radice quadrata di questo valore.",
 15: "Gli scanner dell'energia ti permettono di vedere, quando il bersaglio è a portata, i suoi livelli di energia. La portata è proporzionale alla radice quadrata di questo valore.",
 16: "Gli scanner del carburante ti permettono di vedere, quando il bersaglio è a portata, i suoi livelli di carburante. La portata è proporzionale alla radice quadrata di questo valore.",
 17: "Gli scanner di manovra ti permettono di vedere, quando il bersaglio è a portata, la sua velocità di virata massima attuale. La portata è proporzionale alla radice quadrata di questo valore.",
 18: "Gli scanner di mobilità ti permettono di vedere, quando il bersaglio è a portata, la sua velocità attuale e la sua accelerazione massima. La portata è proporzionale alla radice quadrata di questo valore.",
 19: "I telemetri ti permettono di vedere la distanza dal centro della tua nave al centro del bersaglio attuale. Non c'è limite di portata.",
 20: "Gli scanner termici ti permettono di vedere, quando il bersaglio è a portata, il suo livello termico. La portata è proporzionale alla radice quadrata di questo valore.",
 21: "Gli scanner di mobilità ti permettono di vedere, quando il bersaglio è a portata, la sua velocità attuale. La portata è proporzionale alla radice quadrata di questo valore.",
 22: "Gli scanner delle armi ti permettono di vedere la portata massima delle armi del bersaglio quando è a portata di scansione. In particolare mostrano la portata maggiore fra tutte le armi di un alloggiamento per cannoni e la portata maggiore fra tutte le armi di un alloggiamento per torrette. Queste portate includono lo scostamento dell'arma e indicano quindi la distanza massima dal centro della nave che i colpi possono raggiungere. La portata dello scanner è proporzionale alla radice quadrata di questo valore.",
 23: "Spinta prodotta dai motori. Una spinta maggiore aumenta l'accelerazione e la velocità massima di una nave. Più massa ha una nave, più spinta serve per ottenere la stessa accelerazione.",
 24: "Energia consumata al secondo quando si attivano i propulsori.",
 25: "Calore generato al secondo quando si attivano i propulsori.",
 26: "Danni agli scudi inflitti alla nave al secondo quando si attivano i propulsori.",
 27: "Danni allo scafo inflitti alla nave al secondo quando si attivano i propulsori.",
 28: "Carburante consumato al secondo quando si attivano i propulsori.",
 29: "Scarica accumulata sugli scudi al secondo quando si attivano i propulsori.",
 30: "Corrosione accumulata sullo scafo al secondo quando si attivano i propulsori.",
 31: "Ionizzazione accumulata al secondo quando si attivano i propulsori.",
 32: "Disturbo accumulato al secondo quando si attivano i propulsori.",
 33: "Perdita di carburante accumulata al secondo quando si attivano i propulsori.",
 34: "Interazioni esotermiche accumulate al secondo quando si attivano i propulsori.",
 35: "Interferenza sui motori accumulata al secondo quando si attivano i propulsori.",
 36: "Interferenza sugli scudi accumulata al secondo quando si attivano i propulsori.",
 37: "Forza di virata prodotta dai motori. Più massa ha una nave, più forza di virata serve per ottenere la stessa velocità di virata.",
 38: "Velocità di virata, in gradi al secondo. Più alta è la massa di una nave (compresa la massa del carico o dei caccia che trasporta), più lenta è la virata.",
 39: "Modifica del fattore indicato la velocità di virata della nave.",
 40: "Energia consumata al secondo quando si vira.",
 41: "Calore generato al secondo quando si vira.",
 42: "Danni agli scudi inflitti alla nave al secondo quando si vira.",
 43: "Danni allo scafo inflitti alla nave al secondo quando si vira.",
 44: "Carburante consumato al secondo quando si vira.",
 45: "Scarica accumulata sugli scudi al secondo quando si vira.",
 46: "Corrosione accumulata sullo scafo al secondo quando si vira.",
 47: "Ionizzazione accumulata al secondo quando si vira.",
 48: "Disturbo accumulato al secondo quando si vira.",
 49: "Perdita di carburante accumulata al secondo quando si vira.",
 50: "Interazioni esotermiche accumulate al secondo quando si vira.",
 51: "Interferenza sui motori accumulata al secondo quando si vira.",
 52: "Interferenza sugli scudi accumulata al secondo quando si vira.",
 53: "Quest'arma può sparare in qualsiasi direzione, seguendo il bersaglio attualmente selezionato. Occupa uno degli alloggiamenti per torrette della tua nave.",
 54: "Quante torrette possono essere montate su questa nave. Le torrette sparano nella direzione del bersaglio attualmente selezionato, invece di sparare dritto in avanti come i cannoni.",
 55: "Tonnellate di spazio armi occupate da questo equipaggiamento.",
 56: "Tonnellate di armi che questa nave può ospitare. (Per installare un'arma devi anche avere spazio totale sufficiente per gli equipaggiamenti.)",
 57: "Modifica la probabilità che questo equipaggiamento illegale compaia in una scansione del carico. Più alta è la visibilità, più è probabile che una scansione lo rilevi. Una visibilità di 5 ha la stessa probabilità di essere scansionata di un equipaggiamento da 5 tonnellate.",
 58: "Nasconde una massa equivalente di carico illegale alle scansioni del carico, evitandoti la multa. Un occultamento di 10 farebbe sì che fino a 10 tonnellate di carico illegale non compaiano nelle scansioni del carico.",
 59: "Acquista dall'emporio e installa sulla nave selezionata (o sulle navi selezionate).",
 60: "Tieni premuto Shift, Control o Alt per acquistare 5, 20 o 500 equipaggiamenti alla volta. Tieni premuta una combinazione di questi tasti per quantità maggiori.",
 61: "Vendi dal carico, dal deposito o dalla nave selezionata (o dalle navi selezionate), in quest'ordine.",
 62: "Tieni premuto Shift, Control o Alt per vendere 5, 20 o 500 equipaggiamenti alla volta. Tieni premuta una combinazione di questi tasti per quantità maggiori.",
 63: "Installa sulla nave selezionata (o sulle navi selezionate) prendendo dal carico o dal deposito, in quest'ordine.",
 64: "Tieni premuto Shift, Control o Alt per installare 5, 20 o 500 equipaggiamenti alla volta. Tieni premuta una combinazione di questi tasti per quantità maggiori.",
 65: "Disinstalla dalla nave selezionata (o dalle navi selezionate) verso il carico se c'è spazio, altrimenti verso il deposito.",
 66: "Tieni premuto Shift, Control o Alt per disinstallare 5, 20 o 500 equipaggiamenti alla volta. Tieni premuta una combinazione di questi tasti per quantità maggiori.",
 67: "Trasferisci l'equipaggiamento dal deposito planetario al carico se possibile. Altrimenti acquistalo dall'emporio.",
 68: "Tieni premuto Shift, Control o Alt per spostare 5, 20 o 500 equipaggiamenti alla volta. Tieni premuta una combinazione di questi tasti per quantità maggiori.",
 69: "Sposta l'equipaggiamento dal carico, dalla nave selezionata (o dalle navi selezionate) o dall'emporio al deposito planetario, in quest'ordine.",
 70: "Tieni premuto Shift, Control o Alt per immagazzinare 5, 20 o 500 equipaggiamenti alla volta. Tieni premuta una combinazione di questi tasti per quantità maggiori.",
 71: "Acquista questa nave.",
 72: "Tieni premuto Shift, Control o Alt per acquistare 5, 20 o 500 navi alla volta. Tieni premuta una combinazione di questi tasti per quantità maggiori.",
 73: "Vendi le navi selezionate e i loro equipaggiamenti.",
 74: "Vendi gli scafi delle navi selezionate, ma conserva gli equipaggiamenti nel deposito.",
 75: "Il prezzo a cui si venderebbe la nave stessa senza equipaggiamenti installati.",
 76: "Il prezzo a cui si venderebbero tutti gli equipaggiamenti di questa nave.",
 77: "Energia e calore generati al secondo quando questa nave è inattiva, cioè non spara, non si muove e non usa altri sistemi.",
 78: "Energia consumata e calore generato al secondo quando questa nave vira e spinge. Comprende il costo del postbruciatore, se installato, oppure il costo della spinta inversa se è maggiore del costo della spinta in avanti. Si somma alla quantità \"inattiva\".",
 79: "Energia consumata e calore generato al secondo quando questa nave spinge. Si somma alla quantità \"inattiva\".",
 80: "Energia consumata e calore generato al secondo quando questa nave usa i propulsori di spinta inversa. Si somma alla quantità \"inattiva\".",
 81: "Energia consumata e calore generato al secondo quando questa nave usa il postbruciatore. Si somma alla quantità \"inattiva\".",
 82: "Energia consumata e calore generato al secondo quando questa nave vira. Si somma alla quantità \"inattiva\".",
 83: "Energia consumata e calore generato al secondo quando questa nave spara con tutte le armi. Si somma alla quantità \"inattiva\". Nota che le armi possono consumare o generare più energia o calore nell'istante in cui sparano: questo è il valore medio nel tempo.",
 84: "Energia consumata e calore generato al secondo quando questa nave ricarica gli scudi e ripara lo scafo nello stesso momento. Si somma alla quantità \"inattiva\".",
 85: "Energia consumata e calore generato al secondo quando questa nave ripara lo scafo. Si somma alla quantità \"inattiva\".",
 86: "Energia consumata e calore generato al secondo quando questa nave ricarica gli scudi. Si somma alla quantità \"inattiva\".",
 87: "La somma dell'energia consumata e del calore generato al secondo dai valori di energia e calore qui sopra. Rappresenta il caso peggiore, con tutti i sistemi possibili attivi contemporaneamente.",
 88: "La capacità energetica permette a una nave di prelevare temporaneamente più energia di quanta ne produca, e può essere aumentata installando batterie.",
 89: "La capacità termica è il livello massimo a cui la generazione di calore può arrivare senza che la nave finisca per surriscaldarsi, ed è influenzata dalla massa della nave. Se il valore di \"variazione netta\" del calore supera questo valore, la nave può surriscaldarsi. Le armi con un alto calore per colpo possono surriscaldarti anche se la \"variazione netta\" resta sotto la capacità termica.",
 90: "Questa nave non ha accumulo di energia. Questo è quindi il massimo di energia che qualunque sistema della nave può prelevare in un solo istante, come l'energia richiesta per un singolo colpo di un'arma. I sistemi che richiedono più di questa energia per attivarsi saranno inutilizzabili.",
 91: "Armi fissate alla nave (sparano nella direzione in cui punta la nave) e che non richiedono munizioni.",
 92: "Armi che possono sparare in qualsiasi direzione e seguono il bersaglio attualmente selezionato.",
 93: "Armi che richiedono munizioni (da acquistare separatamente).",
 94: "Equipaggiamenti che servono da munizioni per altre armi. Per sparare queste munizioni serve un lanciatore del tipo adatto.",
 95: "Equipaggiamenti che occupano spazio generico, non lo spazio riservato ai motori o alle armi.",
 96: "Equipaggiamenti che forniscono energia o accumulano l'energia generata.",
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
CTX = {u['idx']: u['context'] for u in src}
TAGS = re.compile(r'<[^<>]+>')

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
states = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in src}
assert set(states.values()) == {'PENDING'}, {k: v for k, v in states.items() if v != 'PENDING'}

assert sorted(T) == list(range(1, 97)) == sorted(eng), (len(T), len(eng))
for idx, txt in T.items():
    assert '\t' not in txt, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]) == [], idx
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip() and txt.strip() != eng[idx].strip(), idx
    assert kind[idx] == 'TUTORIAL_TIP', (idx, kind[idx])
    assert not re.search(r'\b(avete|potete|potrete|siete|vostro|vostra|vostri|vostre)\b', txt), (idx, txt)

# --- contesti: 87 distinti, nove con due unita' -------------------------------------------
seen = {}
for u in src:
    seen.setdefault(u['context'], []).append(u['idx'])
double = sorted(k for k, v in seen.items() if len(v) == 2)
assert len(seen) == 87, len(seen)
assert len(double) == 9, double
assert sorted(v for k, v in seen.items() if len(v) == 2) == [
    [38, 82], [59, 60], [61, 62], [63, 64], [65, 66], [67, 68], [69, 70], [71, 72], [88, 89]]

g = {}
for u in src:
    g.setdefault(u['english'], []).append(u['idx'])
assert not [v for v in g.values() if len(v) > 1], 'nessuna ripetizione attesa'

os.makedirs(OUT, exist_ok=True)
for n in range(3):
    lo, hi = 1 + 32 * n, 32 + 32 * n
    d = {k: T[k] for k in range(lo, hi + 1)}
    assert len(d) == 32
    with open(os.path.join(OUT, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte 96 unita (32 x 3) · 87 contesti · 9 contesti doppi · tutte PENDING')
