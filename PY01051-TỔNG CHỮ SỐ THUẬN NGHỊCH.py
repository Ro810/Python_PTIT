def thuannghich(n):
    return str(n) == str(n)[::-1]

def solve(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    if len(str(sum)) < 2:
        print("NO")
        return
    if thuannghich(sum):
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
