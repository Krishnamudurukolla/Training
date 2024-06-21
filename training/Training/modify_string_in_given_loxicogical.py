n = int(input())
for i in range(n):
    result = ''
    order = input()
    string = input()
    for char in order:
        if char in string:
            result += char
    print('Output',result,end = '\n\n')
    '''2
polikujmnhytgbvfredcxswqaz
abcd
qwrbupcsfoghjkldezxvpintma
activedoc'''