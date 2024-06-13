input_string = input("Enter a string: ")

print("Length of a string: ", len(input_string))

print("Upper Case: ", input_string.upper())
print(input_string.isupper())

print("Lower Case: ", input_string.lower())
print(input_string.islower())

print("Capital case:", input_string.capitalize())
print("Capitalized every word:", input_string.title())

substr = input("Enter a substring to count it's occurences: ")
print("Occurences of", substr," in the string", input_string.count(substr))

Prefix = input("Enter a prefix to check if the string starts with it: ")
print("Starts with", Prefix, ":", input_string.startswith(Prefix))

Suffix = input("Enter a prefix to check if the string starts with it: ")
print("Starts with", Suffix, ":", input_string.endswith(Suffix))

old_substr = input("Enter a old substring to replace: ")
new_substr = input("Enter a new substring to replace: ")
print("After replacement: ", input_string.replace(old_substr, new_substr))

delimiter = input("Enter a delimiter to split the string")
print("splited string: ", input_string.split(delimiter))

substr = input("Enter substrings to join(sep by space): ").split()
join_deli = input("Enter a delimiter to join the substrings: ")
print("Joined string: ", join_deli.join(substr))

print(input_string.strip())

print(input_string.rfind("1"))
print(input_string.rinde("1"))
