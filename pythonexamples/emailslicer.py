
email = input("Enter your email: ")

index = email.index("@") # returns number of characters in that the index first appears at

username = email[:index] # will make whole string for after whatever the index =
domain = email[index + 1:] # will start after the @ symbol

print(f"Your username is {username} and domain is {domain}")
# calebmmccraney@gmail.com

# could be written :
#       username = email[:email.index("@")] # ends at the @ and its exclusive
#       domain = email[email.index("@") + 1:] # + 1 because start is inclusive