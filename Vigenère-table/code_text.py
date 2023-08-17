import cryptography
import tables
import string_format

def coding_text():
    user_input = input("Enter your text or press enter: ")

    if user_input == "":
        user_input = input("Type the file path: ")
        user_input = string_format.format_from_file(user_input)
    else: 
        user_input = string_format.format_from_keyboard(user_input)

    keyword = input("Give me the keyword: ")
    coding_table = input("Upload your own table. If you would like to use defaoult table press enter: ")

    if coding_table == "":
        coding_table = tables.default_table()
        crypting = cryptography.Crypto(keyword, coding_table)
        crypting_text = crypting.coded_text(user_input)
    else:
        own_table = tables.read_tabels(coding_table)
        crypting = cryptography.Crypto(keyword, own_table)
        crypting_text = crypting.coded_text(user_input)

    return crypting_text
