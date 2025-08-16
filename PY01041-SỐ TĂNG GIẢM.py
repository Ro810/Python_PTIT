def solve(n):
    s = str(n)
    if len(s) < 3:
        print("NO")
        return
    i = 0
    while i + 1 < len(s) and s[i] < s[i + 1]:
        i += 1
    if i == 0 or i == len(s) - 1:
        print("NO")
        return
    while i + 1 < len(s) and s[i] > s[i + 1]:
        i += 1
    if i == len(s) - 1:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
