from load import *
def BendAlgorithm(self):
	shearForceList = []
	bendMomentList = []

	for dot in reversed(self.dotList):
		shearForce = 0
		bendMoment = 0
		for load in reversed(self.loadList):
			match load:
				case DistrLoad():
					if (load.distance2 > dot):
						shearSign = (-1 if (load.direction == Direction.Up) else 1)
						shearForce += (load.distance2 - max(dot, load.distance)) * load.value * shearSign

						leverage = (load.distance2 - max(dot, load.distance)) * 0.5 + max(load.distance, dot) - dot
						bendMoment += (load.distance2 - max(dot, load.distance)) * load.value * leverage * -shearSign

				case ShearForce():
					if (load.distance > dot):
						shearSign = (-1 if (load.direction == Direction.Up) else 1)
						shearForce += load.value * shearSign
						leverage = load.distance - dot
						bendMoment += load.value * -shearSign * leverage

				case BendMoment():
					if (load.distance > dot):
						bendMoment += load.value * (-1 if (load.direction == Direction.Clockwise) else 1)

		shearForceList.append(shearForce)
		bendMomentList.append(bendMoment)

	shearForceList = shearForceList[::-1]
	bendMomentList = bendMomentList[::-1]

	solution = {"SHEAR POWERS":[shearForceList, True], "BEND MOMENTS":[bendMomentList, True]}
	return solution
