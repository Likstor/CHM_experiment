class Percolation:
    def __init__(self, N):
        self.matrix = [[(False)] for x in range(N)]

    def open(self, i: int, j: int) -> None:
        self.matrix[i][j] = True

    def isOpen(self, i: int, j: int) -> bool:
        return self.matrix[i][j]

    def isFull(self, i: int, j: int) -> bool:
        return self.matrix[i][j]

    def percolates(self):
        ...