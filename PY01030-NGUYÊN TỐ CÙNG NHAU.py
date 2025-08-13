def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, k = map(int, input().split())
cnt = 0
for i in range(pow(10, k - 1), pow(10, k)):
    if gcd(n, i) == 1:
        cnt += 1
        print(i, end = ' ')
    if cnt == 10:
        print()
        cnt = 0
