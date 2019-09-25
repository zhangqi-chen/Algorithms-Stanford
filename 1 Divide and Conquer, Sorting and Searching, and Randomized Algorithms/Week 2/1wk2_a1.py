"""
Inversions: num of (i, j) in A where i<j and A[i]>A[j]
"""

ia = []
f = open('IntegerArray.txt', 'r')
ls = f.readlines()
f.close()
ia = [int(i) for i in ls]


def inversion(a):
    n = len(a)
    if n == 1:
        return (a, 0)
    else:
        b1, nleft = inversion(a[:n//2])
        b2, nright = inversion(a[n//2:])
        cross = 0
        b = []
        i, j = 0, 0
        while i < len(b1) or j < len(b2):
            if i == len(b1):
                b += b2[j:]
                j = len(b2)
            elif j == len(b2):
                b += b1[i:]
                i = len(b1)
            elif b1[i] < b2[j]:
                b += [b1[i]]
                i += 1
            else:
                b += [b2[j]]
                j += 1
                cross += len(b1)-i
        return (b, nleft+nright+cross)


_, num = inversion(ia)
print(num)
