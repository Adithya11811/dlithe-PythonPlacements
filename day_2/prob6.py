#1. write a program to read a string from user and implement the logic to remove the characters
#   which are at the odd no's of the index

sent = input("Enter a string ")
new_str = ""
for i in range(1,len(sent),2):
    new_str+=sent[i]

print(new_str)