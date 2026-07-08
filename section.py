from math import pi

# Произвольное cечение
class Section:
    def __init__(self, distance1 : int, distance2 : int, area : int):
        self.area = area
        self.distance1 = distance1
        self.distance2 = distance2
    def __repr__(self):
        return f"distance1: {self.distance1}; "\
                f"distance2: {self.distance2}; " \
                f"area: {self.area}; "

# Круглое сечение
class RoundSection(Section):
    def __init__(self, distance1 : int, distance2 : int, diameter : int):
        area = pi * diameter ** 2 / 4
        super().__init__(distance1, distance2, area)
        self.diameter = diameter
        self.axialInertiaMoment = pi * diameter ** 4 / 32
        self.polarInertiaMoment = pi * diameter ** 4 / 64
        self.sectionModulus = pi * diameter ** 3 / 16
    def __repr__(self):
        return f"distance1: {self.distance1}; "\
                  f"distance2: {self.distance2}; "\
                  f"area: {self.area}; "\
                  f"axialInertiaMoment: {self.axialInertiaMoment}; "\
                  f"polarInertiaMoment: {self.polarInertiaMoment}; "\
                  f"sectionModulus: {self.sectionModulus}; "


# Толстостенное круглое сечение
class ThickRoundSection(RoundSection):
    def __init__(self, distance1 : int, distance2 : int, outerDiameter : int, innerDiameter : int):
        area = pi * (outerDiameter ** 2 - innerDiameter ** 2) / 4
        super().__init__(distance1, distance2, outerDiameter)
        self.outerDiameter = outerDiameter
        self.innerDiameter = innerDiameter
        self.polarInertiaMoment = pi * (outerDiameter ** 4 - innerDiameter ** 4) / 32
        self.axialInertiaMoment = pi * (outerDiameter ** 4 - innerDiameter ** 4) / 64
        self.sectionModulus = pi * (outerDiameter ** 3 - innerDiameter ** 3) / 16
    def __repr__(self):
        return f"distance1: {self.distance1}; "\
                f"distance2: {self.distance2}; "\
                f"outerDiameter: {self.outerDiameter}; "\
                f"innerDiameter: {self.innerDiameter}; "\
                f"area: {self.area}; "\
                f"axialInertiaMoment: {self.axialInertiaMoment}; "\
                f"polarInertiaMoment: {self.polarInertiaMoment}; "\
                f"sectionModulus: {self.sectionModulus}; "\

# Тонкостенное круглое сечение
class ThinRoundSection(RoundSection):
    def __init__(self, distance1 : int, distance2 : int, outerDiameter : int, innerDiameter : int):
        area = pi * (outerDiameter ** 2 - innerDiameter ** 2) / 4
        super().__init__(distance1, distance2, outerDiameter)
        self.outerDiameter = outerDiameter
        self.innerDiameter = innerDiameter
        self.axialInertiaMoment = pi / 64 * (outerDiameter ** 4 - innerDiameter ** 4)

    def __repr__(self):
        return f"distance1: {self.distance1}; " \
                f"distance2: {self.distance2}; " \
                f"outerDiameter: {self.outerDiameter}; " \
                f"innerDiameter: {self.innerDiameter}; " \
                f"area: {self.area}; " \

# Двутавр
class IBeamSection(Section):
    def __init__(self, distance1 : int, distance2 : int, width : int, height : int, innerThickness : int, thickness1 : int, thickness2 : int):
        area = width * (thickness1 + thickness2) + innerThickness * (height - thickness1 - thickness2)
        super().__init__(distance1, distance2, area)
        self.width = width
        self.height = height
        self.innerThickness = innerThickness
        self.thickness1 = thickness1
        self.thickness2 = thickness2
        self.axialInertiaMoment = innerThickness * (height - 2 * innerThickness) ** 2 / 6 + 2 * (width * innerThickness ** 3 / 12 + width * innerThickness * ((height - innerThickness) / 2) ** 2)

    def __repr__(self):
        return f"dist1: {self.distance1}; "\
                f"dist2: {self.distance2}; "\
                f"width: {self.width}; "\
                f"height: {self.height}; "\
                f"innerThickness: {self.innerThickness}; "\
                f"thickness1: {self.thickness1}; "\
                f"thickness2: {self.thickness2}; "\
                f"area: {self.area}; "\
                f"axialInertiaMoment: {self.axialInertiaMoment}; "\

# Полое прямоугольное сечение
class HollowRectangleSection(Section):
    def __init__(self, distance1 : int, distance2 : int, sideLength : int, thickness : int):
        area = 4 * thickness * (sideLength - thickness)
        super().__init__(distance1, distance2, area)
        self.sideLength = sideLength
        self.thickness = thickness
        self.axialInertiaMoment = (sideLength ** 4 - (sideLength - 2 * thickness) ** 4) / 12
    def __repr__(self):
        return f"distance1: {self.distance1}; "\
                f"distance2: {self.distance2}; "\
                f"sideLength: {self.sideLength}; "\
                f"thickness: {self.thickness}; "\
                f"area: {self.area}; "\
                f"axialInertiaMoment: {self.axialInertiaMoment}; "\

# Тавр
class TSection(Section):
    def __init__(self, distance1 : int, distance2 : int, width : int, height : int, thickness1 : int, thickness2 : int):
        area = width * (thickness2) + thickness2 * (height - thickness1)
        super().__init__(distance1, distance2, area)
        self.width = width
        self.height = height
        self.thickness1 = thickness1
        self.thickness2 = thickness2

    def __repr__(self):
        return f"distance1: {self.distance1}; "\
                f"distance2: {self.distance2}; "\
                f"width: {self.width}; "\
                f"height: {self.height}; "\
                f"thickness1: {self.thickness1}; "\
                f"thickness2: {self.thickness2}; "\
                f"area: {self.area}; "\


# Квадратное сечение
class SquareSection(Section):
    def __init__(self, distance1 : int, distance2 : int, sideLength : int):
        area = sideLength ** 2
        super().__init__(distance1, distance2, area)
        self.sideLength = sideLength
        self.axialInertiaMoment = 0.141 * sideLength ** 4
        self.polarInertiaMoment = sideLength ** 4 / 12
        self.sectionModulus = 0.208 * sideLength ** 3

    def __repr__(self):
        return f"distance1: {self.distance1}; "\
                f"distance2: {self.distance2}; "\
                f"sideLength: {self.sideLength}; "\
                f"area: {self.area}; "\
                f"axialInertiaMoment: {self.axialInertiaMoment}; "\
                f"polarInertiaMoment: {self.polarInertiaMoment}; "\
                f"sectionModulus: {self.sectionModulus}; "
