l=list(map(int,input().split()))
c=1
w=l[0]
for i in range(1,len(l)):
    if l[i]==l[i-1]:
        c+=1
    else:
        if c!=0:
            c-=1
        if c==0:
            w=l[i]
print(w)