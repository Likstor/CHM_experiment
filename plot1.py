import matplotlib.pyplot as plt
from main import PercolationStats
from percolation_qu import Percolation

# реализовал Ухов Игорь Викторович

while True:
    type = input('Выберите, от чего хотите график зависимости - N или T: ')

    if type == 'N':
        N = int(input('Введите N: '))
        for i in range(10, N + 1, 5):
            z = PercolationStats()
            z.doExperiment(i, 2)
            plt.plot(z.confidence(), [i, i])
        break
    elif type == 'T':
        T = int(input('Введите T: '))
        for i in range(10, T + 1, 5):
            z = PercolationStats()
            z.doExperiment(i, 2)
            plt.plot(z.confidence(), [i, i])
        break

plt.show()