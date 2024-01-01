def format_string(str) -> str:
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

print()
# Printing all recorded user inputs in chronological order
print("\n".join(user_input_list))