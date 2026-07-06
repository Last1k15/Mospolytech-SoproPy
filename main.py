from enum import Enum 

# Интерфейс нагрузки
class Load:
    def __init__(self, value : int, distance : int):
        self.value = value
        self.distance = distance


# Сосредоточенная сила
class ConcPower(Load):
    def __init__(self, value : int, distance : int):
        super().__init__(value, distance)


# Распределенная нагрузка
class DistrLoad(Load):
    def __init__ (self, value : int, distance1 : int, distance2 : int):
        super().__init__(value, distance1)
        self.distance2 = distance2


# Изгибный момент
class BendMoment(Load):
    def __init__(self, value : int, distance : int):
        super().__init__(value, distance)


# Момент кручения
class TorsionMoment(Load):
    def __init__(self, value : int, distance : int):
        super().__init__(value, distance)

# Сечение
class Section:
    def __init__(self, area : int, distance1 : int, distance2 : int, inertiaMoment : int = 0):
        self.area = area
        self.distance1 = distance1
        self.distance2 = distance2
        self.inertiaMoment = inertiaMoment
        self.length = length

class MaterialProperties:
    def __init__(self, youngModulus : int, poissonsRatio : int, fluidityMargin : int = 0): # мод Юнга, коэф Пуассона, предел текучести
        self.youngModulus = youngModulus
        self.poissonsRatio = poissonsRatio
        self.fluidityMargin = fluidityMargin


# Общий класс решения задачи
class Task:
    class TaskType(Enum):
        TensionCompression = 1
        Torsion = 2
        Bend = 3

    def __init__(self, taskType : TaskType = None, material : MaterialProperties = None, length : int = 0, sectionList : list[Section] = None, loadList : list[Load] = None):
        self.taskType = taskType
        self.material = material
        self.length = length
        self.sectionList = sectionList
        self.loadList = loadList

    def validateSections(self):
        lengthSum = 0
        for sect in self.sectionList:
            lengthSum += sect.length
        if (lengthSum != self.length):
            raise ValueError("Sections are not valid")

    def validateLoads(self):
        for load in self.loadList:

            badTensionCompressionTypes = self.taskType = self.TaskType.TensionCompression and not isinstance(load, ConcPower)
            badTorsionTypes = self.taskType = self.TaskType.Torsion and not isinstance(load, TorsionMoment)
            badBendTypes = self.taskType = self.TaskType.Bend and isinstance(load, TorsionMoment)

            if (badTensionCompressionTypes or badTorsionTypes or badBendTypes):
                raise ValueError("Loads types are not valid")

            if (0 <= load.distance > self.length):
                raise ValueError("Loads distances are not valid")

    def defineDots(self):
        dotList = []
        for load in self.loadList:
            if (isinstance(load, DistrLoad)):
                dotList.append(load.distance1)
                dotList.append(load.distance2)
            else dotList.append(load.distance)
        for load in self.sectionList:
            dotList.append(load.distance1)
            dotList.append(load.distance2)
        dotList = sort(set(dotList))
        return dotList


    def solve(self):
        self.validateSections()
        self.validateLoads()
        if (self.taskType == self.TaskType.TensionCompression):
            dotList = defineDots()
            for load in self.loadList
            normForceList = []
            for load in self.loadList:
                

    def interactWithUser(self):
        inp = "_"
        while (inp not in "123"):
            inp = input("Тип задачи?\nРастяжение-Сжатие = 1\nКручение = 2\nИзгиб = 3\n-> ")
        self.taskType = self.TaskType(int(inp)).name
        while (True):
            inp = input("Длина стержня?\n-> ")
            try:
                self.length = int(inp)
                break
            except ValueError:
                continue

# раст-сж 

myTaskType = Task.TaskType.TensionCompression
LENGTH = 4
AREA = 0.0025
mySectList = []
mySectList.append(Section(2*AREA, 1))
mySectList.append(Section(2*AREA, 1))
mySectList.append(Section(AREA, 2))

LOAD = 10*10**3
myLoadList = []
myLoadList.append(ConcPower(LOAD, 1))
myLoadList.append(ConcPower(LOAD, 4))

myMaterial = MaterialProperties(
        youngModulus = 70*10**9,
        poissonsRatio = 0.31,
        fluidityMargin = 50*10**6
)

myTask = Task(
        taskType = myTaskType,
        length = LENGTH,
        sectionList = mySectList,
        loadList = myLoadList,
        material = myMaterial
)

myTask.solve()
# myTask.interactWithUser()
# attrs = vars(myTask)
# print(', '.join("%s: %s" % item for item in attrs.items()))


