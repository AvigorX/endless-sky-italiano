"""mkparts.py — L99: costruisce `parts/part01-03.json` (38 unita', righe 106-211).

Quattro contesti: tre missioni «sport star» quasi identiche (Wrestling 119-128, Fencing 142-151, Mystery Sport
165-174) e `Gambling Judgment` (188-211).

**Sette gruppi di ripetizioni** rese identiche da costanti uniche: 1/8/15 (l'apertura), 2/9/16 (ignorare),
3/10/17 (guardare), 4/11/18 (la folla), 6/13 (l'evento), 7/14/21 (il trillo), 24/27 (ordinare).

**Zero token, zero quadre** (asseriti): nessun `<...>` e nessuna `[`/`]` in questo lotto.

**Una virgoletta dispari voluta**: l'unita' 32 apre la citazione del barista e **non la chiude** (la battuta
continua nell'unita' 33). Va riprodotta con **una** virgoletta, non pareggiata.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

OPEN = '''Mentre attraversate lo spazioporto, notate una folla di Hai che trillano raccolti in una zona.'''
IGNORE = '''(Ignorateli e passate oltre.)'''
LOOK = '''(Date un'occhiata.)'''
CROWD = '''La folla sembra composta per lo più da Hai giovani, anche se ci sono alcuni Hai più maturi, che mostrano visibilmente più ritegno nel loro entusiasmo. Raggiunto il bordo della folla e guardando al di sopra degli Hai più bassi, vedete un tavolo allestito con due stendardi ai lati e una pila di quelle che, a prima vista, sono foto stampate su carta patinata.'''
SIGNING = '''Dopo solo un momento la persona in questione esce da una cabina dietro l'allestimento e saluta i suoi fan, che si dimostrano molto entusiasti, prima di sedersi con una specie di penna per la fila degli Hai radunati. Sembra che certe usanze umane si siano diffuse fra gli Hai.'''
TRILL = '''Potete sentire la folla di Hai trillare per un bel tratto mentre proseguite per i vostri affari.'''
ORDER = '''(Ordinate qualcosa.)'''

P1 = {
 1: OPEN,
 2: IGNORE,
 3: LOOK,
 4: CROWD,
 5: '''Gli stendardi raffigurano un Hai dall'aria piuttosto muscolosa, reso con grande dettaglio, con un'animazione potenziata in ologramma che lo fa sembrare intento senza posa a sollevare e lasciar cadere un avversario volutamente sfocato. L'effetto, però, è ottenuto solo con un trucco di prospettiva spostata artificialmente. Con vostra sorpresa, capite che si tratta di una sessione di autografi di una stella del wrestling, nientedimeno.''',
 6: SIGNING,
 7: TRILL,
 8: OPEN,
 9: IGNORE,
 10: LOOK,
 11: CROWD,
 12: '''Gli stendardi raffigurano un Hai snello nella divisa di schermidore, di una familiarità sorprendente, con un'animazione potenziata in ologramma che lo fa sembrare intento senza posa a eseguire un'elegante parata e risposta contro un avversario fuori campo. L'effetto, però, è ottenuto solo con un trucco di prospettiva spostata artificialmente. Con vostra sorpresa, capite che si tratta di una sessione di autografi di una stella della scherma, nientedimeno.''',
 13: SIGNING,
}

P2 = {
 14: TRILL,
 15: OPEN,
 16: IGNORE,
 17: LOOK,
 18: CROWD,
 19: '''Gli stendardi raffigurano una coppia di Hai, uno con una rete e uno con quella che sembra una sorta di frisbee con lame. Non è affatto chiaro che cosa facciano esattamente, e quando le persone in questione escono da una cabina dietro l'allestimento e salutano i fan diventa evidente che, anche riuscendo a farvi sentire sopra il trillare, nessuno ha particolare voglia di spiegarvelo.''',
 20: '''I due si tolgono i caschi e rivolgono ai fan sorrisi smaglianti alla maniera Hai, prima di sedersi con una specie di penna per la fila degli Hai radunati. Sembra che le sessioni di autografi delle celebrità siano popolari fra gli Hai.''',
 21: TRILL,
 22: '''Vi fermate in una tavola calda per mangiare a terra nello spazioporto, ma non siete seduti da molto quando notate un gruppo di altri capitani di navi umani appartati in un angolo che giocano, per quanto riuscite a capire, a poker. Notate che il gruppo riceve una varietà di sguardi torvi da vari Hai che stanno cenando nel locale.''',
 23: '''Dopo un po' arriva a prendere l'ordine il barista, un Hai di mezza età e leggermente in sovrappeso.''',
 24: ORDER,
 25: '''"Ehi, ho notato che ci sono degli sguardi torvi qui intorno. I capitani umani non sono benvenuti?"''',
 26: '''Il barista sembra confuso per un istante, poi guarda verso il tavolo e scuote la testa, avendo capito. "Oh no, siete perfettamente benvenuti. Quel gruppo sta semplicemente infrangendo i principi della maturità, e alcuni Hai si sentono a disagio quando degli adulti si comportano sfacciatamente come bambini in pubblico."''',
 27: ORDER,
}

P3 = {
 28: '''"I principi della maturità?"''',
 29: '''"Ah già, suppongo che lei non lo sappia. Ci sono diversi principi che agli Hai vengono insegnati crescendo, lezioni da interiorizzare per essere un membro responsabile e funzionante della società. Il secondo è 'Essere onesti negli affari', e il terzo è 'Scommettere solo sull'abilità, non sul caso', quindi il loro gioco ne infrange due."''',
 30: '''"Alcuni direbbero che il poker è più questione di abilità che di caso."''',
 31: '''"Certo, però se è solo un gioco, non c'è niente di male, no?"''',
 32: '''"Oh no, temo che il primo principio garantisca che non sia davvero favorevole in nessuno dei due casi. Il primo è 'Avere una chiara separazione fra fantasia e realtà', così un gioco non può avere conseguenze reali, altrimenti è realtà, non fantasia. Quindi scommettere denaro sul gioco significa portare conseguenze reali in un esercizio di fantasia. Questo è tabù per un adulto.''',
 33: '''"Se si interpreta il gioco come giocato per l'abilità, senza le puntate, allora si soddisfano il primo e il terzo principio, ma resta il problema che le abilità principali sono il bluff e la manipolazione, il che viola il secondo principio. Il bluff non è un'abilità considerata virtuosa, e nemmeno la manipolazione."''',
 34: '''"Aspetta, gli Hai non mentono e non bluffano?"''',
 35: '''Il barista ridacchia con uno strano trillo e dice: "Oh no, gli Hai mentono e bluffano. Siamo anzi molto bravi a bluffare, vantaggioso per l'evoluzione allo stato brado e cose così. È solo considerato molto immaturo e basso. Un adulto dovrebbe poter condurre la propria vita senza ricorrere a istinti così primitivi. L'abbiamo imparato a nostre spese molto tempo fa, prima di rinchiuderci nei nostri confini attuali."''',
 36: '''Vi guarda intensamente prima di continuare: "Non sentirete parlare spesso dei principi, ma se guardate bene vedrete che i primi tre soprattutto sono radicati molto in profondità nella nostra società."''',
 37: '''Con un'alzata di spalle apre il blocchetto degli ordini e si dà un colpetto sulla pancia. "Certo, mia nonna diceva sempre che quelli dopo il decimo erano più indicazioni che regole vere, e di certo ho le mie divergenze con il tredicesimo. Ora, prima di parlarle fino a stordirla, che cosa le porto?"''',
 38: '''Prende l'ordine con diligenza e con un sorriso.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
for idx, txt in list(P1.items()) + list(P2.items()) + list(P3.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]) == [], idx
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx
assert sorted(P1) == list(range(1, 14)) and sorted(P2) == list(range(14, 28)) and sorted(P3) == list(range(28, 39))
# i gruppi identici vengono da una costante unica: la resa non puo' divergere
assert P1[1] is P1[8] is P2[15] and P1[1] == OPEN
assert P1[2] is P1[9] is P2[16] and P1[3] is P1[10] is P2[17]
assert P1[4] is P1[11] is P2[18] and P1[6] is P1[13] and P1[7] is P2[14] is P2[21]
assert P2[24] is P2[27] is ORDER
# l'unita' 32 apre la citazione e non la chiude: una sola virgoletta, voluta
assert eng[32].count('"') == 1 and P3[32].count('"') == 1
assert all(eng[i].count('"') % 2 == 0 for i in eng if i != 32)

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2), ('part03.json', P3)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (13 + 14 + 11)' % (len(P1) + len(P2) + len(P3)))
