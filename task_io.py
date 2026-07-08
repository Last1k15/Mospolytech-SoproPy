import matplotlib.pyplot as plt

# Вывести заголок
def printHeader(header=''):
	val = 60 - len(header)
	line = '-'*int(val/2)
	print(line + header + line)


# Вывести общие данные и результаты в текстовом формате
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

	# Искомые величины из решения
	for k,v in solution.items():
		printHeader(k)
		print(v)

	print('='*60)


# Построить эпюры по выходным массивам
def plotDiagram(self, solution):

	i = 1 # счетчик окон
	for k,v in solution.items():

		# Пропустим величины без метки "изобразить на эпюре"
		if (v[1] == False):
			continue

		plt.figure(i)
		i += 1
		plt.title(k)

		# Научная нотация
		plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

		# На оси абсцисс предотвратим наложение смежных величин, отличных на BIAS - округлим и удалим дубликаты
		plt.xticks(list(set([round(n, 3) for n in self.dotList])))
		plt.yticks(v[0])

		plt.plot(self.dotList, v[0], 'o-') # изобразим эпюру, выделим точки
		plt.plot(self.dotList, [0]*len(self.dotList)) # изобразим стержень

	plt.show()

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
