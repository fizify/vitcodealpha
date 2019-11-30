def trib(n):
    a,b,c = 0,1,1
    for i in range(n):
        yield (a)
        a,b,c = b,c,(a+b+c)
m = int(input())
f = trib(m)
for i in range(m):
    print(next(f),end=' ')
