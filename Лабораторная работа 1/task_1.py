import doctest


class Auto:
    """
    Класс для представления автомобиля, зарегистрированного
    при нарушении скоростного режима
    """
    def __init__(self, name: str, speed: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param name: Название марки авто
        :param speed: Скорость, при которой было зарегистрировано нарушение

        >>> auto = Auto("Honda Civic", 110)
        >>> current_speed = auto.speed
        >>> print(current_speed)
        110
        """
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной.")

        self.name = name
        self.speed = speed

    def verdict(self, speed: float, normal_speed: float) -> bool:
        """
        Метод проверяет, есть ли нарушение, и выносит вердикт

        :param normal_speed: Скорость, заданная для данного участка дороги
        :param speed: Скорость, с которой ехал водитель
        :return: Истина, если нарушение есть, Ложь – если нет

        Пример:
        >>> auto = Auto("Honda Civic", 110)
        >>> current_speed = auto.speed
        >>> auto.verdict(current_speed, 90)
        True
        >>> auto.verdict(current_speed, 120)
        False
        >>> auto.verdict(current_speed, 4)
        Traceback (most recent call last):
            ...
        ValueError: Установленная скорость не может быть меньше 5 км/ч.
        """
        if normal_speed < 5:
            raise ValueError("Установленная скорость не может быть меньше 5 км/ч.")
        return speed > normal_speed


class Driver:
    def __init__(self, name: str, surname: str):
        """
        Данные о водителе

        :param name: Имя
        :param surname: Фамилия

        Пример:
        >>> driver = Driver("Вася", "Пупкин")
        >>> wrong_driver = Driver("Иван Иванов", 110)
        Traceback (most recent call last):
            ...
        TypeError: Имя и фамилия должны быть типа str.
        """
        if not isinstance(name, str) or not isinstance(surname, str):
            raise TypeError("Имя и фамилия должны быть типа str.")


class Fine:
    def __init__(self, current_speed: float, allowed_speed: float):
        """
        Создание и подготовка штрафного листа

        :param current_speed: Зафиксированная скорость
        :param allowed_speed: Допустимая скорость

        Примеры:
        >>> auto = Auto("Honda Civic", 110)
        >>> speed = auto.speed
        >>> fine = Fine(speed, 90)
        """
        self.current_speed = current_speed
        self.allowed_speed = allowed_speed

    def fine(self) -> int:
        """
        Функция, которая проверяет пороговое значение нарушения и возвращает
        соответствующий штраф

        :return: Штраф в соответствии с пороговым значением

        Пример:
        >>> auto = Auto("Honda Civic", 110)
        >>> speed = auto.speed
        >>> fine = Fine(speed, 90)
        >>> fine.fine()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()