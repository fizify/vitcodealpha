n=int(input())
a=0
b=c=1
d=3
print('0 1 1',end=' ')
while(d!=n):
  e=a+b+c
  print(e, end=' ')
  a=b
  b=c
  c=e
  d+=1
