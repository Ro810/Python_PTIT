t = int(input())
for _ in range(t):
    n = int(input())
    x = 10
    while n >= x:
        n = (n + (x // 2)) // x * x
        x *= 10
    print(n)
