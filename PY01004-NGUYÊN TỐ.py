def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            cnt += 1
    if prime(cnt):
        print("YES")
    else:
        print("NO")

