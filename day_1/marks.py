#for conditional statements read the marks of the student; if it's  > 80 distinc, 60-80 pass, <60 fail else invalid
marks = int(input("Enter your marks: "))
print()
if marks >= 80:
    print("Distinction")
elif marks >= 60 and marks < 80:
    print("PASS")
elif marks < 60:
    print("Fail")
else:
    print("Invalid")
