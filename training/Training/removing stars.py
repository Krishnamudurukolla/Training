s=input()
l=[]
for i in s:
    if i!='*':
        l.append(i)
    elif l:
        l.pop()
print("".join(l))