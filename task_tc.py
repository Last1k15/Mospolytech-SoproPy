from load import *

def TensionCompressionAlgorithm(self):
	normalForceList = [] # нормальные силы
	normalStressList = [] # нормальные напряжения
	deformationList = [] # абсолютные деформации
	displacementList = [] # перемещения

	prevDot = self.dotList[-1]

	# Заделка слева, идем к заделке справа налево
	for dot in reversed(self.dotList):

		normalForce = 0
		for load in reversed(self.loadList):
			passedLoad = (load.distance > dot) # Прошли нагрузку
			if (passedLoad):
				sign = (-1 if (load.direction == Direction.Left) else 1) # правило знаков при растяжении-сжатии
				normalForce += load.value * sign
			else: break # нагрузки далее еще не пройдены, не имеет смысла продолжать для этой точки
		normalForceList.append(normalForce)

		# Найдем сечение, в котором расположена точка
		for sect in reversed(self.sectionList):
			insideSection = (sect.distance1 <= dot and sect.distance2 >= dot)
			if (insideSection): # точка в этом сечении
				normalStressList.append(normalForce / sect.area)
				deformationList.append((normalForce * (prevDot - dot)) / (self.material.youngsModulus * sect.area))
				break
		prevDot = dot

	# Массивы заполнялись по движению к заделке, перевернем, чтобы получить массивы от заделки
	normalForceList = normalForceList[::-1]
	normalStressList = normalStressList[::-1]
	deformationList = deformationList[::-1]

	# Запас по текучести
	safetyFactor = self.material.yieldStrength / max([abs(n) for n in normalStressList])

	# При отдалении от заделки перемещения накапливаются
	displacement = 0
	for i in range(len(self.dotList)):
		displacementList.append(displacement)
		displacement += deformationList[i]

	# Булево значение "изобразить на эпюре"
	solution = {
		"NORM POWERS" : [normalForceList, True],
		"NORM TENSIONS" : [normalStressList, True],
		"DEFORMATIONS" : [deformationList, False],
		"DISPLACEMENTS" : [displacementList, True],
		"SAFETY FACTOR" : [safetyFactor, False]
	}

	return solution
