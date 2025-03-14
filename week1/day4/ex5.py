from Family import Family


class TheIncredibles(Family):

    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] >= 18:
                    print(f"{member['name']} uses their power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old and cannot use their power!")

    def incredible_presentation(self):
        print("\n💥 Here is our powerful family! 💥")
        super().family_presentation()
        for member in self.members:
            print(f"Incredible Name: {member['incredible_name']}, Power: {member['power']}")


incredible_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredible_family = TheIncredibles("Incredibles", incredible_members)

incredible_family.incredible_presentation()

incredible_family.use_power("Michael")
incredible_family.use_power("Sarah")

incredible_family.born(name="Jack", age=0, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")


incredible_family.incredible_presentation()