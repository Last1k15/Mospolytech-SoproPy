from math import pi

# Сечение
class Section:
    def __init__(self, distance1 : int, distance2 : int, area : int):
        self.area = area
        self.distance1 = distance1
        self.distance2 = distance2
    def __repr__(self):
        return f"(area: {self.area}; dist1: {self.distance1}; dist2: {self.distance2}; inertiaMoment: {self.inertiaMoment})"

class RoundSection(Section):
    def __init__(self, distance1 : int, distance2 : int, diameter : int):
        area = pi * outerDiameter ** 2 / 4
        super().__init__(area, distance1, distance2)
        self.diameter = diameter
        self.inertiaMoment = pi * outerDiameter ** 4 / 32
        self.resistanceMoment = pi * outerDiameter ** 3 / 16
    def __repr__(self):
        return f"(area: {self.area}; dist1: {self.distance1}; dist2: {self.distance2}; inertiaMoment: {self.inertiaMoment}); resistanceMoment: {self.resistanceMoment}"

class ThickRoundSection(RoundSection):
    def __init__(self, distance1 : int, distance2 : int, outerDiameter : int, innerDiameter : int = 0):
        area = pi * (outerDiameter ** 2 - innerDiameter ** 2) / 4
        super().__init__(distance1, distance2, outerDiameter)
        self.outerDiameter = outerDiameter
        self.innerDiameter = innerDiameter
        self.inertiaMoment = pi * (outerDiameter ** 4 - innerDiameter ** 4) / 32
        self.resistanceMoment = pi * (outerDiameter ** 3 - innerDiameter ** 3) / 16

class ThinRoundSection(RoundSection):
    def __init__(self, distance1 : int, distance2 : int, outerDiameter : int, innerDiameter : int = 0):
        area = pi * (outerDiameter ** 2 - innerDiameter ** 2) / 4
        super().__init__(distance1, distance2, outerDiameter)
        self.outerDiameter = outerDiameter
        self.innerDiameter = innerDiameter
        self.inertiaMoment = pi / 64 * (outerDiameter ** 4 - innerDiameter ** 4)

class LBeamSection(Section):
    def __init__(self, distance1 : int, distance2 : int, width : int, height : int, innerThickness : int, thickness1 : int, thickness2 : int):
        area = width * (thickness1 + thickness2) + innerThickness * (height - thickness1 - thickness2)
        super().__init__(area, distance1, distance2)
        self.width = width
        self.height = height
        self.innerThickness = innerThickness
        self.thickness1 = thickness1
        self.thickness2 = thickness2
        self.inertiaMoment = innerThickness * (height - 2 * innerThickness) ** 2 / 6 + 2 * (width * innerThickness ** 3 / 12 + width * innerThickness * ((height - innerThickness) / 2) ** 2)

    def __repr__(self):
        return f"(area: {self.area}; dist1: {self.distance1}; dist2: {self.distance2}; inertiaMoment: {self.inertiaMoment}); resistanceMoment: {self.resistanceMoment}"

class HollowRectangleSection(Section):
    def __init__(self, distance1 : int, distance2 : int, sideLength : int, thickness : int):
        area = 4 * thickness * (sideLength - thickness)
        super().__init__(distance1, distance2, area)
        self.sideLength = sideLength
        self.thickness = thickness
        self.inertiaMoment = (sideLength ** 4 - (sideLength - 2 * thickness) ** 4) / 12

class TSection(Section):
    def __init__(self, distance1 : int, distance2 : int, width : int, height : int, thickness1 : int, thickness2 : int):
        area = width * (thickness2) + thickness2 * (height - thickness1)
        super().__init__(distance1, distance2, area)
        self.width = width
        self.height = height
        self.thickness1 = thickness1
        self.thickness2 = thickness2

class SquareSection(Section):
    def __init__(self, distance1 : int, distance2 : int, sideLength : int):
        area = sideLength ** 2
        super().__init__(area, distance1, distance2)
        self.sideLength = sideLength
        self.inertiaMoment = 0.141 * sideLength ** 4
        self.resistanceMoment = 0.208 * sideLength ** 3

    def __repr__(self):
        return f"(area: {self.area}; dist1: {self.distance1}; dist2: {self.distance2}; inertiaMoment: {self.inertiaMoment}); resistanceMoment: {self.resistanceMoment}"
