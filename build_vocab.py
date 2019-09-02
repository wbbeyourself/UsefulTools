import sys

if len(sys.argv) == 1:
    print 'python build_vocab.py vocab_size < train_file > vocab_file'
    sys.exit()

n = int(sys.argv[1])

d = {}
for s in sys.stdin:
    for w in s.split():
        d[w] = d.get(w, 0) + 1

print '<eos>'
print '<unk>'
print 'LITERAL1'
print 'LITERAL2'
print 'LITERAL3'
print 'LITERAL4'
print 'LITERAL5'
print 'TERM1'
print 'TERM2'
print 'TERM3'
print 'TERM4'
print 'TERM5'
print 'HUMAN1'
print 'HUMAN2'
print 'HUMAN3'
print 'HUMAN4'
print 'HUMAN5'
print 'LOCATION1'
print 'LOCATION2'
print 'LOCATION3'
print 'LOCATION4'
print 'LOCATION5'
print 'ORGANIZATION1'
print 'ORGANIZATION2'
print 'ORGANIZATION3'
print 'ORGANIZATION4'
print 'ORGANIZATION5'
for i in range(15):
    print 'RESERVE' + str(i)

m = 42
for k, v in sorted(d.items(), key=lambda d: d[1], reverse=True):
    if 'LITERAL' in k or 'TERM' in k or 'HUMAN' in k or 'LOCATION' in k or 'ORGANIZATION' in k:
        continue
    print k
    m += 1
    if m == n:
        break
