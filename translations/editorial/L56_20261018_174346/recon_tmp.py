import collections
import json
import re

HERE = 'staging/editorial/L56_20261018_174346'
u = json.load(open(HERE + '/source.json', encoding='utf-8'))['units']
print('unita', len(u), 'righe', u[0]['line'], '-', u[-1]['line'])
print('kinds', dict(collections.Counter(x['kind'] for x in u)))
print('tab', sum(x['english'].count('\t') for x in u), 'iniziali',
      sum(1 for x in u if x['english'].startswith('\t')))
print('virgolette', sum(y['english'].count('"') for y in u))
print('dispari', [x['idx'] for x in u if x['english'].count('"') % 2])
print('quadre', [x['idx'] for x in u if '[' in x['english'] or ']' in x['english']])
print('backtick', sum(x['english'].count('`') for x in u))
TAGS = re.compile(r'<[^<>]+>')
fam = collections.Counter(t for x in u for t in TAGS.findall(x['english']))
print('token', sum(fam.values()), dict(fam))
for k in ('UI_LABEL', 'LOGBOOK', 'DIALOG', 'CONVERSATION', 'VALUE', 'DESCRIPTION', 'TEXT'):
    print(k, [x['idx'] for x in u if x['kind'] == k])
print('== DIALOG ==')
for x in u:
    if x['kind'] == 'DIALOG':
        print(' ', x['idx'], 'r', x['line'], repr(x['english'])[:200])
print('== UI_LABEL ==')
for x in u:
    if x['kind'] == 'UI_LABEL':
        print(' ', x['idx'], 'r', x['line'], '|', repr(x['english']))
print('== contesti ==')
ctx = []
for x in u:
    if not ctx or ctx[-1][0] != x['context']:
        ctx.append([x['context'], x['idx'], x['idx']])
    else:
        ctx[-1][2] = x['idx']
for c in ctx:
    print(' ', c[0], c[1], c[2], c[2] - c[1] + 1)
print('== duplicati ==')
c = collections.Counter(x['english'] for x in u)
for k, n in c.items():
    if n > 1:
        print(' ', n, [x['idx'] for x in u if x['english'] == k], repr(k)[:60])

out = 'C:/Users/Dave/AppData/Local/hermes/profiles/game/cache/scratch/l56_en.txt'
with open(out, 'w', encoding='utf-8') as f:
    for x in u:
        f.write('%d\t%d\t%s\n' % (x['idx'], x['line'], x['kind']))
        f.write(x['english'].replace('\t', '»') + '\n')
print('dump ok')
