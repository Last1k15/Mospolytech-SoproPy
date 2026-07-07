# Интерфейс нагрузки
class Load:
    def __init__(self, value : int, distance : int):
        self.value = value
        self.distance = distance
    def __repr__(self):
        return f"(val: {self.value};dist: {self.distance})"


# Сосредоточенная сила
class ConcPower(Load):
    def __init__(self, value : int, distance : int):
        super().__init__(value, distance)


# Распределенная нагрузка
class DistrLoad(Load):
    def __init__ (self, value : int, distance1 : int, distance2 : int):
        super().__init__(value, distance1)
        self.distance2 = distance2

    def __repr__(self):
        return f"(val: {self.value};dist1: {self.distance1};dist2: {self.distance2})"


# Изгибный момент
class BendMoment(Load):
    def __init__(self, value : int, distance : int):
        super().__init__(value, distance)


# Момент кручения
class TorsionMoment(Load):
    def __init__(self, value : int, distance : int):
        super().__init__(value, distance)
