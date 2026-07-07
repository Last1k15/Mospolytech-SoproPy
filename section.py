# Сечение
class Section:
    def __init__(self, area : int, distance1 : int, distance2 : int, inertiaMoment : int = 0):
        self.area = area
        self.distance1 = distance1
        self.distance2 = distance2
        self.inertiaMoment = inertiaMoment
    def __repr__(self):
        return f"(area: {self.area}; dist1: {self.distance1}; dist2: {self.distance2}; inertiaMoment: {self.inertiaMoment})"
