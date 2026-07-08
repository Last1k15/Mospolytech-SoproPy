from load import *
def TorsionAlgorithm(self):
	torsionMomentList = []
	angularTensionList = []
	displacementList = []
	strainList = []

	prevDot = self.dotList[-1]
	for dot in reversed(self.dotList):
		torsionMoment = 0
		for load in reversed(self.loadList):
			if (load.distance > dot):
				sign = (-1 if (load.direction == Direction.Clockwise) else 1)
				torsionMoment += load.value * sign
			else: break
		torsionMomentList.append(torsionMoment)
		for sect in reversed(self.sectionList):
			if (sect.distance1 <= dot and sect.distance2 >= dot): 
				angularTensionList.append(torsionMoment / sect.resistanceMoment)
				displacementList.append((torsionMoment * (prevDot - dot)) / (self.material.shearModulus * sect.inertiaMoment))
				break
		prevDot = dot

	torsionMomentList = torsionMomentList[::-1]
	angularTensionList = angularTensionList[::-1]
	displacementList = displacementList[::-1]

	strain = 0
	for i in range(len(self.dotList)):
		strainList.append(strain)
		strain += displacementList[i]

	solution = {"TORSION MOMENT":[torsionMomentList, True], "ANGULAR TENSIONS":[angularTensionList, True], "DISPLACEMENTS":[displacementList, False], "STRAINS":[strainList, True]}
	return solution
