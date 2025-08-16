def nguyento(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    s = str(n)
    if not nguyento(len(s)):
        print("NO")
        return
    cnt = 0
    for i in range(len(s)):
        if nguyento(int(s[i])):
            cnt += 1
    if cnt > len(s) - cnt:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
