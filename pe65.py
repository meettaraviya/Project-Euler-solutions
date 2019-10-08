fracs = [2]

while len(fracs)<100:
    if len(fracs)%3 in [0,1]:
        fracs.append(1)
    else:
        fracs.append(((len(fracs)+1)*2)//3)

print(fracs)

n=1
d=0


def gcd(a,b):
    if a<b:
        return gcd(b,a)
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)


for f in fracs[::-1]:
    n,d = d,n
    n += f*d

print(sum(map(int,str(n))))