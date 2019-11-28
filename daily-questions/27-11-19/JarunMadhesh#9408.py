n= 1; i =0; matrix= []

while(i<n):
    temp=input().split()
    matrix.append(temp)
    n=len(temp)
    i+=1

for i in range(n):
    for j in range(n):
        print(matrix[n-1-j][i],end=' ')
    print()
