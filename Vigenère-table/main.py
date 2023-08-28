import decode_text
import code_text


choose_coding = input("If you'd like to code the text use C, to decode use D: ")
final_text = ""
if choose_coding == "C":
    final_text = code_text.coding_text()
if choose_coding == "D":
    final_text = decode_text.translate_code()

print(final_text)