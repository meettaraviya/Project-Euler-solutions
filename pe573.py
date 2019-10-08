n = 1000000
ans = 0.0
# for i in range(1, n+1):
num = 1
den = 1
for j in range(n):
    # if j%1000 == 0:
    #     print(j//1000)

    if num > 1e25 and isinstance(num, int):
        num //= int(1e15)
        den //= int(1e15)
        # print(num)
        # print(den)
        # input()
        # num = float(num)
        # den = float(den)
        # print(num)
        # print(den)
        # input()
    if num/den < 1e-10:
         break

    num *= (n-j)
    den *= n
    ans += num / den

print(ans)