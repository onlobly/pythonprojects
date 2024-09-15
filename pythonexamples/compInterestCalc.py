# Python compound interest calc.  (Calc is short for calculator btw, its just slang).

principle = 0
rate = 0
time = 0

while True: # while loop will always be active until we break out of it!
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero!")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero!")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero!")
    else:
        break

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time) # this is the formula for interest
print(f"Balance after {time} year/s is ${total:.2f}!") # formatted to two decimals
