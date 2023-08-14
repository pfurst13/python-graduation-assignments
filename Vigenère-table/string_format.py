from unidecode import unidecode
import string

def format_from_keyboard(user_input):
    user_input = unidecode(user_input)

    return user_input

def format_from_file(txt_input):

    to_format_file = ""

    with open(txt_input, "r") as text:
        to_format_file = text.read()

    to_format_file = unidecode(to_format_file)
    to_format_file = to_format_file.translate(str.maketrans('','', string.punctuation))
    
    return to_format_file