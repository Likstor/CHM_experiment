import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from percolation_qu import Percolation
from main import PercolationStats

# реализовал Ухов Игорь Викторович

while True:
    type = input('Выберите, от чего хотите график зависимости - N или T: ')

    if type == 'N':
        N = int(input('Введите N: '))
        for i in range(10, N + 1, 5):
            z = PercolationStats()
            z.doExperiment(i, 2)
            ax = sns.lineplot(z.confidence())
        break
    elif type == 'T':
        T = int(input('Введите T: '))
        for i in range(10, T + 1, 5):
            z = PercolationStats()
            z.doExperiment(i, 2)
            ax = sns.lineplot(z.confidence())
        break

plt.show()