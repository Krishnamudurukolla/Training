n=[(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
p=[5, 6, 5, 4, 11, 2]
l=[p[0]]
cp=0
for i in range(1,len(n)):
    cp = p[i]
    j=i-1
    while j>=0 and n[j][1]>n[i][0]:
        j-=1
    #print("i=",i,"j=",j)
    if j>=0:
        cp+=l[j]
    #print("cp=",cp,"i=",i)
    l.append(max(cp,p[i-1]))
print(l)