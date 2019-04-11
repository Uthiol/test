def mysum(i):
    a=0
    b=0
    while b<=i:
        a=a+b
        b+=1
    return a

def mysumgauss(i):
    return ((i*(i+1))//2)

def check(n):
    for i in range(n):
        assert(mysum(i)==mysumgauss(i))

