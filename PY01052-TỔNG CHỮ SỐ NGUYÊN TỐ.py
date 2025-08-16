def nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    if nguyen_to(sum):
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
