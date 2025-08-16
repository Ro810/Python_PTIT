def solve(n):
    s = str(n)
    if len(s) % 2 == 0:
        print("NO")
        return
    if s[0] == s[1]:
        print("NO")
        return
    for i in range(0, len(s) - 2, 2):
        if s[i] != s[i + 2]:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
