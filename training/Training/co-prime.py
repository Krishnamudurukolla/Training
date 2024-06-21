import math
a=int(input())
b=int(input())
x=math.gcd(a,b)
if x==1:
    print("co-prime")
else:
    print("not a co-prime")
'''
for i in range(2,min(a,b)+1):
    if (a%i==0 and b%i==0):
        '''