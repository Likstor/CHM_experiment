class QuickUnion: # реализовал Новосерьянц Эдуард Отарикович
    def __init__(self, size: int = None) -> None:
        self._id = [] if size is None else list(range(size ** 2))
        self._size = [] if size is None else [1] * (size ** 2)

    def make_set(self) -> None:
        self._id.append(len(self._id))
        self._size.append(1)

    def find_set(self, x: int) -> int:
        return self._id[x]

    def __str__(self) -> str:
        str_1 = ' '.join(map(str, self._id))
        str_2 = ' '.join(map(str, self._size))
        return str_1 + '\n' + str_2

    def root(self, x: int) -> int:
        if x == self._id[x]:
            return x

        self._id[x] = self.root(self._id[x])
        return self._id[x]

    def union_set(self, x: int, y: int) -> None:
        root_x = self.root(x)
        root_y = self.root(y)

        if root_x == root_y:
            return

        if self._size[root_x] < self._size[root_y]:
            self._id[root_x] = root_y
            self._size[root_y] += self._size[root_x]
            return

        self._id[root_y] = root_x
        self._size[root_x] += self._size[root_y]

    def connected(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)


class Percolation: # реализовал Новосерьянц Эдуард Отарикович
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
        return self._matrix

    def isOpen(self, string: int, column: int) -> bool:
        return self._matrix[string][column]

    def open(self, string: int, column: int) -> None:
        self._matrix[string][column] = True
        pos_uf = string * len(self._matrix) + column

        if column - 1 > -1 and self.isOpen(string, column - 1):
            self._uf.union_set(pos_uf, column - 1 + string * len(self._matrix))

        if column + 1 < len(self._matrix) and self.isOpen(string, column + 1):
            self._uf.union_set(pos_uf, column + 1 + string * len(self._matrix))

        if string - 1 > -1 and self.isOpen(string - 1, column):
            self._uf.union_set(pos_uf, column + (string - 1)
                               * len(self._matrix))

        if string + 1 < len(self._matrix) and self.isOpen(string + 1, column):
            self._uf.union_set(pos_uf, column + (string + 1)
                               * len(self._matrix))

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