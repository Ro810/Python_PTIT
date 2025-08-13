def thuannghich(n):
    s = str(n)
    return s == s[::-1]

def check(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    for i in range(len(s)):
        if s[i] != '0' and s[i] != '2' and s[i] != '4' and s[i] != '6' and s[i] != '8':
            return False 
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(22, n): 
        if thuannghich(i) and check(i):
            print(i, end=' ')
    print()  
            
