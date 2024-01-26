def fun(a,b):
    yield(a+b)
    yield(a*b)
out=fun(3,4)
print(list(out))  