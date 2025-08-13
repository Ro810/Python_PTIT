def solve(n):
    res = []
    i = 2
    while i * i <= n:
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            res.append(f"{i}^{count}")
        i += 1
    if n > 1:
        res.append(f"{n}^1")
    print("1 * " + " * ".join(res))

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
