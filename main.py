from enum import Enum 

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

# Сечение
class Section:
    def __init__(self, area : int, distance1 : int, distance2 : int, inertiaMoment : int = 0):
        self.area = area
        self.distance1 = distance1
        self.distance2 = distance2
        self.inertiaMoment = inertiaMoment
    def __repr__(self):
        return f"(area: {self.area};dist1: {self.distance1};dist2: {self.distance2};inertiaMoment: {self.inertiaMoment})"

class MaterialProperties:
    def __init__(self, youngModulus : int, poissonsRatio : int, fluidityMargin : int = 0): # мод Юнга, коэф Пуассона, предел текучести
        self.youngModulus = youngModulus
        self.poissonsRatio = poissonsRatio
        self.fluidityMargin = fluidityMargin
    def __repr__(self):
        return f"youngModulus: {self.youngModulus}\npoissonsRatio: {self.poissonsRatio}\nfluidityMargin: {self.fluidityMargin}"


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
        self.sectionList = sorted(sectionList, key=lambda x: x.distance1)
        self.loadList = sorted(loadList, key=lambda x: x.distance)
        self.dotList = []


    def validateSections(self):
        lengthSum = 0
        for sect in self.sectionList:
            lengthSum += (sect.distance2 - sect.distance1)
        if (lengthSum != self.length):
            raise ValueError("Sections are not valid")

    def validateLoads(self):
        for load in self.loadList:

            badTensionCompressionTypes = self.taskType == self.TaskType.TensionCompression and not isinstance(load, ConcPower)
            badTorsionTypes = self.taskType == self.TaskType.Torsion and not isinstance(load, TorsionMoment)
            badBendTypes = self.taskType == self.TaskType.Bend and isinstance(load, TorsionMoment)

            if (badTensionCompressionTypes or badTorsionTypes or badBendTypes):
                raise ValueError("Loads types are not valid")

            if (0 <= load.distance > self.length):
                raise ValueError("Loads distances are not valid")

    def defineDots(self):
        for load in self.loadList:
            if (isinstance(load, DistrLoad)):
                self.dotList.append(load.distance1)
                self.dotList.append(load.distance2)

            else: self.dotList.append(load.distance)

        for sect in self.sectionList:
            self.dotList.append(sect.distance1)
            self.dotList.append(sect.distance2)
        self.dotList = sorted(set(self.dotList))


    def solve(self):
        self.validateSections()
        self.validateLoads()
        if (self.taskType == self.TaskType.TensionCompression):
            self.defineDots()
            normPowerList = []
            normTensionList = []
            displacementList = []
            strainList = []
            for dot in reversed(self.dotList):
                normPower = 0
                for load in reversed(self.loadList):
                    if (load.distance >= dot):
                        normPower += load.value
                    else: break
                normPowerList.append(normPower)
                for sect in reversed(self.sectionList):
                    if (sect.distance1 <= dot and sect.distance2 >= dot): 
                        normTensionList.append(normPower / sect.area)
                        displacementList.append((normPower * (sect.distance2 - sect.distance1)) / (self.material.youngModulus * sect.area))
                        break
            normPowerList = normPowerList[::-1]
            normTensionList = normTensionList[::-1]
            displacementList = displacementList[::-1]
            safetyFactor = self.material.fluidityMargin / max([abs(n) for n in normTensionList])

            strain = 0
            for i in range(len(self.dotList)):
                strainList.append(strain)
                strain += displacementList[i]

            self.printData()
            print("normPowers:\n", normPowerList)
            print("normTensions:\n",normTensionList)
            print("displacements:\n",displacementList)
            print("strains:\n",strainList)
            print("safetyFactor:\n",safetyFactor)
                
    def printData(self):
        print(f"{self.taskType.name = }")
        print(self.material)

        print("\n\nSECTIONS")
        for sect in self.sectionList:
            print(sect)

        print("\n\nLOADS")
        for load in self.loadList:
            print(load,type(load))
        print("\n\nDOTS")
        print(self.dotList)
        print("\n\n")

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
mySectList.append(Section(2*AREA, 0, 1))
mySectList.append(Section(AREA, 2, 4))
mySectList.append(Section(2*AREA, 1, 2))

LOAD = 10*10**3
myLoadList = []
myLoadList.append(ConcPower(LOAD, 4))
myLoadList.append(ConcPower(LOAD, 1))

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


