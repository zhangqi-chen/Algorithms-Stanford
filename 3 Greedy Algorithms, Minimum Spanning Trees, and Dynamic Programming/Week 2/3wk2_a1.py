"""
k-clustering
"""

f = open('clustering1.txt', 'r')

graph = {}
f.readline()
ls = f.readline()
while ls:
    data = list(map(int, ls.split(' ')))
    graph[(data[0], data[1])] = data[2]
    ls = f.readline()
f.close()

g = graph.copy()

c = list(range(1, 501))
cnum = 500
while True:
    edge = min(g, key=g.get)
    d = g.pop(edge)
    l1, l2 = c[edge[0]-1], c[edge[1]-1]
    if l1 != l2 and cnum > 4:
        cnum -= 1
        for i in range(500):
            c[i] = l1 if c[i] == l2 else c[i]
    elif l1 != l2 and cnum == 4:
        print(edge, l1, l2, d)
        break
