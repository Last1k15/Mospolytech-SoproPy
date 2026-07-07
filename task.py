from enum import Enum 

from material import *
from section import *
from load import *
from task_validate import *
from task_io import *

from task_tc import *
from task_torsion import *
from task_bend import *

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
        self.BIAS = 0.00005

    validateSections = validateSections
    validateLoads = validateLoads
    printData = printData
    interactWithUser = interactWithUser
    plotDiagram = plotDiagram

    TensionCompressionAlgorithm = TensionCompressionAlgorithm
    TorsionAlgorithm = TorsionAlgorithm
    BendAlgorithm = BendAlgorithm

    def defineDots(self):
        for load in self.loadList:
            if (isinstance(load, DistrLoad)):
                if (load.distance1 != 0):
                    self.dotList.append(load.distance1 - self.BIAS)
                self.dotList.append(load.distance2 - self.BIAS)
                self.dotList.append(load.distance1 + self.BIAS)
                if (load.distance2 != self.length):
                    self.dotList.append(load.distance2 + self.BIAS)

            else: 
                if (load.distance != 0):
                    self.dotList.append(load.distance - self.BIAS)
                if (load.distance != self.length):
                    self.dotList.append(load.distance + self.BIAS)

        for sect in self.sectionList:
            if (sect.distance1 != 0):
                self.dotList.append(sect.distance1 - self.BIAS)
            self.dotList.append(sect.distance1 + self.BIAS)
            self.dotList.append(sect.distance2 - self.BIAS)
            if (sect.distance2 != self.length):
                self.dotList.append(sect.distance2 + self.BIAS)

        self.dotList = sorted(set(self.dotList))
        self.dotList[-1] -= self.BIAS


    def solve(self):

        print("Validating data...", end="")
        self.validateSections()
        self.validateLoads()
        print("OK!")

        self.defineDots()

        solution = dict()
        match self.taskType:
            case self.TaskType.TensionCompression:
                solution = self.TensionCompressionAlgorithm()

            case self.TaskType.Torsion:
                solution = self.TorsionAlgorithm()

            case self.TaskType.Bend:
                solution = self.BendAlgorithm()

        self.printData(solution)
        self.plotDiagram(solution)
        print("Task complete!")
