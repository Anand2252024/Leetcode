from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        # Optimize by iterating over the smaller dimension
        if m > n:
            matrix = list(zip(*matrix))
            m, n = n, m

        ans = float("-inf")

        for left in range(n):
            row_sum = [0] * m

            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]

                prefix = 0
                prefix_sums = [0]

                for s in row_sum:
                    prefix += s

                    idx = bisect.bisect_left(prefix_sums, prefix - k)
                    if idx < len(prefix_sums):
                        ans = max(ans, prefix - prefix_sums[idx])

                    bisect.insort(prefix_sums, prefix)

        return ans