"""mkparts.py — L104: costruisce `parts/part01-02.json` (27 unita', righe 250-334).

Due contesti: `Ask Quarg About Coalition Early` (265-284) e `Quarg Pug Arfecta Warning` (302-334).

**Cinque citazioni aperte e non chiuse** (unita' 5, 19, 22, 23, 24): il discorso del Quarg continua nell'unita'
successiva e il gioco mostra i due messaggi come uno solo. Ognuna ha **il numero di virgolette del sorgente** e
nessuna chiude: si riproducono, non si pareggiano.

**0 token, 0 quadre, nessuna ripetizione.** L'unita' 23 ha un `-` isolato nel sorgente («human - what weapon»):
si riproduce come trattino, non come em dash.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

P1 = {
 1: '''Avete incontrato la Coalizione, e gli Heliarch che governano il loro spazio dall'interno dei mondi ad anello che i Quarg hanno costruito laggiù, e che affermano di avere "sconfitto gli oppressori Quarg". Volete cercare qualche Quarg qui e chiedere la loro versione della storia?''',
 2: '''(Sì.)''',
 3: '''(No.)''',
 4: '''Fermate il primo Quarg che vi passa accanto e chiedete se può raccontare la sua versione della storia sulla Coalizione.''',
 5: '''"Ah, dunque hai incontrato la stolta Coalizione," comincia. "Un tempo erano tre specie promettenti, prima di cedere al desiderio insensato di usurpare le grandi imprese altrui.''',
 6: '''"Non che siano tutti ladruncoli, ma purtroppo la civiltà che sono diventati è ora governata da un esercito fanatico, come di certo hai visto, avendo parlato con quei miseri Heliarch."''',
 7: '''"È vero che vi hanno sconfitti?"''',
 8: '''"È vero quello che mi hanno raccontato? Che li opprimevate e ostacolavate il loro sviluppo?"''',
 9: '''Fa scattare i denti l'uno contro l'altro per un momento e si acciglia un po'. "Non sottovalutarci, umano. Siamo numerosi, e siamo forti." Si ferma un momento, con un'espressione vuota sul viso, come se cercasse di ricordare qualcosa. "Sappiamo solo che è meglio non massacrare miliardi di esseri per mantenere la nostra posizione."''',
 10: '''"Certo che no. Ci hai visto fare cose simili con l'umanità? O con qualche altra specie aliena che tu possa aver raggiunto nei tuoi viaggi con un motore a salto? Gli Heliarch, come qualsiasi altro esercito fanatico, si sono inventati una scusa per giustificare l'attacco contro di noi."''',
 11: '''Prima che possiate chiedergli altro, il Quarg vi saluta e si allontana.''',
 12: '''Appena atterrate, vedete una folla di Quarg radunarsi intorno a una delle vostre scorte, il Pug Arfecta. Il capitano della nave sembra scosso mentre i Quarg lo circondano e un Quarg piuttosto alto, anche per gli standard Quarg, sembra interrogarlo. Il capitano si guarda intorno e, vedendo voi, vi indica, facendo sì che il Quarg venga verso di voi. Il Quarg alto torreggia su di voi e vi fissa con uno sguardo penetrante.''',
 13: '''Appena atterrate con la nave, una folla di Quarg comincia a radunarsi. Mentre scendete, trovate un Quarg piuttosto imponente che vi blocca l'uscita. Alto anche per gli standard Quarg, torreggia su di voi e vi fissa con uno sguardo penetrante.''',
 14: '''"È come se un bambino in fasce avesse addomesticato un drago e ora lo cavalcasse per il cielo sputando fuoco con abbandono sconsiderato," dice senza distogliere lo sguardo, senza battere ciglio.''',
}

P2 = {
 15: '''"È una storia lunga..."''',
 16: '''"È stato un atto di giusta ribellione."''',
 17: '''"I Pug si credono dèi, ma dal momento che Dio è morto..."''',
 18: '''"Ho visto qualcosa che mi piaceva, e me la sono presa."''',
 19: '''Sbuffa: "Non importa come sia successo.''',
 20: '''"Allora ti credi un salvatore o un rivoluzionario?" dice il Quarg con quello che immaginate sia un tono sarcastico.''',
 21: '''"Quindi ti degni di dimostrare che si sbagliano?" dice il Quarg con un tono quasi divertito, o forse incredulo.''',
 22: '''"Un bambino in fasce, davvero...''',
 23: '''"Vi diamo un avvertimento. Non sapete cosa avete, umano - quale arma impugnate.''',
 24: '''"Ne abbiamo visto il potere. L'abbiamo sentito, e ne abbiamo imparato. Ma voi e la vostra specie non sapete nulla dei fardelli e dei pericoli che ne seguono. Fate attenzione a essere voi a dirigere questo potere, e non lui a dirigere voi.''',
 25: '''"Sappi bene che abbiamo imparato a superarlo."''',
 26: '''Il Quarg dà un ultimo lungo sguardo alla vostra nave, poi fa un breve cenno di commiato, lasciandovi ai vostri affari. Anche la folla comincia a disperdersi, e solo pochi restano a fissare la nave a bocca aperta.''',
 27: '''Mentre attraversate l'anello, notate occasionali sguardi torvi da parte dei Quarg a bordo.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
OPEN = [5, 19, 22, 23, 24]
for idx, txt in list(P1.items()) + list(P2.items()):
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]) == [], idx
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx
    if idx in OPEN:
        # citazione aperta: il discorso continua nell'unita' successiva
        assert not txt.rstrip().endswith('"'), idx
assert sorted(P1) == list(range(1, 15)) and sorted(P2) == list(range(15, 28))
assert [i for i in range(1, 28) if eng[i].count('"') % 2] == OPEN
assert [i for i in range(1, 28) if (P1 | P2)[i].count('"') % 2] == OPEN
assert eng[23].count('"') == 1 and P2[23].count('"') == 1
# il trattino isolato dell'unita' 23 resta un trattino, non un em dash
assert ' - ' in P2[23] and '\u2014' not in P2[23]

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (14 + 13)' % (len(P1) + len(P2)))
