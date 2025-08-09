class Person:
    # Инициализация атрибутов экземпляра
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name                      # Имя
        self.birth_date = birth_date          # Дата рождения
        self.__occupation = occupation        # Профессия (приватный атрибут)
        self.__higher_education = higher_education  # Высшее образование (приватный атрибут True/False)

    # Геттер и сеттер для occupation
    @property
    def occupation(self):
        return self.__occupation

    @occupation.setter
    def occupation(self, value):
        self.__occupation = value

    # Геттер и сеттер для higher_education
    @property
    def higher_education(self):
        return self.__higher_education

    @higher_education.setter
    def higher_education(self, value):
        self.__higher_education = value

    # Базовый метод introduce
    def introduce(self):
        edu_status = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет! Меня зовут {self.name}. Моя профессия {self.occupation}. {edu_status}")


# Класс-наследник "Одноклассник"
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        edu_status = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет! Меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Я учился с Арианой в группе {self.group}. {edu_status}")


# Класс-наследник "Друг"
class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_status = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет! Меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Мое хобби {self.hobby}. {edu_status}")


# Создание объектов
cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")

# Вызов метода introduce() для каждого объекта
cl1.introduce()
fr1.introduce()
