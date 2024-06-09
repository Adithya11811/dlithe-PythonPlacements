# leap year
n = int(input("Enter a year"))
if n %4 == 0:
    if n% 100 == 0:
        if n%400 == 0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("leap year")
else:
    print("Not a leap year")
