def printData(self):
	print(f"{self.taskType.name = }")
	print(self.material)

	print("\n\nSECTIONS")
	for sect in self.sectionList:
		print(sect)

	print("\n\nLOADS")
	for load in self.loadList:
		print(load,type(load))
	print("\n\nDOTS")
	print(self.dotList)
	print("\n\n")

def interactWithUser(self):
	inp = "_"
	while (inp not in "123"):
		inp = input("Тип задачи?\nРастяжение-Сжатие = 1\nКручение = 2\nИзгиб = 3\n-> ")
	self.taskType = self.TaskType(int(inp)).name
	while (True):
		inp = input("Длина стержня?\n-> ")
		try:
			self.length = int(inp)
			break
		except ValueError:
			continue
