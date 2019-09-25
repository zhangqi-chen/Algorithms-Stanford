"""
Traveling salesman problem
"""

import numpy as np
from itertools import combinations

f = open('tsp.txt', 'r')
ls = f.readlines()[1:]
graph = [list(map(float, i.split(' '))) for i in ls]


def dis(i, j):
    return np.sqrt((graph[i][0]-graph[j][0])**2+(graph[i][1]-graph[j][1])**2)


N = len(graph)
dic1 = {frozenset([0]): {0: 0}}

for m in range(1, N):
    comb = list(combinations(range(1, N), m))
    dic2 = {frozenset(comb[i]): {list(comb[i])[j]: 0 for j in range(m)} for i in range(len(comb))}
    print(m, len(dic2))
    for s in dic2:
        for j in s:
            ans = []
            if m == 1:
                dic2[s][j] = dis(0, j)
            else:
                sj = set(s)
                sj.remove(j)
                dic2[s][j] = min([dic1[frozenset(sj)][k]+dis(k, j) for k in sj if k != j])
    dic1 = dic2.copy()

tsp = min([dic2[frozenset(comb[0])][j]+dis(0, j) for j in range(1, N)])
print(tsp)
