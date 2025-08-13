def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

t = int(input())
for _ in range(t):
    n = input()
    m = n[::-1]
    if gcd(int(n), int(m)) == 1:
        print("YES")
    else:
        print("NO")
