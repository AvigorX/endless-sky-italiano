# -*- coding: utf-8 -*-
"""Porta il controllo LOGBOOK di L67 da 'assenza dichiarata' a 'conteggio atteso' (1 unita')."""
p = 'check.py'
s = open(p, encoding='utf-8').read()

old = """rows.append(('righe LOGBOOK nel segmento (0 attese: assenza dichiarata)',
             len([v for v in cov if v['kind'] == 'LOGBOOK']) or 'ok',
             not [v for v in cov if v['kind'] == 'LOGBOOK']))"""
new = """rows.append(('righe LOGBOOK nel segmento (%d attese: controllo positivo)' % len([x for x in LOG if lo <= x <= hi]),
             len([v for v in cov if v['kind'] == 'LOGBOOK']) or 'ok',
             len([v for v in cov if v['kind'] == 'LOGBOOK']) == len([x for x in LOG if lo <= x <= hi])))"""
assert old in s
s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s)
print('riga LOGBOOK resa positiva')
