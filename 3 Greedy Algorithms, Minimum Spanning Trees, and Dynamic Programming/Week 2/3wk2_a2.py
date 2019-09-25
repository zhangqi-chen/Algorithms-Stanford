"""
k-clustering
"""

f = open('clustering_big.txt', 'r')

f.readline()
ls = f.readline()
graph = []
while ls:
    graph += [ls[:-1].replace(' ', '')]
    ls = f.readline()
f.close()

graph = list(set(graph))
N = len(graph)
gn = [int(i, 2) for i in graph]


def nb(v):
    n = 24
    data = []
    for i in range(n):
        s = list(v)
        s[i] = '1' if s[i] == '0' else '0'
        data += [int(''.join(s), 2)]
        for j in range(i+1, n):
            ss = s.copy()
            ss[j] = '1' if ss[j] == '0' else '0'
            data += [int(''.join(ss), 2)]
    return data


uf = {i: i for i in gn}
rank = {i: 0 for i in gn}


def find(i):
    global uf
    if uf[i] == i:
        return i
    elif uf[uf[i]] == uf[i]:
        return uf[i]
    else:
        newi = uf[i]
        while uf[newi] != newi:
            newi = uf[newi]
        uf[i] = newi
        return newi


def merge(i, j):
    global uf, rank
    i, j = find(i), find(j)
    if i != j:
        if rank[i] > rank[j]:
            uf[j] = i
        elif rank[i] < rank[j]:
            uf[i] = j
        else:
            uf[j] = i
            rank[i] += 1


for s in range(N):
    if s % 10000 == 0:
        print('scan %i, size=%i' % (s+1, len(set(uf.values()))))
    for vn in nb(graph[s]):
        if vn in uf:
            merge(gn[s], vn)

for i in uf:
    find(i)
print('DONE, cluster size=%i' % len(set(uf.values())))
