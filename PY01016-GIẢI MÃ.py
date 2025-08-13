t = int(input())
for _ in range(t):
    s = input()
    res = ""
    i = 0
    while i < len(s):
        if s[i].isalpha():
            char = s[i]
            i += 1
            if i < len(s) and s[i].isdigit():
                res += char * int(s[i])
                i += 1
        else:
            i += 1
    print(res)
