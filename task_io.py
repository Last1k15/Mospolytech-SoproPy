def printHeader(header=''):
	val = 60 - len(header)
	line = '-'*int(val/2)
	print(line + header + line)

def printData(self, solution = dict()):
	print('='*60)

	printHeader("TASK INFO")
	print(self.taskType.name)
	print(self.material)

	printHeader("SECTIONS")
	for sect in self.sectionList:
		print(sect)

	printHeader("LOADS")
	for load in self.loadList:
		print(load)

	printHeader("DOTS")
	print(self.dotList)

	for k,v in solution.items():
		printHeader(k)
		print(v)

	print('='*60)

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
