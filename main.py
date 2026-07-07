from task import *

myTaskType = Task.TaskType.TensionCompression
L = 2.3
A = 12.5*10**(-4)
F = 90*10**3
myMaterial = MaterialProperties(
        youngModulus = 2*10**11,
        poissonsRatio = 0.31,
        fluidityMargin = 235*10**6
)

mySectList = []
mySectList.append(Section(2*A, 0, 0.8))
mySectList.append(Section(A, 0.8, 2.3))

myLoadList = []
myLoadList.append(ConcPower(4*F, 0.4))
myLoadList.append(ConcPower(-F, 1.6))
myLoadList.append(ConcPower(-F, 2.3))

myTask = Task(
        taskType = myTaskType,
        length = L,
        sectionList = mySectList,
        loadList = myLoadList,
        material = myMaterial
)

myTask.solve()
