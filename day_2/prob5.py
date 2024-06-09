# 5. write a pyton program that accepts a sentence and finds the number of words, digits, uppercase letters and lowercase letters
w_count = 0
sent = input("Enter a sentence")

w= sent.strip().split(' ')
w_count = len(w)

digits = 0
letters= 0
upcs = 0
lcs = 0

for i in range(0, len(sent)):
    if sent[i].isdigit():
        digits+=1
    elif sent[i].isalpha():
        letters+=1
        if sent[i].islower():
            lcs+=1
        elif sent[i].isupper():
            upcs+=1

print("word count", w_count)
print("digit count",digits)
print("letter count",letters)
print("lowercase letters",lcs)
print("uppercase letters", upcs)