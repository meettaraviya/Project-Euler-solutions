i = 1
for j in range(1, 101):
    i *= j
print(sum([int(c) for c in str(i)]))