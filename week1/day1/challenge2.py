user_input = input("Enter a string: ")


new_string = ""


for i in range(len(user_input)):
    
    if i == 0 or user_input[i] != user_input[i - 1]:
        new_string += user_input[i]


print(new_string)
