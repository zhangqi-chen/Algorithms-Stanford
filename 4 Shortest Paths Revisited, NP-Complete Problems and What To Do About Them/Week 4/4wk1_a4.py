"""
2-SAT
"""

f = open('2sat6.txt', 'r')
ls = f.readline()
n = int(ls)
N = n*2
graph = {i: [] for i in range(-n, n+1) if i != 0}
graph_r = {i: [] for i in range(-n, n+1) if i != 0}
ls = f.readline()
while ls:
    data = list(map(int, ls.split(' ')))
    graph[-data[0]] += [data[1]]
    graph[-data[1]] += [data[0]]
    graph_r[data[1]] += [-data[0]]
    graph_r[data[0]] += [-data[1]]
    ls = f.readline()
f.close()


def record(i):
    global t, m
    if t >= m*100000:
        print('Point %i t=%i' % (i+1, t))
        m += 1


def tdone(g, i):
    global f, t, leader, s, ex
    for j in g[i]:
        if not ex[j]:
            ex[j] = True
            leader[j] = s
            return j
    t += 1
    t += 1 if t == 0 else 0
    f[i] = t
    record(i)
    return 0


def DFS_loop(g):
    global t, s, ex, f, N
    for i in list(g.keys())[::-1]:
        if not ex[i]:
            s = i
            ex[i] = True
            leader[i] = s
            exlist = [i]
            while True:
                if len(exlist) == 0:
                    break
                j = tdone(g, exlist[-1])
                if j == 0:
                    exlist.pop(-1)
                else:
                    exlist += [j]


t = -n-1
s = None
m = 0
ex = {i: False for i in graph}
f = {i: 0 for i in graph}
leader = {i: 0 for i in graph}
print('Loop 1')
DFS_loop(graph_r)

gnew = {i: [] for i in graph}
for i in graph:
    for j in graph[i]:
        gnew[f[i]] += [f[j]]

fr = {f[i]: i for i in graph}

t = -n-1
m = 0
ex = {i: False for i in graph}
f = {i: 0 for i in graph}
leader = {i: 0 for i in graph}
print('Loop 2')
DFS_loop(gnew)

sccdic = {}
for i in leader:
    if leader[i] in sccdic:
        sccdic[leader[i]] += [fr[i]]
    else:
        sccdic[leader[i]] = [fr[i]]

num = 0
for i in sccdic:
    if len(sccdic[i]) > 1:
        num += 1
        for j in sccdic[i]:
            if -j in sccdic[i]:
                print('error')
                break
        print(sccdic[i])
print(num)
