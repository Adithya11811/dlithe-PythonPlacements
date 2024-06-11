# 9. write a program to partition a list around the given value such that all elements less than the given value come before it and all elements greater than the given value comes after it

li = [1,9,8,3,5,21,7,4,17,14,6,1,2,2]

p_val = 7

left_li= []
right_li =[]

for x in li:
    if p_val < x:
        right_li.append(x)
    elif p_val >x:
        left_li.append(x)

left_li.append(p_val)
left_li.extend(right_li)

print(left_li)