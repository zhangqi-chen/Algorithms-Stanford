import numpy as np
f=open('knapsack1.txt','r')
f.readline()
l=f.readline()
v=[]
w=[]
while l:
    data=list(map(int,l.split(' ')))
    v+=[data[0]]
    w+=[data[1]]
    l=f.readline()
f.close()
Wall=10000
N=100
A=np.zeros([N+1,Wall+1])
for i in range(1,N+1):
    for x in range(0,Wall+1):
        A[i,x]=max(A[i-1,x],A[i-1,x-w[i-1]]+v[i-1]) if x>=w[i-1] else A[i-1,x]
print(A[N,Wall])