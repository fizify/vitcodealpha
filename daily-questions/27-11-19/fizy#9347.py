n= int(input("sq matrix ka power bata: "))
final=[]
for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(input(f"({i},{j}) wala number bata: "))
   
    final.append(temp)

finale=[]
for i in range(n):
    temp=[]
    for j in reversed(range(n):
        temp.append(final[j][i])
    finale.append(temp)

for i in finale:print(i)
