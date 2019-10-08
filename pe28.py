i=1
k=3
N=1001
s=0

while k<=N:
    while i<=k*k:
        if i%(k-1)==1:
            s+=i
            print(i)
        i+=1
    k+=2

print()
print(s)