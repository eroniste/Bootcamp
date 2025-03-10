choice = input("Enter 1 for multiples or 2 to remove consecutive duplicates: ")

if choice == "1":
    number = int(input("Enter a number: "))
    length = int(input("Enter a length: "))

    multiples = [number * i for i in range(1, length + 1)]

    print(multiples)

elif choice == "2":
    user_input = input("Enter a string: ")

    new_string = ""

    for i in range(len(user_input)):
        if i == 0 or user_input[i] != user_input[i - 1]:
            new_string += user_input[i]

    print(new_string)

else:
    print("Invalid input! Please enter either 1 or 2.")
