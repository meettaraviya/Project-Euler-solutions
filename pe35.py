import itertools

primes = set()
non_primes = set([1])

def is_prime(p):
    if p in primes:
        return True
    elif p in non_primes:
        return False
    for i in range(2,p):
        if p%i==0:
            non_primes.add(p)
            return False
    primes.add(p)
    return True

none_circular_primes = set()

def is_circular_prime(p):
    global count, none_circular_primes
    if p>5 and '0' in str(p) or '2' in str(p) or '4' in str(p) or '6' in str(p) or '8' in str(p) or '5' in str(p):
        return False  
    if p in none_circular_primes:
        return False
    not_circular_prime = False
    sp = str(p)+str(p)
    d = len(sp)//2
    for i in range(d):
        perm = sp[i:i+d]
        if not is_prime(int(''.join(perm))):
            not_circular_prime = True
            break
    if not_circular_prime:
        for i in range(d):
            perm = sp[i:i+d]
            none_circular_primes.add(int(''.join(perm)))
        return False
    else:
        print(p)
        return True

count = 4

for i in range(10,1000000):
    # if i%1000==0:
    #     print(i, count) 
    if is_circular_prime(i):
        count += 1

print()
print(count)
    
