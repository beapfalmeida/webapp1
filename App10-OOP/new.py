class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        name = self.name.upper()
        return name

    def age(self, current_year=2023):
        age = current_year - self.birth_year
        return age

user = User("John", 1999)
age = user.age()
name = user.get_name()
print(age)
print(name)



