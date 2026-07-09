from section import *
from load import *
import matplotlib.pyplot as plt

# Вывести заголок
def printHeader(header=''):
	val = 60 - len(header)
	line = '-'*int(val/2)
	print(line + header + line)


# Вывести общие данные и результаты в текстовом формате
def printData(self, solution = dict()):
	print('='*60)

	printHeader(self.taskType.name)
	match self.taskType:
		case self.TaskType.TensionCompression:
			print(
				f"youngsModulus:  {self.material.youngsModulus}",
				f"poissonsRatio:  {self.material.poissonsRatio}",
				f"yieldStrength:  {self.material.yieldStrength}",
				sep="\n"
			)
		case self.TaskType.Torsion:
			print(
				f"youngsModulus:  {self.material.youngsModulus}",
				f"poissonsRatio:  {self.material.poissonsRatio}",
				f"shearModulus:  {self.material.yieldStrength}",
				sep="\n"
			)

		case self.TaskType.Bend:
			print(
				f"youngsModulus:  {self.material.youngsModulus}",
				f"poissonsRatio:  {self.material.poissonsRatio}",
				f"yieldStrength:  {self.material.yieldStrength}",
				sep="\n"
			)


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
		print(v[0])

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
		ax = plt.gca()
		ax.grid(True, linestyle=':', alpha=0.7)

		# Научная нотация
		plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

		# На оси абсцисс предотвратим наложение смежных величин, отличных на BIAS - округлим и удалим дубликаты
		plt.xticks(list(set([round(n, 3) for n in self.dotList])))
		plt.yticks(v[0])

		plt.plot(self.dotList, v[0], 'o-', linewidth=3, color="lightblue") # изобразим эпюру, выделим точки
		plt.plot(self.dotList, [0]*len(self.dotList), linewidth=5, color="orange") # изобразим стержень

		for (xi, mi) in zip(self.dotList, v[0]):
			ax.annotate(f'{mi:.1e}', (xi, mi), textcoords="offset points", xytext=(0, 10 if mi >= 0 else -15), 
						ha='center', fontsize=12, color='black')

	plt.show()


def prompt(self):

	def askNum(request : str):
		while (True):
			out = 0
			inp = input(request)

			if (inp == ""):
				return 0

			try:
				out = float(inp)
				break
			except ValueError:
				continue

		return out

	def askOption(request : str, options : list):
		inp = "-1"
		while (inp not in options):
			inp = input(request).upper()
			if (inp == ""):
				return -1
			
		return inp

	def askSections():
		while (True):
			print("Простое (0), Круглое (1), Толстостенное круглое (2), Тонкостенное круглое (3), Квадратное (4), Тавр (5), Двутавр (6), Полое Прямоугольное (7)")
			print("Чтобы закончить, отправьте пустой ввод")
			sectOption = int(askOption("Выберите сечение из списка\n-> ", [str(n) for n in list(range(8))]))
			match sectOption:
				case -1:
					break
				case 0:
					self.sectionList.append(Section(
						distance1 = float(askNum("distance1: ")),
						distance2 = float(askNum("distance2: ")),
						area = float(askNum("area: ")),
					))
				case 1:
					self.sectionList.append(RoundSection(
						distance1 = float(askNum("distance1: ")),
						distance2 = float(askNum("distance2: ")),
						diameter = float(askNum("diameter: ")),
					))
				case 2:
					self.sectionList.append(ThickRoundSection(
						distance1 = float(askNum("distance1: ")),
						distance2 = float(askNum("distance2: ")),
						outerDiameter = float(askNum("outerDiameter: ")),
						innerDiameter = float(askNum("innerDiameter: ")),
					))
				case 3:
					self.sectionList.append(ThinRoundSection(
						distance1 = float(askNum("distance1: ")),
						distance2 = float(askNum("distance2: ")),
						outerDiameter = float(askNum("outerDiameter: ")),
						innerDiameter = float(askNum("innerDiameter: ")),
					))
				case 4:
					self.sectionList.append(SquareSection(
						distance1 = float(askNum("distance1: ")),
						distance2 = float(askNum("distance2: ")),
						sideLength = float(askNum("sideLength: ")),
					))
				case 5:
					self.sectionList.append(TBeamSection(
						distance1 = float(askNum("distance1: ")),
						distance2 = float(askNum("distance2: ")),
						width = float(askNum("width: ")),
						height = float(askNum("height: ")),
						thickness1 = float(askNum("thickness1: ")),
						thickness2 = float(askNum("thickness2: ")),
					))
				case 6:
					self.sectionList.append(IBeamSection(
						distance1 = float(askNum("distance1: ")),
						distance2 = float(askNum("distance2: ")),
						width = float(askNum("width: ")),
						height = float(askNum("height: ")),
						innerThickness = float(askNum("innerThickness: ")),
						thickness1 = float(askNum("thickness1: ")),
						thickness2 = float(askNum("thickness2: ")),
					))
				case 7:
					self.sectionList.append(HollowSquareSection(
						distance1 = float(askNum("distance1: ")),
						distance2 = float(askNum("distance2: ")),
						sideLength = float(askNum("sideLength: ")),
						thickness = float(askNum("thickness: ")),
					))
	
	def askTCLoads():
		while (True):
			endPrompt = input("Добавить продольную силу?(1/0)")
			if (endPrompt == "1"):
				self.loadList.append(AxialForce(
					distance = float(askNum("distance: ")),
					value = float(askNum("value: ")),
					direction = Direction.Left if askOption("direction: ", ["LEFT", "RIGHT"]) == "LEFT" else Direction.Right
				))
			else: break

	def askTorsionLoads():
		while (True):
			endPrompt = input("Добавить крутящий момент?(1/0)")
			if (endPrompt == "1"):
				self.loadList.append(Torque(
					distance = float(askNum("distance: ")),
					value = float(askNum("value: ")),
					direction = Direction.Clockwise if askOption("direction: ", ["CLOCKWISE", "COUNTERCLOCKWISE"]) == "CLOCKWISE" else Direction.CounterClockwise
				))
			else: break

	def askBendLoads():
		while (True):
			print("Поперечная сила (0), Распределенная нагрузка (1), Изгибающий момент (2)")
			print("Чтобы закончить, отправьте пустой ввод")
			loadOption = int(askOption("Выберите нагрузку из списка\n-> ", [str(n) for n in list(range(3))]))
			match loadOption:
				case -1:
					break
				case 0:
					self.loadList.append(ShearForce(
						distance = float(askNum("distance: ")),
						value = float(askNum("value: ")),
						direction = Direction.Up if askOption("direction: ", ["UP", "DOWN"]) == "UP" else Direction.Down
					))
				case 1:
					self.loadList.append(DistrLoad(
						distance1 = float(askNum("distance1: ")),
						distance2 = float(askNum("distance2: ")),
						value = float(askNum("value: ")),
						direction = Direction.Up if askOption("direction: ", ["UP", "DOWN"]) == "UP" else Direction.Down
					))
				case 2:
					self.loadList.append(BendMoment(
						distance = float(askNum("distance: ")),
						value = float(askNum("value: ")),
						direction = Direction.Clockwise if askOption("direction: ", ["CLOCKWISE", "COUNTERCLOCKWISE"]) == "CLOCKWISE" else Direction.CounterClockwise
					))

	self.taskType = self.TaskType(int(askOption("Тип задачи?\nРастяжение-Сжатие = 0\nКручение = 1\nИзгиб = 2\n-> ", [str(n) for n in list(range(3))])))
	self.length = askNum("Длина стержня?\n-> ")

	match self.taskType:
		case self.TaskType.TensionCompression:
			self.material.youngsModulus = askNum("Модуль Юнга?\n-> ")
			self.material.yieldStrength = askNum("Предел текучести?\n-> ")
			askSections()
			askTCLoads()
		case self.TaskType.Torsion:
			self.material.shearModulus = askNum("Модуль сдвига?\n-> ")
			if (self.material.shearModulus == 0):
				self.material.youngsModulus = askNum("Модуль Юнга?\n-> ")
				self.material.poissonsRatio = askNum("Коэффициент Пуассона?\n-> ")
			askSections()
			askTorsionLoads()
		case self.TaskType.Bend:
			askSections()
			askBendLoads()

	self.solve()
