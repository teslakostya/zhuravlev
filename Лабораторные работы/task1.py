import doctest


class BMWM5F90:
    def __init__(self, acceleration_time: float, engine_volume: float, cylinders_count: int):
        """
        Создание и подготовка к работе объекта "Автомобиль BMW M5 F90"

        :param acceleration_time: Время разгона до 100 км/ч (секунды)
        :param engine_volume: Объём двигателя (литры)
        :param cylinders_count: Количество цилиндров

        Примеры:
        >>> car = BMWM5F90(3.4, 4.4, 8)  # инициализация экземпляра класса
        """
        if not isinstance(acceleration_time, (int, float)):
            raise TypeError("Время разгона должно быть типа int или float")
        if acceleration_time <= 0:
            raise ValueError("Время разгона должно быть положительным числом")
        self.acceleration_time = acceleration_time

        if not isinstance(engine_volume, (int, float)):
            raise TypeError("Объём двигателя должен быть типа int или float")
        if engine_volume <= 0:
            raise ValueError("Объём двигателя должен быть положительным числом")
        self.engine_volume = engine_volume

        if not isinstance(cylinders_count, int):
            raise TypeError("Количество цилиндров должно быть типа int")
        if cylinders_count <= 0:
            raise ValueError("Количество цилиндров должно быть положительным числом")
        self.cylinders_count = cylinders_count

        # Дополнительные атрибуты
        self.current_speed = 0  # текущая скорость в км/ч
        self.mileage = 0  # пробег в км

    def is_stopped(self) -> bool:
        """
        Функция которая проверяет стоит ли автомобиль

        :return: True если автомобиль стоит (скорость = 0), иначе False

        Примеры:
        >>> car = BMWM5F90(3.4, 4.4, 8)
        >>> car.is_stopped()
        True
        """
        return self.current_speed == 0

    def accelerate(self, target_speed: float, time: float) -> None:
        """
        Разгон автомобиля до определённой скорости за заданное время.

        :param target_speed: Целевая скорость (км/ч)
        :param time: Время разгона (секунды)
        :raise ValueError: Если целевая скорость меньше текущей или время отрицательное

        Примеры:
        >>> car = BMWM5F90(3.4, 4.4, 8)
        >>> car.accelerate(100, 3.4)
        """
        if not isinstance(target_speed, (int, float)):
            raise TypeError("Целевая скорость должна быть типа int или float")
        if target_speed < self.current_speed:
            raise ValueError("Целевая скорость не может быть меньше текущей")
        if not isinstance(time, (int, float)):
            raise TypeError("Время должно быть типа int или float")
        if time < 0:
            raise ValueError("Время не может быть отрицательным")

        # Обновляем скорость и пробег (упрощённая модель)
        acceleration_distance = (self.current_speed + target_speed) / 2 * (time / 3600)
        self.mileage += acceleration_distance
        self.current_speed = target_speed

    def brake(self, braking_time: float) -> float:
        """
        Торможение автомобиля.

        :param braking_time: Время торможения (секунды)
        :raise ValueError: Если время торможения отрицательное
        :return: Скорость после торможения

        Примеры:
        >>> car = BMWM5F90(3.4, 4.4, 8)
        >>> car.current_speed = 100
        >>> car.brake(5)
        0.0
        """
        if not isinstance(braking_time, (int, float)):
            raise TypeError("Время торможения должно быть типа int или float")
        if braking_time < 0:
            raise ValueError("Время торможения не может быть отрицательным")

        # Упрощённый расчёт - линейное уменьшение скорости
        deceleration = self.current_speed / (braking_time if braking_time > 0 else 1)
        new_speed = max(0, self.current_speed - deceleration * braking_time)

        # Расчёт расстояния торможения
        braking_distance = (self.current_speed + new_speed) / 2 * (braking_time / 3600)
        self.mileage += braking_distance
        self.current_speed = new_speed

        return new_speed

    def get_specifications(self) -> dict:
        """
        Получение технических характеристик автомобиля

        :return: Словарь с характеристиками

        Примеры:
        >>> car = BMWM5F90(3.4, 4.4, 8)
        >>> specs = car.get_specifications()
        >>> specs['acceleration_time']
        3.4
        """
        return {
            'acceleration_time': self.acceleration_time,
            'engine_volume': self.engine_volume,
            'cylinders_count': self.cylinders_count,
            'current_speed': self.current_speed,
            'mileage': self.mileage
        }


import doctest

class IPhone17Pro:
    def __init__(self, display_size: float, refresh_rate: int, camera_mp: int):
        """
        Создание объекта "iPhone 17 Pro"

        :param display_size: Диагональ дисплея (дюймы)
        :param refresh_rate: Частота обновления (Гц)
        :param camera_mp: Камера (Мп)

        Примеры:
        >>> phone = IPhone17Pro(6.3, 120, 48)
        """
        if not isinstance(display_size, (int, float)) or display_size <= 0:
            raise ValueError("Диагональ должна быть положительным числом")
        if not isinstance(refresh_rate, int) or refresh_rate <= 0:
            raise ValueError("Частота должна быть положительным целым числом")
        if not isinstance(camera_mp, int) or camera_mp <= 0:
            raise ValueError("Камера должна быть положительным целым числом")

        self.display_size = display_size
        self.refresh_rate = refresh_rate
        self.camera_mp = camera_mp
        self.on = False
        self.storage_used = 0

    def is_on(self) -> bool:
        """
        Проверка включен ли телефон

        Примеры:
        >>> phone = IPhone17Pro(6.3, 120, 48)
        >>> phone.is_on()
        False
        """
        return self.on

    def power_toggle(self) -> None:
        """
        Включить/выключить телефон

        Примеры:
        >>> phone = IPhone17Pro(6.3, 120, 48)
        >>> phone.power_toggle()
        >>> phone.is_on()
        True
        >>> phone.power_toggle()
        >>> phone.is_on()
        False
        """
        self.on = not self.on

    def take_photo(self, size_mb: float = 5.0) -> None:
        """
        Сделать фото

        :param size_mb: Размер фото в МБ

        Примеры:
        >>> phone = IPhone17Pro(6.3, 120, 48)
        >>> phone.on = True
        >>> phone.take_photo(8.5)
        >>> phone.storage_used
        8.5
        """
        if not self.on:
            raise ValueError("Телефон выключен")
        if not isinstance(size_mb, (int, float)) or size_mb <= 0:
            raise ValueError("Размер фото должен быть положительным числом")

        self.storage_used += size_mb


import doctest


class Su57Fighter:
    def __init__(self, crew: int, max_speed: float, wingspan: float):
        """
        Создание объекта "Истребитель Су-57"

        :param crew: Экипаж (человек)
        :param max_speed: Максимальная скорость (км/ч)
        :param wingspan: Размах крыла (м)

        Примеры:
        >>> fighter = Su57Fighter(1, 2600, 14)
        """
        if not isinstance(crew, int) or crew <= 0:
            raise ValueError("Экипаж должен быть положительным целым числом")
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        if not isinstance(wingspan, (int, float)) or wingspan <= 0:
            raise ValueError("Размах крыла должен быть положительным числом")

        self.crew = crew
        self.max_speed = max_speed
        self.wingspan = wingspan
        self.speed = 0
        self.flying = False

    def is_flying(self) -> bool:
        """
        Проверка состояния полета

        Примеры:
        >>> fighter = Su57Fighter(1, 2600, 14)
        >>> fighter.is_flying()
        False
        """
        return self.flying

    def takeoff_land(self) -> None:
        """
        Взлет или посадка

        Примеры:
        >>> fighter = Su57Fighter(1, 2600, 14)
        >>> fighter.takeoff_land()
        >>> fighter.is_flying()
        True
        >>> fighter.takeoff_land()
        >>> fighter.is_flying()
        False
        """
        if self.flying:
            # Посадка
            if self.speed > 350:
                raise ValueError("Слишком высокая скорость для посадки")
            self.flying = False
            self.speed = 0
        else:
            # Взлет
            self.flying = True
            self.speed = 300

    def set_speed(self, new_speed: float) -> None:
        """
        Установить скорость

        :param new_speed: Новая скорость (км/ч)

        Примеры:
        >>> fighter = Su57Fighter(1, 2600, 14)
        >>> fighter.flying = True
        >>> fighter.set_speed(1500)
        >>> fighter.speed
        1500
        """
        if not self.flying:
            raise ValueError("Самолет на земле")
        if not isinstance(new_speed, (int, float)):
            raise TypeError("Скорость должна быть числом")
        if new_speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        if new_speed > self.max_speed:
            raise ValueError(f"Скорость превышает максимум ({self.max_speed})")

        self.speed = new_speed


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации