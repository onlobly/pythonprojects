#these are strings

first_name = "Caleb"
food = "pasta"
email = "Caleb@fake.com"

print(f"Hello, {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

#integers
age = 18
quantity = 100
num_of_people = 24

print(f"You are {age} years old!")
print(f"You are buying {quantity} item/s.")
print(f"There's {num_of_people} people here.")

#floats
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}.")
print(f"Your gpa is: {gpa}.")
print(f"You ran {distance}!")

#booleans

is_student = False
for_sale = True
is_online = True

if is_student:
    print("You are a student.")
else:
    print("You are not a student!")

if for_sale:
    print("That item is for sale!")
else:
    print("That item is not for sale!")

if is_online:
    print("User is online.")
else:
    print("User is offline.")