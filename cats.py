from cat import Cat # импорт класса Cat


cats = [{"name":"Барон", "sex":"male", "age":2}, {"name":"Сэм", "sex":"male", "age":2}]

for i, cat_ in enumerate(cats):
    cat_object = Cat()
    cat_object.init_from_dict(cat_)
    print(f"{i+1} {cat_object.type} - Name:{cat_object.name}, sex:{cat_object.sex}, age:{cat_object.age}")