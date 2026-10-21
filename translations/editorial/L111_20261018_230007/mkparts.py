"""mkparts.py — L111: costruisce `parts/part01-04.json` (104 unita', righe 16-328).

**104 `TUTORIAL_TIP`**, uno per contesto: le descrizioni dei pannelli di nave. Nessun token, nessun tab, nessuna
quadra, nessuna ripetizione.

Terminologia fissata **una volta** e usata in tutto il lotto:
mass=massa · acceleration=accelerazione · energy=energia · heat=calore · cooling=raffreddamento · fuel=carburante ·
hull=scafo · shield(s)=scudi/scudo · cloak/cloaking=occultamento/occultare · outfit=equipaggiamento ·
ton(ne)s=tonnellate · bunks=cuccette · crew=equipaggio (persone: «membri d'equipaggio»).

Tipi di danno: burn=bruciatura · corrosion=corrosione · discharge=scarica (scudi) · disruption=dirusione (scudi) ·
ion=ionizzazione · scramble=disturbo · leakage=perdita (carburante) · slowing=interferenza sui motori ·
force=forza d'urto · energy=energia · heat=calore.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

P1 = {
 1: '''(parcheggiata)''',
 2: '''Quanto in fretta questa nave acquista velocità. Più alta è la massa di una nave (compresa la massa del carico o dei caccia che trasporta), più lenta è la sua accelerazione.''',
 3: '''Modifica l'accelerazione della nave del fattore indicato.''',
 4: '''Raffreddamento fornito al secondo quando funziona a piena potenza. Il raffreddamento attivo consuma energia, ma se il livello di calore è basso funziona a una velocità di raffreddamento e con un consumo di energia inferiori. La quantità di raffreddamento è proporzionale alla temperatura della nave e raggiunge il livello massimo solo quando siete sul punto di surriscaldarvi.''',
 5: '''Energia consumata al secondo quando si usa questo postbruciatore.''',
 6: '''Danno agli scudi inflitto alla nave al secondo quando si usa questo postbruciatore.''',
 7: '''Danno allo scafo inflitto alla nave al secondo quando si usa questo postbruciatore.''',
 8: '''Carburante consumato al secondo quando si usa questo postbruciatore.''',
 9: '''Scarica accumulata sugli scudi al secondo quando si usa questo postbruciatore.''',
 10: '''Corrosione accumulata sullo scafo al secondo quando si usa questo postbruciatore.''',
 11: '''Ionizzazione accumulata al secondo quando si usa questo postbruciatore.''',
 12: '''Disturbo accumulato al secondo quando si usa questo postbruciatore.''',
 13: '''Perdita di carburante accumulata al secondo quando si usa questo postbruciatore.''',
 14: '''Interazioni esotermiche accumulate al secondo quando si usa questo postbruciatore.''',
 15: '''Interferenza sui motori accumulata al secondo quando si usa questo postbruciatore.''',
 16: '''Interferenza sugli scudi accumulata al secondo quando si usa questo postbruciatore.''',
 17: '''Calore creato al secondo quando si usa questo postbruciatore.''',
 18: '''Spinta prodotta da questo postbruciatore.''',
 19: '''Consente di scansionare gli asteroidi. La portata di questo scanner per asteroidi è proporzionale alla radice quadrata di questo valore.''',
 20: '''Questo tipo di scansione non può essere eseguito dalla vostra nave, ma questo equipaggiamento può essere utile in certe missioni.''',
 21: '''Una nave con questo attributo non richiede equipaggio per funzionare, anche se monta equipaggiamenti che normalmente richiedono personale aggiuntivo. In queste condizioni, però, non potete usarla come nave ammiraglia.''',
 22: '''Il numero di persone (passeggeri o membri d'equipaggio) che la vostra nave può ospitare.''',
 23: '''Protezione contro il danno da bruciatura. Aumenta del fattore indicato quanto danno da bruciatura una nave può sopportare prima che il suo calore salga quanto quello di una nave non protetta.''',
 24: '''Danno da bruciatura resistito al secondo.''',
 25: '''Energia consumata al secondo per resistere al danno da bruciatura.''',
 26: '''Carburante consumato al secondo per resistere al danno da bruciatura.''',
}

P2 = {
 27: '''Calore generato al secondo per resistere al danno da bruciatura.''',
 28: '''Aumenta la "forza" di un membro dell'equipaggio quando attacca un'altra nave per catturarla. Ogni membro dell'equipaggio può impugnare una sola arma alla volta, ma userà quella che garantisce la potenza maggiore.''',
 29: '''Aumenta la "forza" di un membro dell'equipaggio quando difende questa nave da un tentativo di cattura. Ogni membro dell'equipaggio può impugnare una sola arma alla volta, ma userà quella che garantisce la potenza maggiore.''',
 30: '''Tonnellate di carico che questa nave sta trasportando in questo momento, sul massimo disponibile.''',
 31: '''Consente di scansionare il carico della nave bersaglio fino a questa distanza.''',
 32: '''Consente di scansionare il carico della nave bersaglio. La portata di questo scanner per il carico è proporzionale alla radice quadrata di questo valore.''',
 33: '''Determina quanto tempo richiede una scansione del carico. Un valore più alto corrisponde a una scansione più rapida.''',
 34: '''La velocità massima di questo scanner per il carico è proporzionale alla radice quadrata di questo valore. La velocità di scansione osservata dipende da più fattori. I bersagli più lontani o con una stiva più grande richiedono più tempo.''',
 35: '''Aumenta il tempo necessario alle altre navi per scansionare il carico di questa nave. Un valore di uno ha lo stesso effetto sul tempo di una tonnellata in più di stiva da scansionare.''',
 36: '''Tonnellate di carico (merci, carico di missione ed equipaggiamenti saccheggiati) che questa nave può trasportare.''',
 37: '''Tonnellate di spazio per il carico occupate da questo equipaggiamento.''',
 38: '''Questo equipaggiamento permette alla vostra nave di occultarsi. Il valore indica quanto tempo serve per attivare o disattivare completamente l'occultamento. Le navi occultate non possono sparare, a meno che abbiano l'attributo "sparo in occultamento".''',
 39: '''Questo equipaggiamento permette alla vostra nave di occultarsi. Il valore indica quanto tempo serve per attivare o disattivare completamente l'occultamento su una nave di massa 1000. Più alta è la massa della nave, più lento è l'occultamento; più bassa è la massa, più rapido. Le navi occultate non possono sparare, a meno che abbiano l'attributo "sparo in occultamento".''',
 40: '''Energia consumata al secondo mentre si è occultati.''',
 41: '''Carburante consumato al secondo mentre si è occultati.''',
 42: '''Calore generato al secondo mentre si è occultati.''',
 43: '''Scudi consumati al secondo mentre si è occultati.''',
 44: '''Questa nave non può rigenerare gli scudi mentre è occultata; la rigenerazione degli scudi subisce invece un ritardo che cresce quanto più a lungo resta occultata.''',
 45: '''Scafo consumato al secondo mentre si è occultati.''',
 46: '''Questa nave non può rigenerare lo scafo mentre è occultata; la rigenerazione dello scafo subisce invece un ritardo che cresce quanto più a lungo resta occultata.''',
 47: '''Protezione contro le armi che infliggono danno allo scafo quando l'occultamento è attivo. Aumenta del fattore indicato quanto danno allo scafo una nave può sopportare prima di perdere tanta energia quanto una nave non protetta.''',
 48: '''Protezione contro le armi che infliggono danno agli scudi quando l'occultamento è attivo. Aumenta del fattore indicato quanto danno agli scudi una nave può sopportare prima di perdere tanta energia quanto una nave non protetta.''',
 49: '''Mentre è occultata, le armi non possono colpire questa nave e la attraversano.''',
 50: '''Questo dispositivo nasconde così bene la nave che potete sparare mentre vi occultate, perdendo in cambio questa quantità di occultamento, prima di essere di nuovo occultati. Un valore negativo significa che sparare non ostacola affatto il vostro occultamento.''',
 51: '''Se avete uno scafo inferiore a questo valore (espresso in % fra 0 e 1), il dispositivo di occultamento non può più funzionare.''',
 52: '''Calore dissipato al secondo. Serve quando la dissipazione di calore integrata della nave non basta a evitare il surriscaldamento.''',
}

P3 = {
 53: '''Energia consumata al secondo quando il raffreddamento attivo funziona a piena potenza (perché la temperatura della nave si avvicina alla soglia di surriscaldamento).''',
 54: '''Interferenza con la capacità di raffreddamento della nave. Con un'inefficienza di raffreddamento di 5 i sistemi di raffreddamento sono efficaci solo per circa il 75%, e per il 30% con un'inefficienza di 10.''',
 55: '''Protezione contro il danno da corrosione. Aumenta del fattore indicato quanto danno da corrosione una nave può sopportare prima di perdere tanto scafo quanto una nave non protetta.''',
 56: '''Danno da corrosione resistito al secondo.''',
 57: '''Energia consumata al secondo per resistere al danno da corrosione.''',
 58: '''Carburante consumato al secondo per resistere al danno da corrosione.''',
 59: '''Calore generato al secondo per resistere al danno da corrosione.''',
 60: '''Costo, in crediti. Se oggi avete venduto oggetti usati (deprezzati), potete ricomprarli allo stesso prezzo a cui li avete venduti.''',
 61: '''Quanto questa nave incide sulla capacità della vostra flotta. La nave ammiraglia e le scorte parcheggiate non contano. Potete superare la capacità mentre siete atterrati, ma non potrete partire se la superate.''',
 62: '''Protezione contro il danno da scarica agli scudi. Aumenta del fattore indicato quanto danno da scarica una nave può sopportare prima di perdere tanti scudi quanto una nave non protetta.''',
 63: '''Quanto danno da scarica agli scudi questa nave può resistere al secondo.''',
 64: '''Energia consumata al secondo per resistere al danno da scarica.''',
 65: '''Carburante consumato al secondo per resistere al danno da scarica.''',
 66: '''Calore generato al secondo per resistere al danno da scarica.''',
 67: '''Protezione contro il danno da disruzione degli scudi. Aumenta del fattore indicato quanto danno da disruzione una nave può sopportare prima che i suoi scudi siano disturbati quanto quelli di una nave non protetta.''',
 68: '''Danno da disruzione degli scudi resistito al secondo.''',
 69: '''Energia consumata al secondo per resistere al danno da disruzione.''',
 70: '''Carburante consumato al secondo per resistere al danno da disruzione.''',
 71: '''Calore generato al secondo per resistere al danno da disruzione.''',
 72: '''Limita la velocità massima di una nave.''',
 73: '''Riduce la resistenza. Aumenta del fattore indicato la velocità massima di una nave.''',
 74: '''Il numero di navi della categoria "Drone" che questa nave può trasportare.''',
 75: '''La quantità di energia che questo equipaggiamento aggiunge alla capacità energetica della nave. Vi permette di usare temporaneamente più potenza di quella prodotta dai generatori.''',
 76: '''Energia consumata al secondo in volo.''',
 77: '''Energia generata al secondo. Se la nave ha armi diverse da quelle a raggio, probabilmente vi serviranno anche batterie per accumulare energia.''',
 78: '''Tonnellate di spazio per i motori occupate da questo equipaggiamento.''',
}

P4 = {
 79: '''Tonnellate di motori che questa nave può ospitare. (Per installare un motore dovete anche avere spazio totale sufficiente per gli equipaggiamenti.)''',
 80: '''Protezione contro il danno da energia. Aumenta del fattore indicato quanto danno da energia una nave può sopportare prima di perdere tanta energia quanto una nave non protetta.''',
 81: '''Il numero di navi della categoria "Caccia" che questa nave può trasportare.''',
 82: '''La probabilità che questo equipaggiamento si stacchi come detrito quando la nave su cui è installato viene distrutta.''',
 83: '''Protezione contro la forza d'urto delle armi. Aumenta del fattore indicato quanta forza esterna una nave può sopportare prima di essere spostata quanto una nave non protetta.''',
 84: '''Il carburante attuale di questa nave. Un salto normale con iperguida consuma 100 di carburante.''',
 85: '''La quantità di carburante che questa nave può contenere. Un salto normale con iperguida consuma 100 di carburante. Il carburante si rifornisce gratis quando atterrate su un pianeta abitato.''',
 86: '''Carburante consumato al secondo in volo.''',
 87: '''Energia prodotta al secondo consumando carburante.''',
 88: '''Carburante generato al secondo.''',
 89: '''Calore prodotto al secondo consumando carburante.''',
 90: '''Protezione contro il danno al carburante. Aumenta del fattore indicato quanto danno al carburante una nave può sopportare prima di perdere tanto carburante quanto una nave non protetta.''',
 91: '''Quest'arma occupa un porto per cannoni. I cannoni sparano sempre dritto in avanti; le torrette sparano nella direzione del bersaglio selezionato.''',
 92: '''Quanti cannoni questa nave può ospitare. Comprende la maggior parte dei missili e delle armi secondarie che sparano dritto in avanti.''',
 93: '''Quanto efficacemente questa nave irradia il calore in eccesso.''',
 94: '''Calore generato al secondo. La generazione di calore può essere compensata dagli equipaggiamenti di "raffreddamento". Se la nave supera il calore massimo, deve spegnersi temporaneamente per raffreddarsi.''',
 95: '''Protezione contro il danno da calore. Aumenta del fattore indicato quanto danno da calore una nave può sopportare prima che il suo calore salga quanto quello di una nave non protetta.''',
 96: '''Aumenta il calore massimo che questa nave può sopportare prima di surriscaldarsi. Un valore di uno ha lo stesso effetto sul calore massimo di una tonnellata di massa, senza gli effetti che la massa ha sul movimento.''',
 97: '''Robustezza totale dello scafo e velocità di riparazione al secondo. Le navi più piccole vengono messe fuori uso quando la robustezza dello scafo scende sotto circa il 45%, mentre le navi molto grandi a circa il 10%.''',
 98: '''Robustezza totale dello scafo. Le navi con uno scafo più robusto possono subire più danni in proporzione alla propria robustezza totale prima di essere messe fuori uso; le navi più piccole vengono messe fuori uso quando la robustezza dello scafo scende sotto circa il 45%, mentre le navi molto grandi a circa il 10%.''',
 99: '''Energia consumata al secondo quando si ripara lo scafo.''',
 100: '''Energia aggiuntiva consumata al secondo quando si ripara lo scafo dopo il periodo di ritardo della riparazione.''',
 101: '''Modifica del fattore indicato l'energia consumata quando si ripara lo scafo.''',
 102: '''Carburante consumato al secondo quando si ripara lo scafo.''',
 103: '''Carburante aggiuntivo consumato al secondo quando si ripara lo scafo dopo il periodo di ritardo della riparazione.''',
 104: '''Modifica del fattore indicato il carburante consumato quando si ripara lo scafo.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
ALL = {}
for d in (P1, P2, P3, P4):
    ALL.update(d)
for idx, txt in ALL.items():
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]) == [], idx
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx
    assert kind[idx] == 'TUTORIAL_TIP', (idx, kind[idx])

assert sorted(P1) == list(range(1, 27)) and sorted(P2) == list(range(27, 53))
assert sorted(P3) == list(range(53, 79)) and sorted(P4) == list(range(79, 105))
assert len(ALL) == 104 == len({u['idx'] for u in src})
g = {}
for u in src:
    g.setdefault(u['english'], []).append(u['idx'])
assert not [v for v in g.values() if len(v) > 1], 'nessuna ripetizione attesa'
# terminologia: un termine, una resa — controllo su tutte le unita'
JOIN = ' '.join(ALL.values())
LOW = JOIN.lower()
for term in ('massa', 'accelerazione', 'energia', 'calore', 'raffreddamento', 'carburante',
             'scafo', 'scudi', 'occultamento', 'equipaggiamento', 'tonnellate'):
    assert term in LOW, term
for bad in ('massaia', 'shild', 'fuel ', 'hull ', 'cooling', 'cloak '):
    assert bad not in LOW, bad

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2), ('part03.json', P3), ('part04.json', P4)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (26 + 26 + 26 + 26)' % len(ALL))
