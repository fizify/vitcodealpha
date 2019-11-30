l=[0,1,1]
n=int(input("Enter number of terms to be displayed"))
if n<=3:
    for i in range(n):
        print(l[i], end=" ")
else:
    for i in range(3,n):
        a=l[i-3]
        b=l[i-2]
        c=l[i-1]
        d=a+b+c
        l.append(d)
    for i in range(n):
        print(l[i], end=" ")
