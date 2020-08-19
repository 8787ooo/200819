s = []
na = []
ma = 0
man = 0
mi = 100
mim = 0
to = 0

for i in range(5):
    na = input('name')
    n = int(input('score:'))
    s.append(n)
    if n > ma:
        ma = n
        man = na
    if n < mi:
        mi = n
        mim = na
    to += n
h = to/len(s)
print('total',to)
print('平',h)
print('high',ma,'name',man)
print('low',mi,'name',mim)
