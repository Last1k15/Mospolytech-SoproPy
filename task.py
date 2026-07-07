from enum import Enum 

from material import *
from section import *
from load import *
from task_validate import *
from task_io import *

from task_tc_algo import *
from task_torsion_algo import *
from task_bend_algo import *

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

    TensionCompressionAlgorithm = TensionCompressionAlgorithm
    TorsionAlgorithm = TorsionAlgorithm
    BendAlgorithm = BendAlgorithm

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
        print("Task complete!")
