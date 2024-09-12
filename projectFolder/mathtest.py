import math

print(math.pi)
#print(math.e) # physics

#   py math

friends = 10

# friends = friends + 1
# friends += 1 #augmented operator

# friends = friends - 2
# friends -= 2

# friends = friends * 3
# friends *= 3

# friends = friends / 2 # will implicit typecast to a float
# friends /= 2

# friends = friends ** 2 # to the power of
# friends **= 2
# % is the modulus operator
remainder = friends % 3 # remainders are like dividing up into groups and someone being left out

print(type(friends))
print(f"friends: {friends}")
print(f"remainder: {remainder}")

x = 3.14
y = 4
z = 5

# result = round(x)
# result = abs(y) #absolute value
# result = pow(z, 3) # power of
# result = max(x, y, z)
# result = min(x, y, z)
# result = math.sqrt(z) # square root
# result = math.ceil(x)
result = math.floor(x)

print(f"result: {result}")

