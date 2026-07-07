import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.linspace(0, 1e6, 100)

plt.plot(x, y)
# plt.gca().yaxis.set_major_formatter(plt.ScalarFormatter(useMathText=True))
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.show()
