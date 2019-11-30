n = int(input("Enter number of terms"))
T = [0]*n

if n>2:
    T[0] = T[0]=0
    T[2] = 1
    for i in range(3,n):
        T[i] = T[i-1] + T[i-2] + T[i-3];

elif n==2:
    T[0] = 0
    T[1] = 0
else:
    T[0]=0
    
for i in T:
    print(i,end=" ")

