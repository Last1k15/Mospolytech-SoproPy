from enum import Enum 
from material import *
from section import *
from load import *
from task_validate import *
from task_io import *

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

    validateSections = validateSections
    validateLoads = validateLoads
    printData = printData
    interactWithUser = interactWithUser

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

            prevDot = self.dotList[-1] - 0.00005
            for dot in reversed(self.dotList):
                normPower = 0
                for load in reversed(self.loadList):
                    if (load.distance > dot):
                        normPower += load.value
                    else: break
                normPowerList.append(normPower)
                for sect in reversed(self.sectionList):
                    if (sect.distance1 <= dot and sect.distance2 >= dot): 
                        normTensionList.append(normPower / sect.area)
                        displacementList.append((normPower * (prevDot - dot)) / (self.material.youngModulus * sect.area))
                        break
                prevDot = dot

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
