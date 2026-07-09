from enum import Enum 

from material import *
from section import *
from load import *
from task_validate import *
from task_io import *

from task_tc import *
from task_torsion import *
from task_bend import *

# Глобальный класс задачи
class Task:
    class TaskType(Enum):
        TensionCompression = 0 # Растяжение-сжатие
        Torsion = 1 # Кручение
        Bend = 2 # Изгиб

    def __init__(self, taskType : TaskType = None, material : MaterialProperties = MaterialProperties(), length : int = 0, sectionList : list[Section] = [], loadList : list[LoadInterface] = []):
        self.taskType = taskType # тип решаемой задачи
        self.material = material # материал стержня
        self.length = length # длина стержня
        self.sectionList = sorted(sectionList, key=lambda x: x.distance1) # массив поперечных сечений
        self.loadList = sorted(loadList, key=lambda x: x.distance) # массив внешних нагрузок
        self.dotList = [] # Ключевые точки для рассмотрения
        self.BIAS = 0.00005 # отклонение от рассматриваемой точки, чтобы (не)включить нагрузки на определенном шаге

    validateSections = validateSections
    validateLoads = validateLoads
    printData = printData
    prompt = prompt
    plotDiagram = plotDiagram

    TensionCompressionAlgorithm = TensionCompressionAlgorithm
    TorsionAlgorithm = TorsionAlgorithm
    BendAlgorithm = BendAlgorithm

    # Определим ключевые точки для рассморения
    def defineDots(self):

        # Каждую ключевую точку разделим на две, отличающиеся на BIAS, чтобы рассмотреть случай до и после учета нагрузки в этой точке

        distrDots = []

        # Внешняя нагрузка - ключевая точка
        for load in self.loadList:

             # Рассмотрим обе границы распределенной нагрузки
            if (isinstance(load, DistrLoad)):
                if (load.distance != 0):
                    self.dotList.append(load.distance - self.BIAS)
                self.dotList.append(load.distance2 - self.BIAS)
                self.dotList.append(load.distance + self.BIAS)
                if (load.distance2 != self.length):
                    self.dotList.append(load.distance2 + self.BIAS)

                # Сохраним положение распределенной нагрузки
                distrDots.append((load.distance, load.distance2))
                self.dotList.append((load.distance + load.distance2)/2)

            else: 
                if (load.distance != 0):
                    self.dotList.append(load.distance - self.BIAS)
                if (load.distance != self.length):
                    self.dotList.append(load.distance + self.BIAS)

                # Промежутчные точки для распределенной нагрузки
                if (distrDots):
                    for d1, d2 in distrDots:
                        if (load.distance == d1 or load.distance == d2):
                            continue
                        self.dotList.append((d1 + load.distance)/2)
                        self.dotList.append((d2 + load.distance)/2)


        # Стык разных сечений - ключевая точка
        for sect in self.sectionList:
            if (sect.distance1 != 0):
                self.dotList.append(sect.distance1 - self.BIAS)
            self.dotList.append(sect.distance1 + self.BIAS)
            self.dotList.append(sect.distance2 - self.BIAS)
            if (sect.distance2 != self.length):
                self.dotList.append(sect.distance2 + self.BIAS)

        # Удалим совпадающие точки и отсортируем
        self.dotList = sorted(set(self.dotList))


    def solve(self):

        # Проверим качество входных данных
        print("Validating data...", end="")
        self.validateSections()
        self.validateLoads() 
        print("OK!")

        self.defineDots() # определим ключевые точки для рассмотрения

        solution = dict() # Решение получим в формате название-величина

        # В зависимости от типа задачи применим соотвествующий алгоритм решения
        match self.taskType:
            case self.TaskType.TensionCompression:
                solution = self.TensionCompressionAlgorithm()

            case self.TaskType.Torsion:
                solution = self.TorsionAlgorithm()

            case self.TaskType.Bend:
                solution = self.BendAlgorithm()

        # Выведем результат, построим эпюры
        self.printData(solution)
        self.plotDiagram(solution)
        print("Task complete!")
