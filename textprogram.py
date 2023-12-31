def format_string(str):
    interrogatives = ("Who", "What", "When", "Where", "Why", "How")
    str_capitalized = str.capitalize()
    if str_capitalized.startswith(interrogatives):
        return str_capitalized + '?'
    else:
        return str_capitalized + '.'
    

user_input_list = []

while True:
    user_input = input("Say something! ('\end' to end)\n")
    
    if user_input != "\end":
        user_input_list.append(format_string(user_input))
    else:
        break

# Printing all recorded user inputs
print(" ".join(user_input_list))