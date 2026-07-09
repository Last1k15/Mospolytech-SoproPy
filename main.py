from task import *

def torsionTask():
        myTaskType = Task.TaskType.Bend
        L = 5

        myMaterial = MaterialProperties(
                youngsModulus = 210e9,
                poissonsRatio = 0.35
        )

        D = 1E-2
        mySectList = []
        mySectList.append(IBeamSection(distance1 = 0, distance2 = 5, width = 14*D, height = 20*D, innerThickness = 6*D, thickness1 = 6*D, thickness2 = 6*D))

        F = 1e3
        myLoadList = []
        myLoadList.append(ShearForce(distance = 4, value = F, direction=Direction.Down))
        myLoadList.append(BendMoment(distance = 1, value = F, direction=Direction.CounterClockwise))

        myTask = Task(
                taskType = myTaskType,
                length = L,
                sectionList = mySectList,
                loadList = myLoadList,
                material = myMaterial
        )

        myTask.solve()

# myTask = Task()
# myTask.prompt()

# torsionTask()
