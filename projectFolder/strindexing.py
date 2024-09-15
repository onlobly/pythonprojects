# indexing = accessing elements of a sequence using [] (indexing operator)
#       [start : end : step] (x, y, z)

credit_number = "1234-5678-9012-3456"

print(credit_number[4]) # prints the 4th digit, starting with 0
print(credit_number[0:4]) # prints the first four, end is exclusive and start is inclusive
print(credit_number[5:9]) # starts from # of digits in, not string start unless (x:y:z) x is omitted
print(credit_number[5:]) # py assumes you need everything from x to end of string
print(credit_number[-5]) # can underflow around to grab end of string

print(credit_number[::2]) # will assume the start and end is the whole string, and then only include every "z" characters for step

last_digits = credit_number[-4:] # will grab from the fourth to last all the way to the last because y is omitted
print(f"XXXX-XXXX-XXXX-{last_digits}")
credit_number = credit_number[::-1] # step of 1 will show every number, -1 will reverse it!
print(credit_number)
