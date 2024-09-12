# if = do some code only IF something happens
#   else = do something else
#       must use correct ordering of you ifs, elif, and else!

# age = int(input("Enter your age: "))

# if age >= 100:
    # print("You are too old to sign up.")
# elif age >= 18:
    # print("You are now signed up!")
# elif age < 0:
    # print("You haven't been born yet!")
# else:
    # print("You must be 18+ to sign up.")


# response practice

# response = input("Would you like to subscribe to our newsletter?  (Y/N): ")

# if response == "Y": # this == is the comparison operator, one = is setting what the response is = to!
    # print("You have subscribed to our newsletter!")
# else:
    # print("You have declined the newsletter subscription.")


# name practice

# name = input("Enter your name: ")

# if name == "":
    # print("You did not enter anything.")
# else:
    # print(f"Hello {name}!")


# booleans and ifs

# for_sale = True

# if for_sale:
    # print("This item is for sale!")
# else:
    # print("This item is NOT for sale!")

online = False #assuming this changes with user

if online: # ":" means true.  it will always assume true
    print("The user is online!")
else:
    print("The user is offline.")