"""
QuickSort with different pivot
"""

ia = []
f = open('QuickSort.txt', 'r')
ls = f.readlines()
f.close()
ia = [int(i) for i in ls]


def QS1(a):
    if len(a) <= 1:
        return (a, 0)
    pivot = a[0]
    i, j = 1, 1
    n = len(a)-1
    while j < len(a):
        if a[j] > pivot:
            j += 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
    a[0], a[i-1] = a[i-1], a[0]
    a[:i-1], nleft = QS1(a[:i-1])
    a[i:], nright = QS1(a[i:])
    return (a, n+nleft+nright)


def QS2(a):
    if len(a) <= 1:
        return (a, 0)
    pivot = a[-1]
    a[0], a[-1] = a[-1], a[0]
    i, j = 1, 1
    n = len(a)-1
    while j < len(a):
        if a[j] > pivot:
            j += 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
    a[0], a[i-1] = a[i-1], a[0]
    a[:i-1], nleft = QS2(a[:i-1])
    a[i:], nright = QS2(a[i:])
    return (a, n+nleft+nright)


def QS3(a):
    if len(a) <= 1:
        return (a, 0)
    findpivot = [a[0], a[(len(a)-1)//2], a[-1]]
    k = findpivot.copy()
    k.remove(min(k))
    knum = findpivot.index(min(k))
    pivotnum = 0 if knum == 0 else (len(a)-1)//2 if knum == 1 else len(a)-1
    pivot = a[pivotnum]
    a[0], a[pivotnum] = a[pivotnum], a[0]
    i, j = 1, 1
    n = len(a)-1
    while j < len(a):
        if a[j] > pivot:
            j += 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
    a[0], a[i-1] = a[i-1], a[0]
    a[:i-1], nleft = QS3(a[:i-1])
    a[i:], nright = QS3(a[i:])
    return (a, n+nleft+nright)


ia1, ia2, ia3 = ia.copy(), ia.copy(), ia.copy()
ia1, num1 = QS1(ia1)
ia2, num2 = QS2(ia2)
ia3, num3 = QS3(ia3)
