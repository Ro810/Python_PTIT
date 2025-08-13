def check(n):
    s = str(n)
    total = sum(int(c) for c in s)
    if total % 10 != 0:
        return False
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) != 2:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    if check(n):
        print('YES')
    else:
        print('NO')
