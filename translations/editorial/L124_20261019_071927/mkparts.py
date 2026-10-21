"""mkparts.py — L124: secondo segmento di `data/human/ships.txt` (29 unita', righe 2102-3422).

Forma piu' leggera di L123: **28 `DESCRIPTION`** e **1 `VALUE`**, **24 contesti** (19 da una sola nave), **3 unita'
con tab**, **14 virgolette**, **zero token**. **Tutti e 29 i testi sono distinti**: nessuna ripetizione dentro il
segmento.

- **1 `VALUE`**: `Modified Argosies`, nome di nave al plurale, **identico** al sorgente (decisione 259).
- **2 testi vengono da L123** (la nota sui caccia e quella sui droni): resa riletta dal suo `translation.json` e
  **confrontata**, cosi' la stessa nota non cambia forma a un lotto di distanza.
"""
import collections
import glob
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
L10N = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PARTS = os.path.join(HERE, 'parts')
SRC = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
ENG = {u['idx']: u['english'] for u in SRC}
KIND = {u['idx']: u['kind'] for u in SRC}
TAGS = re.compile(r'<[^<>]+>')

PREV = {}
for f in glob.glob(os.path.join(L10N, 'staging/editorial/L123_*', 'translation.json')):
    for u in json.load(open(f, encoding='utf-8'))['units']:
        PREV[u['english']] = u['italian']

UNIQ = [
    ("engaging targets at short range",
     "Il Gunboat della Marina è progettato per ingaggiare bersagli a corto raggio, e serve anche come piattaforma "
     "sensoristica mobile della Marina, scansionando le navi alla ricerca di equipaggiamenti o carichi illegali."),
    ("bolting a cockpit and engine block",
     "Diversi secoli fa, ai primi tempi della Repubblica, il brusco aumento del commercio e dei viaggi spaziali "
     "portò a una forte domanda di navi da carico. Le Hauler nacquero semplicemente imbullonando un abitacolo e un "
     "blocco motore a un container da carico, e il progetto di base non è cambiato molto da allora."),
    ("mid-sized freighter",
     "Questa è una nave da carico di taglia media, progettata per un equilibrio tra capacità di carico e capacità "
     "difensiva. Secoli fa vari modelli di Hauler costituivano quasi metà delle navi mercantili in servizio, ma oggi "
     "il progetto è considerato un po' superato."),
    ("comparatively low price and simple construction",
     "Considerata da molti superata, ci sono comunque ancora molte Hauler in servizio grazie alla combinazione di "
     "prezzo relativamente basso e costruzione semplice. Questa versione grande della Hauler offre il miglior "
     "compromesso tra prezzo e spazio per il carico."),
    ("planetary militia's patrol squadron",
     "La Tarazed Hawk è una nave da guerra di classe intercettore, spesso usata come scorta per le navi da carico o "
     "negli squadroni di pattuglia di una milizia planetaria. Le Hawk sono abbastanza veloci da raggiungere la "
     "maggior parte delle navi più piccole, ma possono montare armi molto più potenti. Sono anche, naturalmente, una "
     "nave preferita dai capitani pirata che hanno guadagnato abbastanza da potersela permettere."),
    ("composite fiber",
     "La Headhunter è una delle navi più recenti progettate dalla Lionheart: una nave versatile che va bene sia per "
     "trasportare carico sia per la caccia ai ricercati. Come in molti progetti Lionheart, lo scafo è in gran parte "
     "fibra composita anziché metallo, sacrificando la robustezza dell'armatura in favore di un peso minore e di un "
     "movimento più rapido."),
    ("updated shuttle model",
     "La Heavy Shuttle è un modello di shuttle aggiornato dei Betelgeuse Shipyards, che cerca di migliorare il loro "
     "classico senza tempo offrendo capacità di carico e di passeggeri leggermente superiori, a scapito di un po' di "
     "velocità e manovrabilità."),
    ("keg-like shape",
     "Costruita per la prima volta da un cantiere ormai dimenticato molti secoli fa, la Hogshead ha preso il suo "
     "nome iconico dalla forma a botte dei suoi pod motore; il suo progetto fu un argomento di discussione molto "
     "acceso tra i capitani di ogni dove. La nave divenne rapidamente popolare dopo essere stata messa in vendita al "
     "pubblico, ed era comunemente vista nei vari sistemi come lo \"spazio-bus\" d'elezione nello spazio umano."),
    ("went bankrupt",
     "Purtroppo, solo pochi decenni dopo l'introduzione della nave, il cantiere fallì e non se ne seppe più nulla, "
     "lasciando la Hogshead alla storia come il loro unico successo. Nell'epoca attuale le Hogshead sono molto meno "
     "comuni; sono considerate \"brutte\" rispetto a navi moderne come la Star Queen, anche se alcuni posti nello "
     "spazio umano le vendono ancora."),
    ("freelancer",
     "La Jackal è nota per essere una delle prime navi da guerra progettate pensando ai piloti \"freelance\", anziché "
     "all'uso aziendale o delle forze dell'ordine. Ai suoi tempi d'oro la Jackal contendeva alla Berserker il titolo "
     "di nave intercettore più diffusa nello spazio umano. Tuttavia l'età della Jackal e la sua rigidità di fronte ai "
     "nuovi sviluppi delle armi portarono a un calo delle vendite che finì per far assorbire il produttore dal "
     "cantiere del suo rivale di vecchia data, la Betelgeuse Shipyards Berserker."),
    ("primary fighter used by the Republic Navy",
     "La Lance è il caccia principale usato dalla Marina della Repubblica. Come tutti i caccia, è debole da sola ma "
     "molto efficace come parte di uno squadrone più grande."),
    ("long before the Republic existed",
     "La Betelgeuse Shipyards Leviathan è in servizio da molto prima che la Repubblica esistesse. Sebbene oggi sia "
     "considerata un modello superato e goffo, resta una forza con cui fare i conti."),
    ("rare, extensively modified Behemoth",
     "Questa è una Behemoth rara e ampiamente modificata, usata da alcuni pirati e contrabbandieri per trasportare "
     "grandi quantità di merci verso sistemi vicini e lontani. È armata abbastanza bene da affrontare persino una "
     "Frigate della Marina se viene intercettata, e abbastanza veloce da fuggire da qualsiasi cosa più grande."),
    ("Quicksilver light warship",
     "Dopo che la loro Quicksilver, nave da guerra leggera armata con cannoni a particelle, ebbe grande successo tra "
     "le scorte dei convogli e le forze di difesa planetarie, la Megaparsec decise di sviluppare una nave più grande "
     "con manovrabilità simile ma potenza di fuoco superiore. La Manta è il risultato: una nave con abbastanza "
     "potenza a lungo raggio che fuggire da uno scontro con lei è quasi impossibile."),
    ("semi-autonomous Mining Drone",
     "Il Mining Drone semi-autonomo è usato dal Sindacato insieme alla nave mineraria Sunder in un ruolo di "
     "supporto. Non essendo molto più di un Mining Laser con un motore attaccato dietro, questi droni non durano a "
     "lungo in combattimento contro altre navi, tanto sono fragili."),
    ("come up with many tricks",
     "L'Argosy è da tempo una nave preferita dai pirati, che hanno escogitato molti trucchi per modificarle e "
     "renderle più adatte alla guerra."),
    ("peace among the stars",
     "Quando la Repubblica si formò, i governi planetari e le corporazioni schieravano spesso flotte proprie; solo "
     "il Deep aveva una qualche forma di marina unificata. La Terra si trovava spesso a dirigere in modo inefficiente "
     "quelle flotte contro pirati o mondi ribelli. Con la necessità di portare \"pace tra le stelle\", secondo il "
     "motto della Repubblica, la neonata Marina della Repubblica commissionò ai cantieri di Luna una nave da guerra "
     "robusta, capace di proiettare la potenza di una Repubblica unita. La nave che ne risultò, la Monitor, fu il "
     "pilastro delle flotte della Marina fino all'introduzione della più avanzata Frigate."),
    ("sold by the Navy to the government of Betelgeuse",
     "I pochi Monitor che volano ancora oggi sono quel che resta di quelli venduti dalla Marina al governo di "
     "Betelgeuse, prima che si unisse alla Repubblica. Di quelli finiti in mani private, alcuni sono passati per i "
     "mercati neri dell'Estremo Nord."),
    ("as much of a hodgepodge as its looks",
     "La Mule è un guazzabuglio quanto il suo aspetto suggerisce. I progettisti della Lionheart hanno unito un buon "
     "spazio per il carico a un armamento decente e persino a una baia di caccia, ottenendo una nave usata per lo "
     "più come cargo ma capace anche di combattere, grazie all'armamento pesante e agli scudi. Questa natura ibrida "
     "ha però il suo rovescio, cioè l'elevato fabbisogno di equipaggio e il fatto che qualsiasi nave specializzata "
     "dello stesso costo farà meglio della Mule nel suo ruolo."),
    ("Hauler I: Type F",
     "I Southbound Shipyards risposero in fretta alla richiesta di una portatrice da parte dei Mondi Liberi "
     "costruendo container da carico modificati per le Hauler: aggiunsero un paio di bracci di attracco per caccia, "
     "un po' di spazio per equipaggiamenti e persino un paio di cuccette. L'accesso ai caccia dall'interno della "
     "nave è così scomodo che la maggior parte dei piloti sceglie di restare a bordo dei propri caccia in volo. "
     "Sebbene il nome tecnico di questa nave sia \"Hauler I: Type F\", gli operai della linea di montaggio Southbound "
     "iniziarono a chiamare la variante a container singolo \"Nest\" per via del suo equipaggio di caccia Finch, e il "
     "nome rimase."),
    ("increase a Blackbird's passenger capacity",
     "La Nighthawk è il risultato di modifiche per aumentare la capacità passeggeri di una Blackbird, per il "
     "trasporto sia di individui fuorilegge sia di schiavi, sacrificando gran parte dello spazio per il carico "
     "originale. Inoltre, a costo di un po' di robustezza degli scudi, le conversioni dello scafo hanno dato alla "
     "nave un po' più di corazzatura e un altro alloggiamento per torretta. Questo dà alle Nighthawk un po' più di "
     "difesa nelle situazioni di combattimento in cui una Blackbird non vorrebbe trovarsi."),
    ("overpriced by most savvy pilots",
     "Dopo che la Blackbird guadagnò una popolarità sorprendente come nave da guerra leggera e agile, nonostante il "
     "progetto originale da trasporto, la Tarazed decise di produrre un progetto pensato espressamente come nave da "
     "guerra. La Osprey fu il risultato. Sebbene sia considerata troppo cara dalla maggior parte dei piloti esperti, "
     "resta comunque una preferita di sempre tra chi ha soldi extra da spendere."),
    ("ugliest ship in the sky",
     "Votata \"la nave più brutta del cielo\" dalla rivista Stars and Starships, la Protector è un tipico esempio "
     "dell'ingegneria del Sindacato, brutalmente efficiente. In pratica non è altro che otto torrette attaccate a un "
     "insieme di motori e alloggi dell'equipaggio, progettata come piattaforma di difesa che possa accompagnare i "
     "convogli mercantili."),
    ("two Particle Cannons",
     "La Megaparsec Quicksilver è una nave da guerra costruita attorno a un solo concetto: progettare la nave più "
     "piccola e veloce capace di portare due cannoni a particelle. Grazie alla velocità, ai propulsori inversi e alla "
     "lunga portata delle armi, la Quicksilver può tenersi a distanza di sicurezza dalla maggior parte dei bersagli e "
     "bombardarli con raffiche di particelle finché non sono distrutti. L'attenzione alle armi ha lasciato alla "
     "Quicksilver non spazio nemmeno per il più semplice generatore di scudi. Purtroppo la Headhunter finì per "
     "superare l'intento progettuale originale, ma il miglior rapporto durabilità-costo della Quicksilver, e "
     "l'esistenza di contratti a lungo termine, l'hanno mantenuta in uso presso le forze di sicurezza del Sindacato."),
    ("four missile launchers",
     "La Rainmaker è una lanciamissili costruita nell'Arsenale della Marina della Repubblica. Viene fornita con "
     "quattro lanciatori di missili e munizioni sufficienti a distruggere anche navi molte volte più grandi. A causa "
     "della scarsa manovrabilità e degli scudi relativamente leggeri, le Rainmaker rendono al meglio come navi "
     "d'attacco a lungo raggio, e una volta esaurite le munizioni sono relativamente inutili in combattimento."),
    ("most popular warship",
     "La Lionheart Raven è la loro nave da guerra più diffusa, un vascello agile ed elegante che però sa infliggere "
     "e assorbire danni considerevoli. Le Raven sono una nave preferita dai cacciatori di taglie, perché sono più "
     "che all'altezza degli intercettori pirata e un pilota abile può usarle per abbattere anche navi molto più "
     "grandi."),
]

db = sqlite3.connect('file:' + os.path.join(L10N, 'state.db') + '?mode=ro', uri=True)
ST = {u['idx']: db.execute('select state from units where id=?', (u['id'],)).fetchone()[0] for u in SRC}
assert set(ST.values()) == {'PENDING'}, {k: v for k, v in ST.items() if v != 'PENDING'}

assert collections.Counter(u['kind'] for u in SRC) == {'DESCRIPTION': 28, 'VALUE': 1}
assert sum(1 for u in SRC if u['english'].startswith('\t')) == 3
assert sum(u['english'].count('"') for u in SRC) == 14
ctx = collections.Counter(u['context'] for u in SRC)
assert len(ctx) == 24 and collections.Counter(ctx.values()) == {1: 19, 2: 5}, ctx
assert collections.Counter(t for u in SRC for t in TAGS.findall(u['english'])) == {}   # zero token

distinct = list(dict.fromkeys(ENG.values()))
assert len(distinct) == 29, len(distinct)
names = {u['english'] for u in SRC if u['kind'] == 'VALUE'}
assert names == {'Modified Argosies'}, names
prose = [e for e in distinct if e not in names]
assert len(prose) == 28
reused = [e for e in prose if e in PREV]
assert len(reused) == 2, len(reused)
assert len([e for e in prose if e not in PREV]) == 26 == len(UNIQ), (len(prose), len(UNIQ))


def resolve(eng):
    if eng in PREV:
        return PREV[eng]
    hits = [t for s, t in UNIQ if s in eng]
    assert len(hits) == 1, (len(hits), eng[:90], hits)
    return hits[0]


cover = {e: resolve(e) for e in prose}
assert len(set(cover.values())) == 28, 'due testi distinti con la stessa resa'

T = {}
for u in SRC:
    eng = u['english']
    if u['kind'] == 'VALUE':
        T[u['idx']] = eng
    else:
        T[u['idx']] = '\t' * (len(eng) - len(eng.lstrip('\t'))) + cover[eng].lstrip('\t')

for idx, txt in T.items():
    eng, kind = ENG[idx], KIND[idx]
    assert txt.count('\t') == eng.count('\t'), idx
    assert txt.count('"') == eng.count('"'), (idx, eng.count('"'), txt.count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng) == [], idx
    assert not re.search(r'[\[\]`\u2019\u2014\u2013\u2026]', txt), idx
    assert not re.search(r"\b(e|piu|perche|cosi|gia|puo|cioe|percio|fa)'", txt), idx
    if kind == 'VALUE':
        assert txt == eng, idx
    else:
        assert txt.strip() and txt.strip() != eng.strip(), idx
    r = len(txt) / len(eng)
    assert 0.55 < r < 1.90, ('gate', idx, round(r, 3), eng[:60])

for n, (lo, hi) in enumerate(((1, 15), (16, 29))):
    d = {str(k): T[k] for k in range(lo, hi + 1)}
    with open(os.path.join(PARTS, 'part%02d.json' % (n + 1)), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print('29 unita (15+14) · 29 testi distinti · 1 VALUE identico · 2 note da L123 · 3 tab · 14 virgolette · 0 token')
