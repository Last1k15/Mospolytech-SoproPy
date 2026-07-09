from task import *

def bendTask():
        myTaskType = Task.TaskType.Bend
        L = 5

        myMaterial = MaterialProperties(
                youngsModulus = 210e9,
                poissonsRatio = 0.35
        )

        D = 1E-2
        mySectList = []
        mySectList.append(IBeamSection(distance1 = 0, distance2 = 5, width = 14*D, height = 20*D, innerThickness = 6*D, thickness1 = 6*D, thickness2 = 6*D))

        F = 20e3
        myLoadList = []
        myLoadList.append(ShearForce(distance = 2, value = F, direction=Direction.Up))
        myLoadList.append(BendMoment(distance = 2, value = F, direction=Direction.CounterClockwise))
        myLoadList.append(ShearForce(distance = 4, value = F, direction=Direction.Down))
        myLoadList.append(BendMoment(distance = 5, value = F, direction=Direction.Clockwise))
        myLoadList.append(DistrLoad(distance1 = 2, distance2 = 5, value = F, direction=Direction.Down))

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

bendTask()
