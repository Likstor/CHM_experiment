import random
from percolation_qu import Percolation
from typing import List
from tqdm import tqdm


class PercolationStats:
    def mean(self, exp_result: List[float], exp_count: int) -> float:
        return sum(exp_result) / exp_count

    def stddev(self, exp_result: List[float], exp_count: int, mean: float) -> float:
        return ((sum([(num - mean) ** 2 for num in exp_result])) / (exp_count - 1)) ** 0.5

    def confidence(self, exp_count: int, mean: float, stddev: float) -> float:
        return [mean - (1.96 * stddev) / (exp_count ** 0.5), mean + (1.96 * stddev) / (exp_count ** 0.5)]

    def doExperiment(self, size: int, count_exp: int) -> None:
        if size <= 0 or count_exp <= 0:
            raise ValueError('N <= 0' if size <= 0 else 'T <= 0')

        exp_result = []
        exp_num = 0

        bar = tqdm(total=count_exp)
        while exp_num <= count_exp:
            p_matrix = Percolation(size)
            counter = 0
            while not p_matrix.percolates():
                pos = [random.randint(0, size - 1),
                       random.randint(0, size - 1)]

                if p_matrix.isOpen(*pos):
                    continue

                p_matrix.open(*pos)
                counter += 1

            exp_num += 1
            exp_result.append(counter / (size ** size))
            bar.update(1)
        bar.close()

        mean = self.mean(exp_result, count_exp)
        stddev = self.stddev(exp_result, count_exp, mean)
        confidence = self.confidence(count_exp, mean, stddev)
        print(
            f'mean                    = {mean}\nstddev                  = {stddev}\n95% confidence interval = {confidence[0]}, {confidence[1]}')


if __name__ == '__main__':
    print('ДЗ №2 "Просачивание"')
    
    while True:
        dsu_type = input('Выберите тип СНМ (qf или qu): ')
        
        if dsu_type == 'qf':
            from percolation_qf import Percolation
            break
        elif dsu_type == 'qu':
            from percolation_qu import Percolation
            break
        else:
            print('Неизвестный тип СНМ, попробуйте еще раз.')
    
    while True:
        size_matrix = input('Введите размер решетки: ')
        try:
            size_matrix = int(size_matrix)
            break
        except:
            print('Некорректный тип данных, попробуйте еще раз.')

    while True:
        count_trials = input('Введите количество испытаний: ')
        try:
            count_trials = int(count_trials)
            break
        except:
            print('Некорректный тип данных, попробуйте еще раз.')
            
    ps = PercolationStats()
    ps.doExperiment(size_matrix, count_trials)
