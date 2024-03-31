import numpy as np


class Solution:
    def fib(self, n: int) -> int:
        A = np.matrix([[0, 1], [1, 1]])
        x = np.matrix([[0], [1]])

        return int(np.matmul(A ** n, x)[0])
