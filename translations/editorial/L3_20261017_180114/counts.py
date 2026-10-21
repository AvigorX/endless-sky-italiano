import sqlite3
c = sqlite3.connect('file:state.db?mode=ro', uri=True)
q = lambda s, *a: c.execute(s, a).fetchall()

tot = q("select count(*) from units where state='PENDING'")[0][0]
pl = q("select count(*), sum(length(english)-length(replace(english,' ',''))+1) from units where state='PENDING' and path='data/map planets.txt'")
pl_after = q("select count(*), sum(length(english)-length(replace(english,' ',''))+1) from units where state='PENDING' and path='data/map planets.txt' and line>5121")
kinds = q("select kind,count(*) from units where state='PENDING' group by kind order by 2 desc")
labels = q("select count(*) from units where state='PENDING' and kind='LABEL'")[0][0]
print('PENDING totali', tot)
print('planets.txt PENDING: %d unita, %d parole' % pl[0])
print('planets.txt dopo riga 5121: %d unita, %d parole' % (pl_after[0], pl_after[1]))
print('LABEL PENDING:', labels)
print('staging L3 = 79 -> PENDING non in staging:', tot - 300)
print('traducibili residue:', tot - 300 - labels)
print('parole residue stimate: 965570 - 4509 =', 965570 - 4509)
print()
for k, n in kinds[:8]:
    print(' ', k, n)
print()
print('ultima riga planets.txt:', q("select max(line) from units where path='data/map planets.txt'")[0][0])
