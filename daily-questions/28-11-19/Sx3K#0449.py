a = 1
b = 0
c = 0
i = 0

while True:
    c = a + b
    b = a
    a = c
    if i % 100000 == 0:
        print(c)
    i += 1
