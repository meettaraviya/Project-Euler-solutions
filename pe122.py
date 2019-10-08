m = [0, 0, 1]

calc = [[[0,1]], [[0,1]], [[0,1,2]]]

def union(A,B):
    i = 0
    j = 0
    C = list()
    while i<len(A) and j<len(B):
        if A[i]<B[j]:
            C.append(A[i])
            i += 1
        elif A[i]>B[j]:
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1
            j += 1
    
    if i==len(A):
        C.extend(B[j:])
    else:
        C.extend(A[i:])
    return C

def len_union(A,B):
    l = 0
    i = 0
    j = 0
    C = list()
    while i<len(A) and j<len(B):
        if A[i]<B[j]:
            l += 1
            i += 1
        elif A[i]>B[j]:
            l += 1
            j += 1
        else:
            l += 1
            i += 1
            j += 1
    
    if i==len(A):
        l += len(B)-j
    else:
        l += len(A)-i
    return l




for i in range(3,201):
    mi = 201
    minj = 1
    for j in range(1,i):
        for a in calc[j]:
            for b in calc[i-j]:
                lu = len_union(a,b)
                nl = lu+1
                if  nl < mi:
                    # newcalc = [sorted(u+[i])]
                    mi = nl
                    minj = j
                # elif nl==mi:
                #     newcalc.append(sorted(u+[i]))
    
    newcalc = []
    for j in range(minj,i):
        for a in calc[j]:
            for b in calc[i-j]:
                u = union(a,b)
                nl = len(u)+1
                if nl==mi:
                    newcalc.append(sorted(u+[i]))

    m.append(mi)
    print(i, mi, len(newcalc))
    calc.append(newcalc)

for i in range(201):
    print(i,m[i], calc[i])

print(sum(m))