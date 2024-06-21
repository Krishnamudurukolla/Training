l=list(map(int,input().split()))
ans=0
def is_prime(n):
    if n<2:
        return False
    for  num in range(2, int(n**(1/2))+1):
        if not n%num:
            return False
    return True
for i in range(1,len(l)):
    if l[i]>l[i-1]:
        mx=l[i]
        mn=l[i-1]
    else:
         mn=l[i-1]
         mx=l[i]
    for num in range(mx,mn-1,-1):
        if is_prime(num):
            ans+=num
            break
print(ans)