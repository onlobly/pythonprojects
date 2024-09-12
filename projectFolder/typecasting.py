# typecasting is the process of converting a value of one data type to another
#   (string, integer, float, boolean)
#   Explicit vs Implicit

name = "Caleb" #string
age = 18 #integer
gpa = 1.9 #float
student = True #boolean

# print(type(student)) # var checker

#   explicit

age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

student = str(student)
print(student)
print(type(student))

age = bool(age)
print(age) # any number expect 0 is true in boolean form

name = bool(name)
print(name) # if name is empty or = "" bool will be false
print(type(name))

#   implicit

x = 2
y = 2.0

x = x / y

print(x) # x will be implicitly turned into a float