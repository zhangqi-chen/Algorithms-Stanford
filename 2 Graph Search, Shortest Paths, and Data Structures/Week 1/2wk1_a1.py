"""
Strongly Connected Component (SCC) Search
"""

f = open('SCC.txt', 'r')
N = 875714
graph = []
graph_r = []
for i in range(N):
    graph += [[]]
    graph_r += [[]]
ls = f.readline()
while ls:
    data = list(map(int, ls.split(' ')[:-1]))
    ls = f.readline()
    if data[0] == data[1]:
        continue
    graph[data[0]-1] += [data[1]]
    graph_r[data[1]-1] += [data[0]]
f.close()


def create(g):
    return [i.copy() for i in g]


g1 = create(graph)
g2 = create(graph_r)


def DFS(g, i):
    global t, s, ex, f, leader, N
    i -= 1
    ex[i] = True
    leader[i] = s
    if len(g[i]) > 1:
        for j in g[i][1:]:
            if not ex[j-1]:
                DFS(g, j)
    t += 1
    f[i] = t
    print('V %i t= %i' % (i+1, t))


m = 0


def record(i):
    global t, m
    if t >= m*100000:
        print('Point %i t=%i' % (i+1, t))
        m += 1


def tdone(g, i):
    global f, t, leader, s, ex
    i -= 1
    for j in g[i]:
        if not ex[j-1]:
            ex[j-1] = True
            leader[j-1] = s
            return j
    t += 1
    f[i] = t
    record(i)
    return 0


def DFS_loop(g):
    global t, s, ex, f, N
    for i in list(range(N))[::-1]:
        if not ex[i]:
            s = i+1
            ex[i] = True
            leader[i] = s
            exlist = [i+1]
            while True:
                if len(exlist) == 0:
                    break
                j = tdone(g, exlist[-1])
                if j == 0:
                    exlist.pop(-1)
                else:
                    exlist += [j]


t = 0
s = None
ex = [False]*N
f = [0]*N
leader = [0]*N
print('Loop 1')
DFS_loop(g2)

for i in range(len(g1)):
    for j in range(len(g1[i])):
        g1[i][j] = f[g1[i][j]-1]

t = 0
ex = [False]*N
f = [0]*N
leader = [0]*N
print('Loop 2')
m = 0
DFS_loop(g1)

sccdic = {}
for i in leader:
    if i in sccdic:
        sccdic[i] += 1
    else:
        sccdic[i] = 1

sccrank = list(sccdic.values())
sccrank.sort(reverse=True)
print(sccrank[:5])
