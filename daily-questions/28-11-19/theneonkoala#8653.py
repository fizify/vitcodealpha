fib=lambda x:x if x<2 else fib(x-1)+fib(x-2)+fib(x-3)
print(fib(int(input())))
