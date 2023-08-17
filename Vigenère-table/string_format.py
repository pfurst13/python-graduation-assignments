from unidecode import unidecode
import string

def format_from_keyboard(user_input):

    return user_input

def format_from_file(txt_input):

    to_format_file = ""

    with open(txt_input, "r") as text:
        to_format_file = text.read()
    
    return to_format_file