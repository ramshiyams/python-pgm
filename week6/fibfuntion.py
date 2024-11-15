def fib(num):
    a=0
    b,c=1,1
    print(a)
    for i in range(num-1):
        print(c)
        c=a+b
        a=b
        b=c  
fib(10)
