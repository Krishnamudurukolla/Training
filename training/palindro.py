def palin(n):
    s=0
    while n:
        r=n%10
        s=(s*10)+r
        n//=10
    return s
n = int(input()) 
t=n
while True:
    su = palin(n)
    if su==n:
        print(n)
        break
    else:
        n+=1
        t=n