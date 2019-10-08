from multiset import Multiset

x = Multiset()

for i in range(10**10+1):
    x.update(str(i))

    if i%10000000 == 0:
        print(i)

    for digit, count in x.items():

        if count == i:
            print(digit, i)