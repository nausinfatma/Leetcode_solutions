import numpy as np

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        
        arr = np.array(matrix)

        arr = np.sort(arr.flatten())
        arr = arr.tolist()

        return arr[k-1]