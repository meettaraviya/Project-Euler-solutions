# n_mod = [0 for i in range(250)]
n_ways = [[0 for i in range(250)], [0 for i in range(250)]]

n_ways[0][0] = 1
n_ways[1][0] = 1

mod = 10**16

k = 0

for i in range(1, 250251):
    m = pow(i, i, 250)
    if i%10000==0:
        print(i)
    for j in range(250):
        n_ways[1-k][j] = (n_ways[k][j] + n_ways[k][j-m]) % mod
    k = 1-k

print(n_ways[k][0]-1)