My_Fav_numbers={11,22,37,43,85}
My_Fav_numbers.add(21)
My_Fav_numbers.add(24)
print(My_Fav_numbers)
My_Fav_numbers.remove(24)
My_Fav_numbers.remove(max(My_Fav_numbers))
friend_fav_numbers = {3889, 568, 91}
our_fav_numbers = My_Fav_numbers | friend_fav_numbers
print("My favorite numbers:", My_Fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)