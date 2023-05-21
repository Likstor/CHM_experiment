import numpy as np
import matplotlib.pyplot as plt
from main import PercolationStats

# реализовал Новосерьянц Эдуард Отарикович

N = T = int(input('Введите размер решётки: '))

x = list(range(2, N))
y = list(range(2, T))

list_exp = zip(list(range(2, N)), list(range(2, T)))
confidense_1 = []
confidense_2 = []
for exp in list_exp:
    ps = PercolationStats()
    ps.doExperiment(*exp)
    res = ps.confidence()
    confidense_1.append(res[0])
    confidense_2.append(res[1])

res_1 = []
res_2 = []
for num in y:
    res_1.append(num - confidense_1.pop(0))
    res_2.append(num + confidense_2.pop(0))


plt.plot(x, y)
plt.title('Confidence Interval of a function')
plt.xlabel('N')
plt.ylabel('T')
plt.fill_between(x, res_1, res_2, alpha=0.5)
plt.show()