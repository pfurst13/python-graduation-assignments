import cryptography

def translate_code(keyword, coding_table, decode_text):
    
    decode = cryptography.Crypto(keyword, coding_table)

    decoded_text = decode.decode_text(decode_text)

    return decoded_text