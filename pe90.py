
allsets = []

for i in range(1024):
    j = 0
    i_ = i
    set_ = []
    while i_>0:
        if i_%2==1:
            set_.append(j)
        i_ //= 2
        j += 1
    if len(set_)==6:
        allsets.append(set_)

print(len(allsets))

squares = set([1,4,9,16,25,36,49,64,81])

count = 0

for i in range(210):
    for j in range(i,210):
        set_a = allsets[i]
        set_b = allsets[j]

        possible = set()
        for a in set_a:
            for b in set_b:
                possible.add(10*a+b)
                possible.add(10*b+a)
                if a in [6,9]:
                    possible.add(60+b)
                    possible.add(90+b)
                    possible.add(10*b+6)
                    possible.add(10*b+9)
                if b in [6,9]:
                    possible.add(60+a)
                    possible.add(90+a)
                    possible.add(10*a+6)
                    possible.add(10*a+9)
        if possible.issuperset(squares):
            print(set_a, set_b)
            count += 1

print(count)


