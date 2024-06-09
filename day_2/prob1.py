#1. write a python program to find the best of 2 test average marks out of 3 tests marks accepted from the user

marks_str = input("Enter the marks in the 3 subjects seperated by a space ")

marks = marks_str.split(' ')
li = []
for i in range(0, len(marks)):
    if len(marks[i]) != 0 :
        li.append(int(marks[i]))

li.sort()
print(f"the top 2 scores are {li[2]} and {li[1]}")