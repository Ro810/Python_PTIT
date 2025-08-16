def nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    ans = 1
    while n:
        tmp = n % 10
        if tmp != 0:
            ans *= tmp
        n //= 10
    print(ans)

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
