from unidecode import unidecode

def format_string(user_input):
    user_input = unidecode(user_input)
    return user_input.upper()

# 1, ask user to get 255 charachter input

user_string = input("Enter a text max 255 characters: ")

while len(user_string) > 255:
    user_string = input("Too long. It can be 255 characters. Enter a new one: ")

# 2, format string to english
user_string = format_string(user_string)
print(user_string)


