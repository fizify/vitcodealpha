rot=list(list(map(int(input().split())) for i in range(int(input())))
print(list(i[::-1] for i in zip(*rot)))
