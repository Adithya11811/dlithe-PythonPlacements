#3. define a function Fn as Fn = Fn-1 + Fn-2. write a python program that accepts a value for N where N>0 as input and pass this value to the function. Display the suitable error for input value is not followed

def Fn(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fn(n-1) + Fn(n-2)


n = int(input("Enter a number "))
if n<0:
    raise "Error not possible for negative number"
else:
    ans = Fn(n)
    print(ans)