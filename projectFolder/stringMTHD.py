# name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

# .find/.rfind will return a -1 (because 0 is the starting point) if nothing matches
# result = len(name) # length of a string (not starting from 0)
# result = name.find(" ") # indexes begin at 0, find finds specific characters in a string
# result = name.rfind("e") # rfind is reverse find, it will find the last occurrence or return
# name = name.capitalize() # will capitalize the first letter in a string
# name = name.upper() # will capitalize everything in the string
# name = name.lower() # obv makes string lowercase
# result = name.isdigit() # will return true or false depending on if the string is only digits
# result = name.isalpha() # will return boolean if string contains only alphabetical characters (excluding spaces)
# result = phone_number.count("-") # will count how many of a character in a string
phone_number = phone_number.replace("-", " ") # very important, replaces ofc, string can be empty

print(phone_number)

# print(help(str)) # a bunch of useful tools!