def TensionCompressionAlgorithm(self):
	normPowerList = []
	normTensionList = []
	displacementList = []
	strainList = []

	prevDot = self.dotList[-1]
	for dot in reversed(self.dotList):
		normPower = 0
		for load in reversed(self.loadList):
			if (load.distance > dot):
				normPower += load.value
			else: break
		normPowerList.append(normPower)
		for sect in reversed(self.sectionList):
			if (sect.distance1 <= dot and sect.distance2 >= dot): 
				normTensionList.append(normPower / sect.area)
				displacementList.append((normPower * (prevDot - dot)) / (self.material.youngModulus * sect.area))
				break
		prevDot = dot

	normPowerList = normPowerList[::-1]
	normTensionList = normTensionList[::-1]
	displacementList = displacementList[::-1]
	safetyFactor = self.material.fluidityMargin / max([abs(n) for n in normTensionList])

	strain = 0
	for i in range(len(self.dotList)):
		strainList.append(strain)
		strain += displacementList[i]

	solution = {"NORM POWERS":[normPowerList, True], "NORM TENSIONS":[normTensionList, True], "DISPLACEMENTS":[displacementList, False], "STRAINS":[strainList, True], "SAFETY FACTOR":[safetyFactor, False]}
	return solution
