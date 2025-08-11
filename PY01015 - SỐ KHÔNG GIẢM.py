t = int(input())
for _ in range(t):
    s = input()
    check = True
    for i in range(len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            print("NO")
            check = False
            break
    if check:
        print("YES")
            
