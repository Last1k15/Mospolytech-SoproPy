from math import pi

# Сечение
class Section:
    def __init__(self, area : int, distance1 : int, distance2 : int):
        self.area = area
        self.distance1 = distance1
        self.distance2 = distance2
    def __repr__(self):
        return f"(area: {self.area}; dist1: {self.distance1}; dist2: {self.distance2}; inertiaMoment: {self.inertiaMoment})"

class RoundSection(Section):
    def __init__(self, distance1 : int, distance2 : int, outerDiameter : int, innerDiameter : int = 0):
        area = pi * (outerDiameter ** 2 - innerDiameter ** 2) / 4
        super().__init__(area, distance1, distance2)
        self.outerDiameter = outerDiameter
        self.innerDiameter = innerDiameter
        self.inertiaMoment = pi * (outerDiameter ** 4 - innerDiameter ** 4) / 32
        self.resistanceMoment = pi * (outerDiameter ** 3 - innerDiameter ** 3) / 16
    def __repr__(self):
        return f"(area: {self.area}; dist1: {self.distance1}; dist2: {self.distance2}; inertiaMoment: {self.inertiaMoment}); resistanceMoment: {self.resistanceMoment}"

class SquareSection(Section):
    def __init__(self, distance1 : int, distance2 : int, sideLength : int):
        area = sideLength ** 2
        super().__init__(area, distance1, distance2)
        self.sideLength = sideLength
        self.inertiaMoment = 0.141 * sideLength ** 4
        self.resistanceMoment = 0.208 * sideLength ** 3

    def __repr__(self):
        return f"(area: {self.area}; dist1: {self.distance1}; dist2: {self.distance2}; inertiaMoment: {self.inertiaMoment}); resistanceMoment: {self.resistanceMoment}"
