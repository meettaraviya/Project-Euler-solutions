from fractions import Fraction

f = (3,7)

f0 = ((3000000)//7, 1000000)

fracs = [Fraction(*f0)]

for d in range(7,1000000):
    
    n = (3*d)//7
    
    if f0[1]*n>d*f0[0] and not d%7==0:
        fracs.append(Fraction(n,d))

fracs = sorted(fracs)

print(fracs[-10:])