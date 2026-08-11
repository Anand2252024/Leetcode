from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a min-heap based on squared distance
        return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
