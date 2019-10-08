from math import sqrt

primes = []

for p in range(2,1000000):
    is_prime = True
    for i in range(2,int(sqrt(p))+1):
        if p%i==0:
            is_prime = False
            break
    if is_prime:
        primes.append(p)

maxdiff = 0
best = 0

sprimes = set(primes)

cumsum = []
sum_=0
for p in primes:
    sum_+=p
    cumsum.append(sum_)

print(len(primes))

for i in range(len(primes)):
    if cumsum[min(i+maxdiff, len(primes)-1)]-cumsum[i]>primes[-1]:
        continue
    k = len(primes)-1
    t = cumsum[i]+primes[-1]
    while cumsum[k]>t:
        k -= 1
    for j in range(k,i,-1):
        if j-i<=maxdiff:
            break
        s = cumsum[j]-cumsum[i]
        if s<1000000 and s in sprimes:
            best = s
            maxdiff = j-i

            print(best, maxdiff,i,j)
            break
        elif s<best:
            break
    if i>100 and i%100==0:
        print(i)


print(best, maxdiff)