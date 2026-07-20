from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        
        # Flatten the grid
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        
        # Effective shift
        k %= total
        
        # Perform the shift
        shifted = flat[-k:] + flat[:-k]
        
        # Reshape back into m x n
        result = []
        for i in range(m):
            row = shifted[i*n:(i+1)*n]
            result.append(row)
        
        return result
