import doctest


class Auto:
    def __init__(self, mark, model, color: str):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param mark: Название марки автомобиля.
        :param model: Название модели автомобиля.
        :param color: Цвет автомобиля.

        Пример:
        >>> auto = Auto("BMW", "3", "Красный")
        >>> auto_mark = auto.mark
        >>> print(auto_mark)
        BMW
        """

        self.mark = mark
        self.model = model
        self.color = color

        if not isinstance(mark, str):
            raise TypeError("Марка должна быть типа str")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")

    def movement(self) -> bool:
        """
        Метод проверяет, движется ли машина
        :return: Возвращает истину при движении.

        Пример:
        >>> auto = Auto("BMW", "3", "Красный")
        >>> auto.movement()
        """
        ...


    def speed_movement(self, time: int, distance: float) -> float:
        """
        Метод вычисляет скорость движения автомобиля исходя из заданных параметров расстояния и времени
        :param time: Время, за которое автомобиль прошёл расстояние.
        :param distance: Расстояние, которое прошёл автомобиль.
        :return: Скорость, с которой автомобиль прошёл расстояние.

        Пример:
        >>> auto = Auto("BMW", "3", "Красный")
        >>> auto.speed_movement(1266, 55.8)
        """
        if not isinstance(time, int):
            raise TypeError("Время должно быть типа int")
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        ...

    def start(self, speed: float) -> None:
        """
        Метод, выполняющий запуск автомобиля с определённой скоростью
        :param speed: Скорость, с которой надо запустить автомобиль.

        Пример:
        >>> auto = Auto("BMW", "3", "Красный")
        >>> auto.start(120)
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть типа int или float")
        ...


class Fine:
    def __init__(self, current_speed: float, allowed_speed: float):
        """
        Создание и подготовка штрафного листа

        :param current_speed: Зафиксированная скорость.
        :param allowed_speed: Допустимая скорость.

        Примеры:
        >>> fine = Fine(150, 90)
        """

        self.current_speed = current_speed
        self.allowed_speed = allowed_speed

        if not isinstance(current_speed, (int, float)) or not isinstance(allowed_speed, (int, float)):
            raise TypeError("Скорость должна быть типа int или float.")

    def verdict(self) -> bool:
        """
        Метод проверяет, есть ли нарушение, и выносит вердикт

        :return: Истина, если нарушение есть, Ложь – если нет.

        Пример:
        >>> fine = Fine(150, 90)
        >>> fine.verdict()
        """
        ...

    def value(self) -> int:
        """
        Функция, которая проверяет пороговое значение нарушения и возвращает
        соответствующий штраф

        :return: Штраф в соответствии с пороговым значением.

        Пример:
        >>> fine = Fine(150, 90)
        >>> fine.value()
        """
        ...

    def cancel(self) -> None:
        """
        Метод, отменяющий штраф

        Пример:
        >>> fine = Fine(80, 90)
        >>> fine.cancel()
        """
        ...

class Cam:
    def __init__(self, memory: int):
        """
        Подготовка записывающего устройства

        :param memory: Содержит значение объема хранилища устройства.

        Пример:
        >>> camera = Cam(128)
        """
        if not isinstance(memory, (int, float)):
            raise TypeError("Объём памяти должен быть типа int или float")
        if memory <= 0:
            raise ValueError("Память не может быть отрицательно1 или равной нулю")

    def record(self) -> None:
        """
        Метод, выполняющий запись в файл

        Пример:
        >>> camera = Cam(128)
        >>> camera.record()
        """
        ...

    def clear(self) -> None:
        """
        Метод, выполняющий очистку памяти

        Пример:
        >>> camera = Cam(128)
        >>> camera.clear()
        """
        ...

    def play(self):
        """
        Метод, выполняющий вывод записи на устройство вывода
        :return: Запись с устройства.

        Пример:
        >>> camera = Cam(128)
        >>> camera.play()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
