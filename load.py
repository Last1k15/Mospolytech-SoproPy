from enum import Enum
from abc import ABC, abstractmethod

class Direction(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3
    Clockwise = 4
    CounterClockwise = 5


# Интерфейс нагрузки
class LoadInterface(ABC):

    def __init__(self, value : int, distance : int, direction : Direction):
        if (not self.validateDirection(direction)):
            raise ValueError("Cant initialize load: invalid direction")
        self.value = abs(value)
        self.distance = distance
        self.direction = direction

    @abstractmethod
    def validateDirection(self, direction : Direction) -> bool:
        pass

    def __repr__(self):
        return f"(val: {self.value}; distance: {self.distance}; type: {self.__class__.__name__}; direction: {self.direction})"



# Продольная сила
class AxialForce(LoadInterface):
    def __init__(self, value : int, distance : int, direction : Direction):
        super().__init__(value, distance, direction)

    def validateDirection(self, direction : Direction) -> bool:
        return (direction == Direction.Left or direction == Direction.Right)


# Поперечная сила
class ShearForce(LoadInterface):
    def __init__(self, value : int, distance : int, direction : Direction):
        super().__init__(value, distance, direction)

    def validateDirection(self, direction : Direction):
        return (direction == Direction.Up or direction == Direction.Down)


# Распределенная нагрузка
class DistrLoad(LoadInterface):
    def __init__ (self, value : int, distance1 : int, distance2 : int, direction : Direction):
        super().__init__(value, distance1, direction)
        self.distance2 = distance2

    def validateDirection(self, direction : Direction):
        return (direction == Direction.Up or direction == Direction.Down)

    def __repr__(self):
        return f"(val: {self.value}; dist1: {self.distance}; dist2: {self.distance2}; type: {self.__class__.__name__})"


# Изгибающий момент
class BendMoment(LoadInterface):
    def __init__(self, value : int, distance : int, direction : Direction):
        super().__init__(value, distance, direction)

    def validateDirection(self, direction : Direction):
        return (direction == Direction.Clockwise or direction == Direction.CounterClockwise)


# Крутящий момент
class Torque(LoadInterface):
    def __init__(self, value : int, distance : int, direction : int):
        super().__init__(value, distance, direction)

    def validateDirection(self, direction : Direction):
        return (direction == Direction.Clockwise or direction == Direction.CounterClockwise)
