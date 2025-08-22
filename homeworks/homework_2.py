class Person:
    # Инициализация атрибутов экземпляра
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name                      # Имя
        self.birth_date = birth_date          # Дата рождения
        self.occupation = occupation          # Профессия
        self.higher_education = higher_education  # Высшее образование (True/False)

    # Базовый метод introduce
    def introduce(self):
        edu_status = "с высшим образованием" if self.higher_education else "без высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я родился {self.birth_date}, "
              f"работаю {self.occupation}, {edu_status}.")

# Класс-наследник "Одноклассник"
class Classmate(Person):
    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, я одноклассник Игоря. "
              f"Я родился {self.birth_date}, работаю {self.occupation}.")

# Класс-наследник "Друг"
class Friend(Person):
    def introduce(self):
        print(f"Привет! Меня зовут {self.name}, я друг Игоря. "
              f"Я родился {self.birth_date}, работаю {self.occupation}.")

# Создание объектов
classmate1 = Classmate("Бектур", "05.12.2000", "Программист", True)
classmate2 = Classmate("Данияр", "14.08.2001", "Дизайнер", False)

friend1 = Friend("Алмаз", "11.03.1999", "Инженер", True)
friend2 = Friend("Канат", "22.07.2000", "Учитель", True)

# Вызов метода introduce() для каждого объекта
for person in (classmate1, classmate2, friend1, friend2):
    person.introduce()

