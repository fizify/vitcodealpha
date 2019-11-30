def trib(n):
    if n < 3:
        return n
    return trib(n-1) + trib(n-2) + trib(n-3)

def tri(n):
    result = []
    for i in range(0,n):
        result.append(trib(n))
    return result

n= int(input('n:'))
print(tri(n))
