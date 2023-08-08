from unidecode import unidecode

def format_string(user_input):
    user_input = unidecode(user_input)

    return user_input.upper()

# 1, ask user to get 255 charachter input

user_string = input("Enter a text max 255 characters no numbers: ")
user_string = format_string(user_string)
print(user_string)
user_string = user_string.replace(' ', '')

while len(user_string) > 255 or user_string.isalpha() == False:
    print(user_string.isalpha())
    user_string = input("Too long or contains numbers. It can be 255 characters. Enter a new one: ")
    user_string = format_string(user_string)
    user_string = user_string.replace(' ', '')

# 2, 3 format string to english print out
print(user_string)

# 4, get keyword from user

user_key_word = input("Enter a keyword length has to be maximum 5 characters and no numbers: ")
keyword_len = len(user_key_word)
print(keyword_len)

while keyword_len > 5 or user_key_word.isalpha() == False:
    user_key_word = input("Keyword has to be maximum 5 characters and no numbers: ")
    keyword_len = len(user_key_word)

user_key_word = format_string(user_key_word)

# 5, keyword concatenation
concanate_user_key = ""
for i in range(len(user_string)):
    concanate_user_key += user_key_word


concanate_user_key = concanate_user_key[:len(user_string)]
print(user_string, len(user_string), concanate_user_key, len(concanate_user_key))

# vtabla.dat open put in 2D list

vtable_list = []

with open("Vtabla.dat", "r") as vtable:
    for line in vtable:
        act_line = []
        line = line.rstrip('\n')
        vtable_list.append(line)

coded_text = []

for i in range(len(user_string)):
    column = 0
    row = 0

    for j, line in enumerate(vtable_list):
        if line[0] == user_string[i]:
            column = j

    row = vtable_list[0].index(concanate_user_key[i])
    coded_text.append(vtable_list[column][row])
final_result = "".join(coded_text)
print(final_result)