# write a program to swap 2 no's using third variable

n1 = int(input())
n2 = int(input())
print("old val of n1",n1)
print("old val of n2",n2)

def swapy(n1, n2):
    temp = n1
    n1 = n2
    n2 = temp
    return n1, n2

n1, n2 = swapy(n1,n2)

print()
print("new val of n1",n1)
print("new val of n2",n2)