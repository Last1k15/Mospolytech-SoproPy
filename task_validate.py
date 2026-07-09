from load import *
from section import *

# Проверка суммы длин сечений
def validateSections(self):
    lengthSum = 0
    # Суммируем длины сечений
    for sect in self.sectionList:
        length = (sect.distance2 - sect.distance1)
        lengthSum += length

    # Должно совпасть с длиной стержня
    if (lengthSum != self.length):
        raise ValueError("Sections are not valid")


# Проверка допустимых для задачи типов внешних нагрузок
def validateLoads(self):

    for load in self.loadList:

        # Для растяжения-сжатия только продольные нагрузки
        badTensionCompressionTypes = (self.taskType == self.TaskType.TensionCompression) and (not isinstance(load, AxialForce))

        # Для кручения только крутящие моменты
        badTorsionTypes = (self.taskType == self.TaskType.Torsion) and (not isinstance(load, Torque))

        # Для изгиба все кроме крутящих моментов
        badBendTypes = (self.taskType == self.TaskType.Bend) and (isinstance(load, Torque))

        if (badTensionCompressionTypes or badTorsionTypes or badBendTypes):
            raise ValueError("Load types are not valid")

        # Проверим границы распределенной нагрузки
        if (isinstance(load, DistrLoad)):
            badRelativeDistances = (load.distance >= load.distance2)
            outOfBounds1 = (load.distance <= 0) or (load.distance > self.length)
            outOfBounds2 = (load.distance2 <= 0) or (load.distance2 > self.length)
            if (badRelativeDistances or outOfBounds1 or outOfBounds2):
                raise ValueError("Load distances are not valid")

        # Проверим расстояния остальных нагрузок
        else:
            outOfBounds = (load.distance <= 0) or (load.distance > self.length)
            if (outOfBounds):
                raise ValueError("Load distances are not valid")
