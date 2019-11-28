n = int(input())
r = []
if(n==1):
     r.append(int(input()))
else:
     for i in range(n):
          r.append(list(map(int,input().split())))
     for i in range(0,int(n/2)):
          for j in range(i,n-i-1):
               s = r[i][j]
               r[i][j] = r[n-j-1][i]
               r[n-j-1][i] = r[n-1-i][n-1-j]
               r[n-1-i][n-1-j] = r[j][n-i-1]
               r[j][n-i-1] = s
print(r)
