n = int(input())
def summ(n):
    if not n:
        return 0
    val = summ(n-1)
    return n + val if not n & 1 else val
print(summ(n))