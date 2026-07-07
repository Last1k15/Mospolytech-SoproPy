from task import *

myTaskType = Task.TaskType.Torsion
L = 2.1
myMaterial = MaterialProperties(
        shearModulus = 8*10**10
)

D = 1*10**(-3)

mySectList = []
mySectList.append(RoundSection(outerDiameter = 65*D, distance1 = 0, distance2 = 0.7))
mySectList.append(SquareSection(sideLength = 60*D, distance1 = 0.7, distance2 = 1.4))
mySectList.append(RoundSection(outerDiameter = 70*D, innerDiameter = 35*D, distance1 = 1.4, distance2 = 2.1))

F = 1*10**3
myLoadList = []
myLoadList.append(TorsionMoment(value = 0.5*F, distance = 0.4))
myLoadList.append(TorsionMoment(value = -0.6*F, distance = 0.8))
myLoadList.append(TorsionMoment(value = 1.1*F, distance = 1.55))

myTask = Task(
        taskType = myTaskType,
        length = L,
        sectionList = mySectList,
        loadList = myLoadList,
        material = myMaterial
)

myTask.solve()
