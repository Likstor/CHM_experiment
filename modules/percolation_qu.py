class Percolation:
    def __init__(self, size: int) -> None:
        self._matrix = [[False] * size for _ in range(size)]
        self._uf = UnionFind(size)

    def __str__(self):
        len_size = len(str(len(self._matrix)))
        output = '   ' + \
            ' '.join(map(lambda x: str(x).center(5),
                         range(len(self._matrix)))) + '\n'
        idx = 0

        while True:
            output += str(idx).center(len_size) + ' ' + ' '.join(
                map(lambda x: f'{x} ' if x is True else str(x), self._matrix[idx]))
            idx += 1

            if idx < len(self._matrix):
                output += '\n'
                continue

            break

        return output
      
    @property
    def matrix(self) -> list:
        return self.__matrix
        
    def open(self, string: int, column: int) -> None:
        self._matrix[string][column] = True
        
    def isOpen(self, string: int, column: int) -> bool:
        return self._matrix[string][column]
        
    def isFull(self, string: int, column: int) -> bool:
        if not self.isOpen(string, column):
            return False

        pos_uf = string * len(self._matrix) + column

        for i in range(len(self._matrix)):
            if self._uf.connected(i, pos_uf):
                return True

        return False

    def percolates(self) -> bool:
        for i in range(len(self._matrix)):
            if self.isFull(len(self._matrix) - 1, i):
                return True

        return False