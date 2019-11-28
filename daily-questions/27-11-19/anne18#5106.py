n=int(input("Enter dimension"))
a=[];new=[]
for i in range(n):
    l=[];l1=[]
    for j in range(n):
        l.append(int(input()))
        l1.append(0)
    a.append(l)
    new.append(l1)
for i in range(n):
    for j in range(n):
        new[j][n-i-1]=a[i][j]
print("old matrix",a)
print("new matrix",new)
