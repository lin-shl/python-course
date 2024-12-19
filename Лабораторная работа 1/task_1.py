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

    def speed_movement(self, distance: float, time: int) -> float:
        """
        Метод вычисляет скорость движения автомобиля исходя из заданных параметров расстояния и времени
        :param time: Время в минутах, за которое автомобиль прошёл расстояние.
        :param distance: Расстояние, которое прошёл автомобиль.
        :return: Скорость, с которой автомобиль прошёл расстояние.

        Пример:
        >>> auto = Auto("BMW", "3", "Красный")
        >>> auto.speed_movement(100, 50)
        120.0
        """

        if not isinstance(time, int):
            raise TypeError("Время должно быть типа int")
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть типа int или float")
        if time < 0 or distance < 0:
            raise ValueError("Значения не должны быть отрицательными")
        if time == 0:
            return 0.0

        # Перевод минут в часы
        time_h = time / 60

        # Вычисление скорости
        speed = distance / time_h

        return speed

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
        if speed < 0:
            raise ValueError("Скорость не должна быть отрицательной")
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
        if current_speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        if allowed_speed < 5:
            raise ValueError("Допустимая скорость не может быть меньше 5 км/ч")

    def verdict(self) -> bool:
        """
        Метод проверяет, есть ли нарушение, и выносит вердикт

        :return: Истина, если нарушение есть, Ложь – если нет.

        Пример:
        >>> fine = Fine(150, 90)
        >>> fine.verdict()
        True
        """
        return self.current_speed > self.allowed_speed

    def value(self) -> int:
        """
        Функция, которая проверяет пороговое значение нарушения и возвращает
        соответствующий штраф

        :return: Сумму штрафа в соответствии с пороговым значением.

        Пример:
        >>> fine = Fine(150, 90)
        >>> fine.value()
        3000
        """
        speed_difference = self.current_speed - self.allowed_speed

        if speed_difference <= 20:
            return 500
        elif 20 < speed_difference <= 40:
            return 1500
        elif 40 < speed_difference <= 60:
            return 3000
        elif speed_difference > 60:
            return 5000

    def cancel(self) -> None:
        """
        Метод, отменяющий штраф

        Пример:
        >>> fine = Fine(80, 90)
        >>> fine.cancel()
        """
        ...

class Cam:
    def __init__(self, memory_capacity: float):
        """
        Подготовка записывающего устройства

        :param memory_capacity: Содержит значение объема хранилища устройства.

        Пример:
        >>> camera = Cam(128)
        """
        if not isinstance(memory_capacity, (int, float)):
            raise TypeError("Объём памяти должен быть типа int или float")
        if memory_capacity <= 0:
            raise ValueError("Память не может быть отрицательной или равной нулю")

        self.memory_capacity = memory_capacity
        self.occupied_memory = 0  # Изначально занятая память равна 0

    def record(self) -> None:
        """
        Метод, выполняющий запись в файл

        Пример:
        >>> camera = Cam(128)
        >>> camera.record()
        """
        # Здесь должна быть логика записи, которая обновляет self.occupied_memory
        ...

    def clear(self) -> None:
        """
        Метод, выполняющий очистку памяти

        Пример:
        >>> camera = Cam(128)
        >>> camera.clear()
        """
        self.occupied_memory = 0
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
