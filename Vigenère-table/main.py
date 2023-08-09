from unidecode import unidecode
import cryptography
import tables

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

vtable_list = tables.read_tabels("/Users/furst_peter/python-graduation-assignments/python-graduation-assignments/Vigenère-table/Vtabla.dat")

coding = cryptography.Crypto(user_key_word, vtable_list)

result_text = coding.coded_text(user_string)

print(result_text)
print(coding.decode_text(result_text))