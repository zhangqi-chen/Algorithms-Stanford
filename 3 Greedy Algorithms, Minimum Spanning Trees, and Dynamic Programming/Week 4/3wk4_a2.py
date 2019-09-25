"""
Knapsack algorithm 2
"""

f = open('knapsack_big.txt', 'r')
f.readline()
ls = f.readline()
v = []
w = []
while ls:
    data = list(map(int, ls.split(' ')))
    v += [data[0]]
    w += [data[1]]
    ls = f.readline()
f.close()
Wall = 2000000
N = 2000

solution = [[N, Wall]]
ans = solution[0]
soludic = {(N, Wall): 0}
i = 0
ni = N
while True:
    ni, wi = ans
    x, y = [ni-1, wi], [ni-1, wi-w[ni-1]]
    if ni >= 1:
        if tuple(x) not in soludic:
            solution += [x]
            soludic[tuple(x)] = 0
        if wi >= w[ni-1]:
            if tuple(y) not in soludic:
                solution += [y]
                soludic[tuple(y)] = 0
    i += 1
    if i == len(solution):
        break
    else:
        ans = solution[i]
    if i % 1000000 == 0:
        print(i)

nn = len(solution)
for i in list(range(nn))[::-1]:
    ni, wi = solution[i]
    if i % 1000000 == 0:
        print(i)
    if ni == 0:
        continue
    soludic[(ni, wi)] = max(soludic[(ni-1, wi)], soludic[(ni-1), wi-w[ni-1]]+v[ni-1]) if wi >= w[ni-1] else soludic[(ni-1, wi)]
print(soludic[(N, Wall)])
