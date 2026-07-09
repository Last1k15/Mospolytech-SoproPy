from load import *
def TorsionAlgorithm(self):
	torqueList = [] # Крутящие моменты
	shearStressList = [] # Касательные напряжения
	deformationList = [] # Угловые деформации
	displacementList = [] # Угловые перемещения

	prevDot = self.dotList[-1]
	for dot in reversed(self.dotList):

		torque = 0

		# Для каждой точки рассмотрим нагрузки справа от неё
		for load in reversed(self.loadList):
			passedLoad = (load.distance > dot)
			if (passedLoad): # Прошли нагрузку
				sign = (-1 if (load.direction == Direction.Clockwise) else 1) # правило знаков при кручении
				torque += load.value * sign
			else: break
		torqueList.append(torque)

		# Найдем сечение, в котором расположена точка
		for sect in reversed(self.sectionList):
			insideSection = (sect.distance1 <= dot and sect.distance2 >= dot)
			if (insideSection): # точка в этом сечении
				shearStressList.append(torque / sect.sectionModulus)
				deformationList.append((torque * (prevDot - dot)) / (self.material.shearModulus * sect.axialInertiaMoment))
				break

		prevDot = dot

	# Массивы заполнялись по движению к заделке, перевернем, чтобы получить массивы от заделки
	torqueList = torqueList[::-1]
	shearStressList = shearStressList[::-1]
	deformationList = deformationList[::-1]

	# При отдалении от заделки угловые перемещения накапливаются
	displacement = 0
	for i in range(len(self.dotList)):
		displacementList.append(displacement)
		displacement += deformationList[i]

	# Булево значение "изобразить на эпюре"
	solution = {
		"TORQUE" : [torqueList, True],
		"SHEAR STRESS" : [shearStressList, True],
		"DEFORMATIONS" : [deformationList, False],
		"DISPLACEMENTS" : [displacementList, True]
	}

	return solution
