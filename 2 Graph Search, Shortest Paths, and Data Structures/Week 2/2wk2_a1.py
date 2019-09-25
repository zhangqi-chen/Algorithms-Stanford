"""
Dijkstra's shortest path
"""

f = open('dijkstraData.txt', 'r')
N = 200
graph = []
ls = f.readline()
while ls:
    data = ls.split('\t')[:-1]
    v = int(data.pop(0))-1
    graph += [{}]
    for i in data:
        edge = list(map(int, i.split(',')))
        graph[v][edge[0]] = edge[1]
    ls = f.readline()
f.close()

groupX = [1]
path = {1: 0}
groupV = list(range(2, 201))

while len(groupV) > 0:
    new = []
    for x in groupX:
        for edge in graph[x-1]:
            if edge in groupV:
                newpath = graph[x-1][edge]+path[x]
                if new == [] or newpath < new[1]:
                    new = [edge, newpath]
    if len(new) > 0:
        path[new[0]] = new[1]
        groupX += [new[0]]
        groupV.remove(new[0])
    else:
        break

answerx = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
print([path[x] for x in answerx])
