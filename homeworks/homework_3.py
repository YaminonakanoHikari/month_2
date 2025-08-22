class Person:
    # Инициализация атрибутов экземпляра
    def __init__(self, name, birth_date, age, occupation, higher_education):
        self.name = name                      # Имя
        self.birth_date = birth_date          # Дата рождения
        self.__age = age                        #Возраст
        self.__occupation = occupation          # Профессия
        self.__higher_education = higher_education  # Высшее образование (True/False)

    @property
    def occupation(self):
        return self.__occupation

    @occupation.setter
    def occupation(self, value):
        self.__occupation = value

    @property
    def higher_education(self):
        return self.__higher_education

    @higher_education.setter
    def higher_education(self, value):
        self.__higher_education = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value



    # Базовый метод introduce
    def introduce(self):
        edu_status = "с высшим образованием" if self.__higher_education else "без высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я родился {self.birth_date}, мне {self.__age} "
              f"работаю {self.__occupation}, {edu_status}.")

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
classmate1 = Classmate("Бектур", "05.12.2000",25,"Программист",True)
classmate1.introduce()
print(classmate1.age)
classmate2 = Classmate("Данияр", "14.08.2001",24, "Дизайнер", False)
classmate2.introduce()
print(classmate2.age)

friend1 = Friend("Алмаз", "11.03.1999", 26,"Инженер", True)
friend1.introduce()
print(friend1.age)
friend2 = Friend("Канат", "22.07.2000", 25,"Учитель", True)
friend2.introduce()
print(friend2.age)

