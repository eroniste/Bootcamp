from datetime import datetime

# Get user input
birthdate = input("Enter your birthdate (DD/MM/YYYY): ")

# Convert input to a datetime object
birthdate = datetime.strptime(birthdate, "%d/%m/%Y")

# Get current year
current_year = datetime.now().year

# Calculate age
age = current_year - birthdate.year

# Determine the number of candles (last digit of age)
num_candles = age % 10

# Generate the candles string
candles = "i" * num_candles

# Define the cake design
cake = f"""
       ___{candles}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""


is_leap_year = (birthdate.year % 4 == 0 and birthdate.year % 100 != 0) or (birthdate.year % 400 == 0)


if is_leap_year:
    print(cake * 2) 
else:
    print(cake)
