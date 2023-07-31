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

is_drawn = True

for i in range(90):
    num_counter = 0
    for weeks in all_lotto_numbers:
        if weeks.count(i + 1) > 0 :
            print('hét: ', weeks, 'a szám: ', i + 1)
            break
        else:
            num_counter += 1
    if num_counter == 51 * 5:
        print('van')
        is_drawn = False
        break
    
if is_drawn:
    print('nincs')

# 6, finding unpair numbers

odd_number_counter = 0

for weeks in all_lotto_numbers:
    for number in weeks:
        if number % 2 != 0:
            odd_number_counter += 1

print('odd number: ', odd_number_counter)

# 7, append 52nd week and write out
all_lotto_numbers.append(fiftytwo_numbers)

with open("lotto52.txt", "w") as f:
    for weeks in all_lotto_numbers:
        for number in weeks:
            f.write(f"{number} ")
        
        f.write('\n')

# often number
often_number = []

for lotto_number in range(90):
    counter = 0
    for week in all_lotto_numbers:
        if week.count(lotto_number + 1) > 0:
            counter += week.count(lotto_number + 1)
    
    often_number.append(counter)

print(often_number)
    
