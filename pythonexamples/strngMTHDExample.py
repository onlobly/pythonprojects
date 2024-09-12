# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

print("username must be more than 4 but less than 12 characters, and must not include spaces or digits.") # trying to find a better way to word this!!!
username = input("Enter a username: ")

if len(username) > 12:
    print(f"{username} is more than 12 characters!")
elif len(username) < 4:
    print(f"{username} is too short!")
elif not username.find(" ") == -1: # if the result is not negative, meaning there is a space, return next message
    print(f"{username} contains a space!")
elif not username.isalpha(): # if the result is not alpha, meaning only text characters, return next message
    print(f"{username} contains numbers!")
else:
    print(f"Welcome, {username}!")
