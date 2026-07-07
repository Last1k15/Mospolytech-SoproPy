from load import *
from section import *
def validateSections(self):
    lengthSum = 0
    for sect in self.sectionList:
        lengthSum += (sect.distance2 - sect.distance1)
    if (lengthSum != self.length):
        raise ValueError("Sections are not valid")

def validateLoads(self):
    for load in self.loadList:

        badTensionCompressionTypes = self.taskType == self.TaskType.TensionCompression and not isinstance(load, ConcPower)
        badTorsionTypes = self.taskType == self.TaskType.Torsion and not isinstance(load, TorsionMoment)
        badBendTypes = self.taskType == self.TaskType.Bend and isinstance(load, TorsionMoment)

        if (badTensionCompressionTypes or badTorsionTypes or badBendTypes):
            raise ValueError("Load types are not valid")

        if (0 <= load.distance > self.length):
            raise ValueError("Load distances are not valid")
