class Cat:
    type = "cat"
    
    def __init__(self, name = "Noname", sex = "Nosex", age = 0):
        self.name = name
        self.sex = sex
        self.age = age


    def set_age(self, age):
        if age > 0 and isinstance(age, int):
            self.age = age


    def init_from_dict(self, cat_dict):
        self.name = cat_dict.get("name")
        self.sex = cat_dict.get("sex")
        self.age = self.set_age(cat_dict.get("age"))
