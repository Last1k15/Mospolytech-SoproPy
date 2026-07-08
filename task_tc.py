from load import *
def TensionCompressionAlgorithm(self):
	normalForceList = []
	normalStressList = []
	displacementList = []
	strainList = []

	prevDot = self.dotList[-1]
	for dot in reversed(self.dotList):
		normalForce = 0
		for load in reversed(self.loadList):
			if (load.distance > dot):
				sign = (-1 if load.direction == Direction.Left else 1)
				normalForce += load.value * sign
			else: break
		normalForceList.append(normalForce)
		for sect in reversed(self.sectionList):
			if (sect.distance1 <= dot and sect.distance2 >= dot): 
				normalStressList.append(normalForce / sect.area)
				displacementList.append((normalForce * (prevDot - dot)) / (self.material.youngModulus * sect.area))
				break
		prevDot = dot

	normalForceList = normalForceList[::-1]
	normalStressList = normalStressList[::-1]
	displacementList = displacementList[::-1]
	safetyFactor = self.material.yieldStrength / max([abs(n) for n in normalStressList])

	strain = 0
	for i in range(len(self.dotList)):
		strainList.append(strain)
		strain += displacementList[i]

	solution = {
		"NORM POWERS" : [normalForceList, True],
		"NORM TENSIONS" : [normalStressList, True],
		"DISPLACEMENTS" : [displacementList, False],
		"STRAINS" : [strainList, True],
		"SAFETY FACTOR" : [safetyFactor, False]
	}
	return solution
