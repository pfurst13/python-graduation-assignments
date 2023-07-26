"""52nd week lotto numbers are as follows:  89 24 34 11 64"""

# 1, user enters the numbers

fiftytwo_numbers = []

for i in range(5):
    number_into_fiftytwo = int(input(f"Enter {i + 1} number: "))
    fiftytwo_numbers.append(number_into_fiftytwo)

# 2, sorting numbers
fiftytwo_numbers = sorted(fiftytwo_numbers)
print(fiftytwo_numbers)

# 3, Choosing number
user_number = int(input("Choose a number 1-52: "))
print(user_number)

# 4, Open the .dat file and printing user choice

all_lotto_numbers = []
with open("lottosz.dat", "r") as lotto:
    for line in lotto:
        act_numbers = []
        act_line = line.split()
        for item in act_line:
            number_from_line = int(item)
            act_numbers.append(number_from_line)
        all_lotto_numbers.append(act_numbers)
print(all_lotto_numbers[user_number - 1])

# 5, find the undrawn number (true/false)
drown_number = 1 
