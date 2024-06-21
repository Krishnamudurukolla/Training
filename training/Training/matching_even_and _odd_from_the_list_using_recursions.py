l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
n1, n2 = len(l1), len(l2)
ans = []
def match(i = 0, j = 0):
    #print(i,j)
    if i>=n1:
        return
    if j>=n1:
        match(i + 1, 0)
    elif not l1[i] & 1:
        if l2[j] & 1:
            ans.append(l1[i] + l2[j])
        match(i, j + 1)
    else:
        if l2[j] & 1:
            match(i + 1, j)
        else:
            match(i + 1, j + 1)
match()
print(ans)