'''s=input
l=[]
for i in range(len(s)):
    if s[i]=='(' or s[i]=='{' or s[i]=='{':
        l.append(s[i])
    elif s[i]=='}' and l[-1]=='{':
        l.pop()
    elif s[i]==')' and l[-1]==')':
        l.pop()
    elif s[i]==']' and l[-1]==']':
        l.pop()
print(l)
if not l:
    print(-1)
else:
    print("not")'''
a=input()
f=0
c=0
for i in a:
    if(i in '{[('):
        s.append(i)
    elif(not s):
        if(i =='}' and s[-1]=='{' or i==']' and s[-1]==']' or i=='(' and s[-1]==')'):
            s.pop()
        else:
            print(c)
            f=1
            break
    else:
        print(c)
        f=1
        
