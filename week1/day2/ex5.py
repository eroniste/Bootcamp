import random

def guess_number(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success! You guessed the correct number.")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

guess_number(42)  
