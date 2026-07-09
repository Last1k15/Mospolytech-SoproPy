from task import *

def tcTask():
        myTaskType = Task.TaskType.TensionCompression
        L = 2.3
        myMaterial = MaterialProperties(
                youngsModulus = 2e11,
                yieldStrength = 235e6
        )

        mySectList = []
        mySectList.append(Section(distance1 = 0, distance2 = 0.8, area = 25e-4))
        mySectList.append(Section(distance1 = 0.8, distance2 = 2.3, area = 12.5e-4))

        F = 20e3
        myLoadList = []
        myLoadList.append(AxialForce(distance = 0.4, value = 360e3, direction=Direction.Right))
        myLoadList.append(AxialForce(distance = 1.6, value = 90e3, direction=Direction.Left))
        myLoadList.append(AxialForce(distance = 2.3, value = 90e3, direction=Direction.Left))

        myTask = Task(
                taskType = myTaskType,
                length = L,
                sectionList = mySectList,
                loadList = myLoadList,
                material = myMaterial
        )

        myTask.solve()

def torsionTask():
        myTaskType = Task.TaskType.Torsion
        L = 2.1

        myMaterial = MaterialProperties(
                shearModulus = 8e10
        )

        D = 1e-3
        mySectList = []
        mySectList.append(RoundSection(distance1 = 0, distance2 = 0.7, diameter = 65*D))
        mySectList.append(SquareSection(distance1 = 0.7, distance2 = 1.4, sideLength = 60*D))
        mySectList.append(ThickRoundSection(distance1 = 1.4, distance2 = 2.1, outerDiameter = 70*D, innerDiameter = 35*D))

        F = 1e3
        myLoadList = []
        myLoadList.append(Torque(distance = 0.4, value = 0.5*F, direction=Direction.CounterClockwise))
        myLoadList.append(Torque(distance = 0.8, value = 0.6*F, direction=Direction.Clockwise))
        myLoadList.append(Torque(distance = 1.55, value = 1.1*F, direction=Direction.CounterClockwise))

        myTask = Task(
                taskType = myTaskType,
                length = L,
                sectionList = mySectList,
                loadList = myLoadList,
                material = myMaterial
        )

        myTask.solve()

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

myTask = Task()
myTask.prompt()

# tcTask()
# torsionTask()
# bendTask()
