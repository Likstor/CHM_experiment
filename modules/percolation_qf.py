class Percolation:
    def __init__(self, N):
        self.matrix = [[(False)] * N for y in range(N)]
        self.uf = QuickFind()
        for _ in range(N**2):
            self.uf.make_set()

    def open(self, i: int, j: int) -> None:
        self.matrix[i][j] = True
        if j - 1 > -1 and self.isOpen(i, j - 1):
            self.uf.union_set(j + i * len(self.matrix), j-1 + i * len(self.matrix))

        if j + 1 < len(self.matrix) and self.isOpen(i, j + 1):
            self.uf.union_set(j + i * len(self.matrix), j+1 + i * len(self.matrix))

        if i - 1 > -1 and self.isOpen(i - 1, j):
            self.uf.union_set(j + i * len(self.matrix), j + (i-1) * len(self.matrix))

        if i + 1 < len(self.matrix) and self.isOpen(i + 1, j):
            self.uf.union_set(j + i * len(self.matrix), j + (i+1) * len(self.matrix))

    def isOpen(self, i: int, j: int) -> bool:
        return self.matrix[i][j]

    def isFull(self, i: int, j: int) -> bool:
        if not self.isOpen(i, j):
            return False

        for x in range(len(self.matrix)):
            if self.uf.connected(x, j + i * len(self.matrix)):
                return True

        return False

    def percolates(self):
        for i in range(len(self.matrix)):
            if self.isFull(len(self.matrix) - 1, i):
                return True

        return False

    def __str__(self):
        output = '    ' + \
            '     '.join(map(str, range(len(self.matrix)))) + '\n'
        idx = 0

        while True:
            output += f'{idx} ' + \
                      ' '.join(map(lambda x: f'{x} ' if x is True else str(x), self.matrix[idx]))
            idx += 1

            if idx < len(self.matrix):
                output += '\n'
                continue

            break

        return output



class QuickFind:
    def __init__(self) -> None:
        self.__id = []

    def make_set(self) -> None:
        self.__id.append(len(self.__id))

    def find_set(self, x: int) -> int:
        return self.__id[x]

    def __str__(self) -> str:
        return ' '.join(map(str, self.__id))

    def union_set(self, x: int, y: int) -> None:
        idx = self.__id[x]
        idy = self.__id[y]

        for i in range(len(self.__id)):
            if self.__id[i] == idy:
                self.__id[i] = idx

    def connected(self, x: int, y: int) -> bool:
        return self.__id[x] == self.__id[y]
