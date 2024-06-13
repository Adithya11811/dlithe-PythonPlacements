def fun(x, y=40):
    print("x: ",x)
    print("y: ",y)

fun(30)

def fun(**kwargs):
    print(kwargs)

fun(a="20", b=57)


def myFun1(*argv):
    print(argv)

myFun1("Hello", "John", "Snow")


cube  = lambda x: x**3

print(cube(2))


def power(N,p):
    if p == 0:
        return 1
    
    return (power(N, p-1)*N)

N = 5
p = 2
print(power(5,2))