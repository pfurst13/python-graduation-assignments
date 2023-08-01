from unidecode import unidecode

def format_string(user_input):
    user_input = unidecode(user_input)
    return user_input.upper()

# 1, ask user to get 255 charachter input

user_string = input("Enter a text max 255 characters no numbers: ")

while len(user_string) > 255 or user_string.isalpha() == False:
    user_string = input("Too long or contains numbers. It can be 255 characters. Enter a new one: ")

# 2, 3 format string to english print out
user_string = format_string(user_string)
print(user_string)

# 4, get keyword from user

user_key_word = input("Enter a keyword length has to be 5 characters and no numbers: ")
keyword_len = len(user_key_word)
print(keyword_len)

while keyword_len != 5 or user_key_word.isalpha() == False:
    user_key_word = input("Keyword has to be 5 characters and no numbers: ")
    keyword_len = len(user_key_word)

user_key_word = format_string(user_key_word)
