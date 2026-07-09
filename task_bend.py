from load import *
def BendAlgorithm(self):
	shearForceList = [] # Поперечные силы
	bendMomentList = [] # Изгибающие моменты

	for dot in reversed(self.dotList):
		shearForce = 0
		bendMoment = 0

		for load in reversed(self.loadList):
			match load:
				case DistrLoad():
					if (load.distance2 > dot):
						shearSign = (-1 if (load.direction == Direction.Up) else 1) # правило знаков для поперечных сил
						shearForce += (load.distance2 - max(dot, load.distance)) * load.value * shearSign

						leverage = (load.distance2 - max(dot, load.distance)) * 0.5 + max(load.distance, dot) - dot # плечо силы
						bendMoment += (load.distance2 - max(dot, load.distance)) * load.value * leverage * -shearSign # изгибающие моменты с обратным знаком к поперечным силам

				case ShearForce():
					if (load.distance > dot):
						shearSign = (-1 if (load.direction == Direction.Up) else 1)
						shearForce += load.value * shearSign
						leverage = load.distance - dot
						bendMoment += load.value * -shearSign * leverage

				case BendMoment():
					if (load.distance > dot):
						bendSign = (-1 if (load.direction == Direction.Clockwise) else 1) # правило знаков для изгибающих моментов
						bendMoment += load.value * bendSign

		shearForceList.append(shearForce)
		bendMomentList.append(bendMoment)

	# Массивы заполнялись по движению к заделке, перевернем, чтобы получить массивы от заделки
	shearForceList = shearForceList[::-1]
	bendMomentList = bendMomentList[::-1]

	# Булево значение "изобразить на эпюре"
	solution = {
		"SHEAR POWERS" : [shearForceList, True],
		"BEND MOMENTS" : [bendMomentList, True]
	}

	return solution
