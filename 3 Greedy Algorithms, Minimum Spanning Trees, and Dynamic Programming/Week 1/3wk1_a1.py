"""
Greedy algorithms
"""

f = open('jobs.txt', 'r')

data = []
f.readline()
ls = f.readline()
while ls:
    data += [list(map(int, ls.split(' ')))]
    ls = f.readline()
f.close()


def getdata(a):
    return [i.copy() for i in a]


jobs1 = getdata(data)
jobs1.sort(key=lambda x: x[0], reverse=True)
jobs1.sort(key=lambda x: x[0]-x[1], reverse=True)
c1, l1 = 0, 0
for j in jobs1:
    l1 += j[1]
    c1 += l1*j[0]

jobs2 = getdata(data)
jobs2.sort(key=lambda x: x[0]/x[1], reverse=True)
c2, l2 = 0, 0
for j in jobs2:
    l2 += j[1]
    c2 += l2*j[0]

f = open('edges.txt', 'r')
graph = []
for i in range(500):
    graph += [{}]
f.readline()
ls = f.readline()
while ls:
    edge = list(map(int, ls.split(' ')))
    graph[edge[0]-1][edge[1]] = edge[2]
    graph[edge[1]-1][edge[0]] = edge[2]
    ls = f.readline()
f.close()

X = [1]
G = list(range(2, 501))
tree = 0
while len(G) > 0:
    newx, newl = 0, 0
    for vx in X:
        for eg in graph[vx-1]:
            if eg in G:
                if newx == 0 or graph[vx-1][eg] < newl:
                    newx, newl = eg, graph[vx-1][eg]
    tree += newl
    X += [newx]
    G.remove(newx)

print('Answers: %i, %i, %i' % (c1, c2, tree))
