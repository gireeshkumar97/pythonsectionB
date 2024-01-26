def fib (n):
    a = 1
    for i in range(n):
        yield a 
        a = a *2
out=fib(10)
print(list(out))
