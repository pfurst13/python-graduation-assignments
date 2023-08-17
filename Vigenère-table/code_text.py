import cryptography
import tables
import string_format

def coding_text():
    user_input = input("Enter your text or upload the file: ")
    user_input = string_format.format_from_keyboard(user_input)