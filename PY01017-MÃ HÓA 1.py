t = int(input())
for _ in range(t):
    s = input()
    res = ""
    char = s[0]
    cnt = 0
    for c in s:
        if c == char:
            cnt += 1
        else:
            res += str(cnt) + char
            char = c
            cnt = 1
    print(res + str(cnt) + char)
