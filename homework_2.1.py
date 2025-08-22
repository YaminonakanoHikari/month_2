# Базовый класс Person
class Person:
    # Метод __init__ — инициализатор (конструктор), который вызывается при создании объекта
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name  # Имя человека
        self.birth_date = birth_date  # Дата рождения
        self.occupation = occupation  # Профессия
        self.higher_education = higher_education  # True/False — есть ли высшее образование

    # Метод introduce — выводит общую информацию о человеке
    def introduce(self):
        # Определяем текст про образование
        edu_status = "с высшим образованием" if self.higher_education else "без высшего образования"
        # Выводим информацию в консоль
        print(f"Привет! Меня зовут {self.name}. Я родился {self.birth_date}, "
              f"работаю {self.occupation}, {edu_status}.")


# Дочерний класс Classmate (одноклассник)
class Classmate(Person):
    # Переопределяем __init__, чтобы добавить новый уникальный атрибут group_name
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        # super() — вызывает конструктор родительского класса Person
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name  # Уникальный атрибут: название группы/класса

    # Переопределяем метод introduce, чтобы изменить вывод
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник Игоря, "
              f"учились вместе в {self.group_name}, "
              f"я родился {self.birth_date}, работаю {self.occupation}.")


# Дочерний класс Friend (друг)
class Friend(Person):
    # Добавляем новый атрибут hobby (хобби)
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        # Вызываем родительский конструктор для общих атрибутов
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby  # Уникальный атрибут: хобби

    # Переопределяем метод introduce
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг Игоря, "
              f"моё хобби — {self.hobby}, "
              f"я родился {self.birth_date}, работаю {self.occupation}.")


# Создание объектов классов
classmate_1 = Classmate("Бектур", "05.12.2000", "Программист", True, "11 Д")
classmate_2 = Classmate("Артур", "30.05.1999", "Менеджер", False, "11 Д")

friend_1 = Friend("Курманбек", "12.08.2005", "Разработчик", False, "Компьютерные игры")
friend_2 = Friend("Алмаз", "11.03.1999", "Инженер", True, "Футбол")

# Список с объектами разных типов
people = [classmate_1, classmate_2, friend_1, friend_2]

# Полиморфизм в действии
# Мы вызываем один и тот же метод introduce() для объектов разных классов
# При этом каждый класс выполняет свою версию метода
for person in people:
    person.introduce()
