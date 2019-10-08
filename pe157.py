from sympy import ntheory

count = 0

for n in range(1, 3):

    denom = 10**n
    
    for i in range(n+1):
        a = 2**i
        a_inv = 2**(n-i)
        for j in range(n+1):
            b = 5**j
            b_inv = 5**(n-j)
            p = (a+b)*a_inv*b_inv

            divisors = ntheory.factor_.divisors(p)

            for d in divisors:
                count += 1
                print(count, a*d, b*d, p//d)

    for i in range(1, n+1):
        a = 1
        b = 10**i
        b_inv = 10**(n-i)
        p = (a+b)*b_inv

        divisors = ntheory.factor_.divisors(p)

        for d in divisors:
            count += 1
            print(count, a*d, b*d, p//d)