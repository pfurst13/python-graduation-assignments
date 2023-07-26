"""52nd week lotto numbers are as follows:  89 24 34 11 64"""

# 1, user enters the numbers

fiftytwo_numbers = []

for i in range(5):
    number_into_fiftytwo = int(input(f"Enter {i + 1} number: "))
    fiftytwo_numbers.append(number_into_fiftytwo)
    print(type(number_into_fiftytwo))

print(fiftytwo_numbers)

# 2, sorting numbers
fiftytwo_numbers = sorted(fiftytwo_numbers)
print(fiftytwo_numbers)