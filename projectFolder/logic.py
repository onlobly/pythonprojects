# logical operators = used on conditional statements

#       and = checks two or more  conditions if True
#       or = checks if at least one condition is True
#       not = True if condition is False, and vice versa

# temp = 25

# if temp > 0 and temp < 30: # if temp is between the two numbers, can be written better
    # print("The temperature is good!")
# else:
    # print("The temperature is bad!")

temp = 40
sunny = True

if temp <= 0 or temp >= 30:
    print("The temperature is bad.")
else:
    print("The temperature is good.")

if not sunny: # could also write: if sunny == True/False
    print("It is sunny!")
else:
    print("It is cloudy.")