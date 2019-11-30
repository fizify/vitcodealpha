n= int(input("n: "))

terms=[0]
for i in range(n):
    l=len(terms); terms.append(1) if len(terms)<=2 else terms.append(terms[l-1]+terms[l-2]+terms[l-3])

print(terms)
