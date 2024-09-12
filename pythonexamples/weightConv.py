# Python weight converter

weight = float(input("Enter a weight: "))
unit = input("kg or lbs? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Converted weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Converted weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} was not valid.")