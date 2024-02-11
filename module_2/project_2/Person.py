class Person:
    def __init__(self, name, family_name, nickname, age):
        self.name = name
        self.family_name = family_name
        self.nickname = nickname
        self.age = age

    def get_name(self):
        return self.name

    def get_full_name(self):
        return self.name + " " + self.family_name

    def get_family_name(self):
        return self.family_name

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age
