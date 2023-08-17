import cryptography
import tables
import string_format
import decode_text



# 1 user input

user_input = input("Enter your text: ")
user_input = string_format.format_from_keyboard(user_input)

# 4, get keyword from user

user_key_word = input("Enter your keyword: ")
user_key_word = string_format.format_from_keyboard(user_key_word)

is_default = True

if is_default == False: 
    vtable_source = input("Add the vtable locaton route: ")
    vtable_list = tables.read_tabels(vtable_source)
elif is_default:
    vtable_list = tables.default_table()

coding = cryptography.Crypto(user_key_word, vtable_list)

result_text = coding.coded_text(user_input)

print(result_text)

print(decode_text.translate_code())

