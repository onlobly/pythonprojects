#   user input

name = input("Enter your name: ") # input is stored as the variable at the same time
age = int(input("Enter your age: ")) # input will always be a string datatype unless type-casted.
age = age + 1

print(f"Hello, {name}!")
print(f"You are going to be {age} years old.")