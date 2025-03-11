family = {}
num_members = int(input("Enter the number of family members: "))

for _ in range(num_members):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    family[name] = age

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name} has to pay ${price}")
    total_cost += price

print(f"Total cost for the family: ${total_cost}")
