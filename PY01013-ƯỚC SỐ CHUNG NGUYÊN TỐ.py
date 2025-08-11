def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    x = gcd(a, b)
    sum = 0
    while x:
        sum += x % 10
        x //= 10
    if is_prime(sum):
        print("YES")
    else:
        print("NO")
