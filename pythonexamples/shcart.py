#   shopping cart project (ty bro code)

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: ")) # prices may have decimals, use float
quantity = int(input("How many would you like?: ")) # could be a float but will use integers for now

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")