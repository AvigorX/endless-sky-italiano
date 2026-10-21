"""mkparts.py — L110: costruisce `parts/part01-02.json` (26 unita', righe 474-580) — CHIUDE il file.

Tre contesti: `Efreti: Distress Call 6` (474-479), `Distress Call 7` (508-558), `Distress Call 8` (570-580).

**21 `MISSION_TEXT` + 2 `VALUE` + 2 `DESCRIPTION` + 1 `DIALOG`**.

**Due coppie di ripetizioni identiche nel sorgente**: 1/4 sono lo stesso `VALUE` (`Salvage the <EDC-ship>`) e 2/5
la stessa `DESCRIPTION`. Vanno rese **identiche** e dichiarate: qui il criterio «zero ripetizioni» dei lotti
precedenti e' rovesciato.

`<first>` e `<last>` (nome e cognome del giocatore) compaiono **insieme** nell'unita' 25, dentro la dedica.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'parts')

VALUE = '''Salvage the <EDC-ship>'''
DESCR = '''Recupera la <EDC-ship> e riportala su <planet> per rivendicarne la proprietà.'''

P1 = {
 1: VALUE,
 2: DESCR,
 3: '''Devi poter trasportare <bunks> membri d'equipaggio in più per recuperare la nave. Torna qui quando avrai capienza sufficiente per l'equipaggio.''',
 4: VALUE,
 5: DESCR,
 6: '''Grazie al lavoro del vostro equipaggio, l'atmosfera della nave viene portata agli standard umani, anche se un po' tropicali. Mentre il recupero prosegue, voi e il vostro equipaggio cominciate a familiarizzare con la nave. Lo scafo robusto sembra in grado di volare nello spazio, ma la nave non ha quasi armi, i sistemi delle batterie sono irrecuperabili e la rigenerazione degli scudi è impossibile. Se i Mereti attaccano, la <EDC-ship> non sopravviverà a lungo.''',
 7: '''(Porta la <EDC-ship> a casa.)''',
 8: '''(Abbandona la nave.)''',
 9: '''Il vostro equipaggio abbandona la nave Korath alle intemperie, solo un'altra storia tragica fra le rovine della loro civiltà.''',
 10: '''Riuscite ad attivare gli scudi, almeno all'inizio, usando la <ship>. Il vostro equipaggio sulla <EDC-ship> prende posizione mentre vi preparate a evitare le pattuglie Mereti sulla strada per <destination>.''',
 11: '''Arrivate, ma notate che la <EDC-ship> non c'è. Dovrete portarla qui per completare la missione di recupero.''',
 12: '''Questa volta non ci sono folle ad aspettarvi quando atterrate; piuttosto, le squadre di terra sembrano stupite di vedere la nave. Vi serve un po' di tempo per organizzare riparazioni aggiuntive, ma quando avete finito un padiglione è stato montato vicino alla <EDC-ship>, e piccoli gruppi di Korath si fermano lì di tanto in tanto.''',
 13: '''(Dai un'occhiata.)''',
}

P2 = {
 14: '''(Ho altro da fare.)''',
 15: '''La tenda è più grande di quanto vi aspettaste. In fondo c'è un gruppo di Korath disposti come un coro, ma stranamente immobili. Un Korath in una specie di veste sta accanto a un tavolo ingombro di dolciumi e di coppe colme di una bevanda densa. Avvicinandovi, capite che il "coro" è fatto di ologrammi. Fate un rapido conto mentale e supponete che siano i Korath morti sulla nave; probabilmente è una specie di memoriale. Il Korath in veste vi saluta e vi preme una coppa in mano.''',
 16: '''(Bevi.)''',
 17: '''(Fai il gesto di bere.)''',
 18: '''O gli Efret non si accorgono del vostro trucco, o sono troppo educati per dirlo. Vi insistono con i dolciumi, così li prendete. Vedete alcuni gruppi dello spazioporto seguire lo stesso rituale, anche se alcuni si avvicinano al "coro" e gli dicono qualcosa. Quando avete finito il cibo, vi congedate e tornate alla vostra nave.''',
 19: '''La bevanda è fermentata e ha un sapore agrodolce che lascia le labbra e la bocca formicolanti, finché non le intorpidisce. Poi il Korath vi insiste con i dolciumi, e voi li accettate con umiltà. Alcuni gruppi dello spazioporto seguono lo stesso rituale, anche se alcuni si avvicinano al "coro" e gli dicono qualcosa. Quando avete finito il cibo, vi congedate e tornate alla vostra nave.''',
 20: '''In passato i Quarg vi hanno tradotto la lingua Korath. Avete il chip dati di quando avete aiutato gli Efret a recuperare la <EDC-ship>. Volete vedere se i Quarg possono dirvi cosa c'è scritto nel chip?''',
 21: '''(Chiedi ai Quarg di tradurre il chip dati.)''',
 22: '''(Magari un'altra volta.)''',
 23: '''(Non m'importa cosa dice.)''',
 24: '''Vi avvicinate a uno dei Quarg nello spazioporto e chiedete aiuto con il chip dati. Si ferma e vi riconosce, ma non parla. Esita qualche istante dopo la vostra richiesta, poi tende la mano. Preso il chip dati, lo inserisce in una specie di comunicatore, annuisce lentamente fra sé e ve lo restituisce.''',
 25: '''Tornate alla vostra nave e provate a inserire di nuovo il chip nei vostri sistemi, che ora mostrano due file: uno in lingua Korath e uno nella vostra. Aprite il file nella vostra lingua e legge: "La <EDC-ship> è una nave di dolore, che porta grande pena in memorie che cantano per generazioni. L'amore è un vuoto nell'anima di molti. Sappiate tutti che <first> <last> è un Efret autentico di cuore, se non di pelle. La <EDC-ship> è sua, per salvare vite e custodire memorie."''',
 26: '''Riponete con cura il chip in un posto sicuro.''',
}

src = json.load(open(os.path.join(HERE, 'source.json'), encoding='utf-8'))['units']
eng = {u['idx']: u['english'] for u in src}
kind = {u['idx']: u['kind'] for u in src}
TAGS = re.compile(r'<[^<>]+>')
ALL = {}
for d in (P1, P2):
    ALL.update(d)
for idx, txt in ALL.items():
    assert not txt.startswith('\t'), idx
    assert txt.count('\t') == 0, idx
    assert txt.count('"') == eng[idx].count('"'), (idx, txt.count('"'), eng[idx].count('"'))
    assert TAGS.findall(txt) == TAGS.findall(eng[idx]), (idx, TAGS.findall(eng[idx]), TAGS.findall(txt))
    assert '[' not in txt and ']' not in txt, idx
    assert txt.strip(), idx

assert sorted(P1) == list(range(1, 14)) and sorted(P2) == list(range(14, 27))
assert [i for i in range(1, 27) if kind[i] == 'VALUE'] == [1, 4]
assert [i for i in range(1, 27) if kind[i] == 'DESCRIPTION'] == [2, 5]
assert [i for i in range(1, 27) if kind[i] == 'DIALOG'] == [11]
for i in (1, 4):
    assert ALL[i] == eng[i], (i, ALL[i], eng[i])
# le DUE ripetizioni: identiche nel sorgente e rese identiche in italiano
assert eng[1] == eng[4] and ALL[1] == ALL[4]
assert eng[2] == eng[5] and ALL[2] == ALL[5]
assert ALL[2] != eng[2]
# nessun'altra unita' identica al sorgente
assert [i for i in ALL if kind[i] != 'VALUE' and ALL[i].strip() == eng[i].strip()] == []
# nome e cognome del giocatore nello stesso testo, e la nave nominata due volte (dedica)
assert TAGS.findall(ALL[25]) == ['<EDC-ship>', '<first>', '<last>', '<EDC-ship>'], TAGS.findall(ALL[25])
assert TAGS.findall(ALL[3]) == ['<bunks>']

os.makedirs(OUT, exist_ok=True)
for name, d in (('part01.json', P1), ('part02.json', P2)):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(d.items())}, f, ensure_ascii=False, indent=1)
print('scritte %d unita (13 + 13)' % len(ALL))
