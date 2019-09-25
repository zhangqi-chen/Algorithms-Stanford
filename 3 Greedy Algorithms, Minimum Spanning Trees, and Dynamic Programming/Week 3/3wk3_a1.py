"""
Huffman coding and Dynamic programing
"""

f = open('huffman.txt', 'r')
data = list(map(int, f.readlines()[1:]))
f.close()
cr = {i: data[i] for i in range(1000)}
meta = [[i] for i in range(1000)]
newid = 1000
while len(cr) > 2:
    k1 = min(cr, key=cr.get)
    w1 = cr.pop(k1)
    k2 = min(cr, key=cr.get)
    w2 = cr.pop(k2)
    cr[newid] = w1+w2
    newid += 1
    meta += [meta[k1]+meta[k2]]
byte = [0]*1000
for i in meta:
    for j in i:
        byte[j] += 1
print(max(byte), min(byte))

f = open('mwis.txt', 'r')
path = list(map(int, f.readlines()))
f.close()
mwis = [0]*1001
solution = [[] for i in range(1001)]
mwis[0] = 0
mwis[1] = path[1]
solution[1] = [1]
for i in range(2, 1001):
    mwis[i] = max(mwis[i-2]+path[i], mwis[i-1])
    if mwis[i-2]+path[i] > mwis[i-1]:
        solution[i] = solution[i-2]+[i]
    else:
        solution[i] = solution[i-1].copy()
ans = solution[-1]
ask = [1, 2, 3, 4, 17, 117, 517, 997]
ans = ['1' if i in solution[-1] else '0' for i in ask]
print(''.join(ans))
