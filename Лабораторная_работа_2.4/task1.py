class Pet:
    """
    Базовый класс для домашних животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Инициализирует объект домашнего животного.

        :param name: Имя животного
        :param age: Возраст животного
        """
        self._name = name
        self._age = age

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта с правильным склонением слова "лет".
        """
        age_word = "лет" if 5 <= self._age % 100 <= 20 else (
            "год" if self._age % 10 == 1 else ("года" if 2 <= self._age % 10 <= 4 else "лет"))
        return f"{self.__class__.__name__} по кличке {self._name}, возраст: {self._age} {age_word}"

    def __repr__(self) -> str:
        """
        Возвращает техническое строковое представление объекта.
        """
        return f"{self.__class__.__name__}('{self._name}', {self._age})"

    def make_sound(self) -> str:
        """
        Метод, который должны переопределить подклассы для звука животного.
        """
        return "Какой-то звук"

    def play(self) -> str:
        """
        Базовый метод для игры животного.
        """
        return f"{self._name} играет."


class Dog(Pet):
    """
    Класс для представления собаки, наследуется от Pet.
    """

    def make_sound(self) -> str:
        """
        Перегружаем метод из базового класса.
        Собака лает, поэтому звук отличается от базового.
        """
        return f"{self._name}: Гав-гав!"

    def play(self) -> str:
        """
        Перегружаем метод play. Предположим, что собаки играют только бегая за мячом.
        """
        return f"{self._name} бегает за мячом!"


class Cat(Pet):
    """
    Класс для представления кошки, наследуется от Pet.
    """

    def make_sound(self) -> str:
        """
        Перегружаем метод из базового класса.
        Кошка мяукает, поэтому звук отличается.
        """
        return f"{self._name}: Мяу!"

    def scratch(self) -> str:
        """
        Новый метод, уникальный для кошек.
        """
        return f"{self._name} царапает мебель!"


# Пример использования
if __name__ == "__main__":
    dog = Dog("Шарик", 7)
    cat = Cat("Мурка", 2)

    print(dog)  # Собака по кличке Шарик, возраст: 7 лет
    print(cat)  # Кошка по кличке Мурка, возраст: 2 года

    print(dog.make_sound())  # Гав-гав!
    print(cat.make_sound())  # Мяу!
    print(cat.scratch())  # Мурка царапает мебель!
    print(cat.play())  # Мурка играет.
    print(dog.play())  # Шарик бегает за мячом!
