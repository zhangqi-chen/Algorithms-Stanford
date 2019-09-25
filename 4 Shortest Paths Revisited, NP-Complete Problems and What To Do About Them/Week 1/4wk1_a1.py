"""
Shortest Path
"""

import numpy as np


def readgraph(file):
    f = open(file, 'r')
    f.readline()
    g = {i: {} for i in range(1, 1001)}
    ls = f.readline()
    while ls:
        data = list(map(int, ls.split(' ')))
        g[data[0]][data[1]] = data[2]
        ls = f.readline()
    f.close()
    return g


g1 = readgraph('g1.txt')
g2 = readgraph('g2.txt')
g3 = readgraph('g3.txt')


def askmin(g):
    n = 1000
    A = np.zeros([n, n, n])
    for i in range(n):
        for j in range(n):
            A[i, j, 0] = 0 if i == j else g[i+1][j+1] if j+1 in g[i+1] else np.inf
    for k in range(1, n):
        if k % 100 == 0:
            print(k)
        for i in range(n):
            for j in range(n):
                A[i, j, k] = min(A[i, j, k-1], A[i, k, k-1]+A[k, j, k-1])
    for i in range(n):
        if A[i, i, n-1] < 0:
            print('error at %i' % (i+1))
    print('min=%i' % A[:, :, n-1].min())


print('g1')
askmin(g1)
print('g2')
askmin(g2)
print('g3')
askmin(g3)
