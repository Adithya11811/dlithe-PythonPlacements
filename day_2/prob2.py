#2. develop a python program to convert a binary number into decimal, octal and hexadecimal numbers using functions

def binary_to_decimal(nstr):
    temp = nstr
    i = 0
    val = 0
    while len(nstr) >0:
        val += int(nstr[len(nstr)-1]) * (2** i)
        i+=1
        nstr = nstr[0: len(nstr)-1]

    return val

def convHD(n):
    if n<9:
        return n
    elif n == 10:
        return 'A'
    elif n== 11:
        return  'B'
    elif n==12:
        return  'C'
    elif n==13:
        return 'D'
    elif n==14:
        return 'E'
    elif n==15:
        return 'F'
    else:
        return "ERROR"

def binary_to_octal(nstr):
    new_str = ""
    cnt = len(nstr)
    while cnt%3!=0:
        new_str+="0"
        cnt+=1
    new_str+=nstr

    n = 0
    li = []
    for i in range(0, cnt, 3):
        temp = ""
        for j in range(i, i+3):
            temp+=new_str[j]

        li.append(temp)

    val = ""
    for i in range(len(li)):
        val += str(binary_to_decimal(li[i]))
    return val


def binary_to_hexadecimal(nstr):
    new_str = ""
    cnt = len(nstr)
    while cnt%4!=0:
        new_str+="0"
        cnt+=1
    new_str+=nstr

    n = 0
    li = []
    for i in range(0, cnt, 4):
        temp = ""
        for j in range(i, i+4):
            temp+=new_str[j]

        li.append(temp)

    val = ""
    for i in range(len(li)):
        val += str(convHD(binary_to_decimal(li[i])))
    return val

n = input("ENTER A BINARY NUMBER ")
n = n.strip()
print(f"DECIMAL VALUE of {n} is ",binary_to_decimal(n))
print(f"OCTAL VALUE of {n} is ",binary_to_octal(n))
print(f"HEXADECIMAL VALUE of {n} is ",binary_to_hexadecimal(n))
