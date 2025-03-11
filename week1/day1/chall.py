from datetime import datetime


birthdate = input("Enter your birthdate (DD/MM/YYYY): ")


birthdate = datetime.strptime(birthdate, "%d/%m/%Y")


current_year = datetime.now().year


age = current_year - birthdate.year


num_candles = age % 10


candles = "i" * num_candles


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
