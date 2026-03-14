if __name__ == "__main__":
    class Aircraft:
        """
        Базовый класс, описывающий самолет.
        """

        def __init__(self, model: str, max_speed: int, fuel: float) -> None:
            """
            Конструктор базового класса.

            Args:
                model (str): Модель самолета.
                max_speed (int): Максимальная скорость (км/ч).
                fuel (float): Количество топлива (литры).
            """
            self.model: str = model
            self.max_speed: int = max_speed
            self._fuel: float = fuel
            self._altitude: float = 0  # текущая высота в метрах

        def __str__(self) -> str:
            return f"Aircraft model: {self.model}, max speed: {self.max_speed} km/h, altitude: {self._altitude} m"

        def __repr__(self) -> str:
            return f"Aircraft(model={self.model!r}, max_speed={self.max_speed!r}, fuel={self._fuel!r})"

        def fly(self, distance: float) -> float:
            """
            Метод полета самолета.

            Args:
                distance (float): Пройденная дистанция (км).

            Returns:
                float: Оставшееся количество топлива.
            """
            consumption: float = distance * 2.5  # расход топлива у самолета
            if consumption > self._fuel:
                print("Warning: Insufficient fuel for this distance!")
                return self._fuel
            self._fuel -= consumption
            self._altitude = 10000  # поднимаемся на крейсерскую высоту
            return self._fuel

        def takeoff(self) -> str:
            """
            Метод взлета.
            """
            if self._fuel < 100:
                return "Cannot takeoff: insufficient fuel!"
            self._altitude = 1000
            return f"{self.model} is taking off. Altitude: {self._altitude} m"

        def land(self) -> str:
            """
            Метод посадки.
            """
            self._altitude = 0
            return f"{self.model} is landing. Welcome to your destination!"

        def transport(self, cargo_weight: float) -> str:
            """
            Метод перевозки груза.

            Args:
                cargo_weight (float): Вес груза (тонны).

            Returns:
                str: Сообщение о перевозке.
            """
            return f"Aircraft transports {cargo_weight} tons of cargo."


    class PassengerAircraft(Aircraft):
        """
        Дочерний класс, описывающий пассажирский самолет.
        """

        def __init__(self, model: str, max_speed: int, fuel: float, seats: int) -> None:
            """
            Конструктор пассажирского самолета.

            Args:
                model (str): Модель самолета.
                max_speed (int): Максимальная скорость.
                fuel (float): Количество топлива.
                seats (int): Количество пассажирских мест.
            """
            super().__init__(model, max_speed, fuel)
            self.seats: int = seats
            self._passengers_on_board: int = 0

        def __str__(self) -> str:
            return f"Passenger aircraft {self.model}, seats: {self.seats}, max speed: {self.max_speed} km/h"

        def board_passengers(self, count: int) -> str:
            """
            Метод посадки пассажиров на борт.
            """
            if count > self.seats:
                return f"Cannot board {count} passengers. Maximum capacity is {self.seats}."
            self._passengers_on_board = count
            return f"{count} passengers boarded {self.model}."

        def transport(self, passengers: int) -> str:
            """
            Переопределённый метод перевозки пассажиров.

            Args:
                passengers (int): Количество пассажиров.

            Returns:
                str: Сообщение о перевозке пассажиров.
            """
            if passengers > self.seats:
                return f"Cannot transport {passengers} passengers. Maximum capacity exceeded!"
            self._passengers_on_board = passengers
            return f"Passenger aircraft {self.model} transports {passengers} passengers at {self.max_speed} km/h."

        def serve_meal(self) -> str:
            """
            Дополнительный метод для пассажирского самолета.
            """
            if self._passengers_on_board > 0:
                return f"Serving meals to {self._passengers_on_board} passengers on {self.model}."
            return "No passengers on board."


    if __name__ == "__main__":
        # Создаем и тестируем базовый самолет
        aircraft = Aircraft("Boeing 737", 850, 20000)
        print(aircraft)
        print(aircraft.takeoff())
        print(f"Fuel after flight: {aircraft.fly(1000)}")
        print(aircraft.land())
        print(aircraft.transport(5.5))
        print()

        # Создаем и тестируем пассажирский самолет
        passenger_aircraft = PassengerAircraft("Airbus A380", 900, 250000, 500)
        print(passenger_aircraft)
        print(passenger_aircraft.takeoff())
        print(passenger_aircraft.board_passengers(450))
        print(passenger_aircraft.transport(450))
        print(passenger_aircraft.serve_meal())
        print(passenger_aircraft.land())
    pass
