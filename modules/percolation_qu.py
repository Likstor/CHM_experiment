class Percolation:
    def __init__(self, size: int) -> None:
        self.__matrix = [[False] * size for _ in range(size)]
        
    @property
    def matrix(self) -> list:
        return self.__matrix
        
    def open(self, string: int, column: int) -> None:
        self._matrix[string][column] = True
        
    def isOpen(self, string: int, column: int) -> bool:
        return self._matrix[string][column]
        
    def isFull(self, string: int, column: int) -> bool:
        return self._matrix[string][column]
        
    def percolates(self) -> bool:
        ...