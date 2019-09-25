"""
Min Cut
"""

from random import choice


f = open('kargerMinCut.txt', 'r')
ls = f.readlines()
f.close()
graph = [list(map(int, i.split('\t')[:-1])) for i in ls]


def create():
    global graph
    return [i.copy() for i in graph]


def mincut(g):
    while len(g) > 2:
        c1 = choice(range(len(g)))
        v_del = g.pop(c1)
        c2 = choice(range(1, len(v_del)))
        v1, v2 = v_del[0], v_del[c2]
        while v2 in v_del:
            v_del.remove(v2)
        for i in range(len(g)):
            if g[i][0] == v2:
                g[i] += v_del
                while v1 in g[i]:
                    g[i].remove(v1)
            for j in range(len(g[i])):
                g[i][j] = v2 if g[i][j] == v1 else g[i][j]
    return len(g[0])-1


N = 1000
cut = []
for i in range(N):
    cut += [mincut(create())]

print(min(cut))
