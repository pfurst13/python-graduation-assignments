import cryptography
import tables

def translate_code():
    
    decode_text = input("Give me the text what you'd like to decode: ")
    decode_keyword = input("Give me the keyword: ")
    coding_table = input("Upload your own table. If you would like to use defaoult table press enter: ")

    if coding_table == "":
        coding_table = tables.default_table()
        decode = cryptography.Crypto(decode_keyword, coding_table)
        decoded_text = decode.decode_text(decode_text)
    else:
        own_table = tables.read_tabels(coding_table)
        decode = cryptography.Crypto(decode_keyword, own_table)
        decoded_text = decode.decode_text(decode_text)

    return decoded_text