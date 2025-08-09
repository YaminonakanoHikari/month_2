class Person:
    # Инициализация атрибутов экземпляра
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name                      # Имя
        self.birth_date = birth_date          # Дата рождения
        self.occupation = occupation          # Профессия
        self.higher_education = higher_education  # Высшее образование (True/False)

# Создание экземпляров класса
person1 = Person("Alexey", "1990-05-14", "Engineer", True)
person2 = Person("Maria", "1995-09-21", "Designer", False)
person3 = Person("Ivan", "1988-12-03", "Teacher", True)

# Вывод атрибутов каждого экземпляра
for person in (person1, person2, person3):
    print(f"Name: {person.name}")
    print(f"Birth date: {person.birth_date}")
    print(f"Occupation: {person.occupation}")
    print(f"Higher education: {'Yes' if person.higher_education else 'No'}")
    print("-" * 30)

