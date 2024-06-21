a = list(map(int,input().split()))
b = list(map(int,input().split()))
def summ(ind = 0, os = 0, es = 0):
    if len(a)==ind:
        return (es, os)
    es += a[ind] if not a[ind] & 1 else 0
    os += b[ind] if b[ind] & 1 else 0
    return summ(ind+1, os, es)
print(summ())