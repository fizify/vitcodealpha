num1=0; num2=1; num3=1;
n=int(input())

if n==1:
    print(num1)
elif n==2:
    print(num1,num2)
elif n==3:
    print(num1,num2,num3)
else:
    print(num1,num2,num3,end=' ')
    for i in range(3,n):
        temp = num1 + num2 + num3
        num1 = num2
        num2 = num3
        num3 = temp
        print(num3,end=' ')
