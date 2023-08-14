from unidecode import unidecode
import string
import cryptography
import tables
import string_format


# 1 user input

user_input = input("Enter a text max 255 characters: ")
user_input = string_format.format_from_keyboard(user_input)
print(user_input)

# 4, get keyword from user

user_key_word = input("Enter a keyword length has to be maximum 5 characters and no numbers: ")
user_key_word = string_format.format_from_keyboard(user_key_word)
print(user_key_word)

vtable_list = tables.read_tabels("/Users/furst_peter/python-graduation-assignments/python-graduation-assignments/Vigenère-table/table.txt")

coding = cryptography.Crypto(user_key_word, vtable_list)

result_text = coding.coded_text(user_input)

print(result_text)
print(coding.decode_text(result_text))