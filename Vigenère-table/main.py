import cryptography
import tables
import string_format


# 1 user input

user_input = input("Enter a text max 255 characters: ")
user_input = string_format.format_from_keyboard(user_input)

# 4, get keyword from user

user_key_word = input("Enter a keyword length has to be maximum 5 characters and no numbers: ")
user_key_word = string_format.format_from_keyboard(user_key_word)
vtable_source = input("Add the vtable locaton route: ")
vtable_list = tables.read_tabels(vtable_source)

coding = cryptography.Crypto(user_key_word, vtable_list)

result_text = coding.coded_text(user_input)

print(result_text)
print(repr(result_text))
decoded_text = input("Give me the text what you'd like to decode: ")
print(coding.decode_text(decoded_text))