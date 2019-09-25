"""
2-sum
"""

f = open('algo1-programming_prob-2sum.txt', 'r')
data = list(map(int, f.readlines()))

delta = 9999999
h = {}
for i in range(-delta, delta+1):
    h[i] = []

data = list(set(data))

for i in data:
    h[i//10000] += [i]

t = []
for i in range(-delta, delta+1):
    if len(h[i]) > 0:
        find = h[-i-2]+h[-i-1]+h[-i]+h[-i+1]
        for x in h[i]:
            for y in find:
                if x != y and abs(x+y) <= 10000 and x+y not in t:
                    t += [x+y]

print(len(t))
