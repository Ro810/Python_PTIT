P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    line = input().strip()
    if not line:
        continue
    k_s = line.split()
    k = int(k_s[0])
    if k == 0:
        break
    s = k_s[1]
    res = ""
    for c in s:
        idx = P.index(c)
        res += P[(idx + k) % 28]
    print(res[::-1])
