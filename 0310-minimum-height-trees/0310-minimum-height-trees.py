from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [set() for _ in range(n)]

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = deque()

        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        remaining = n

        while remaining > 2:
            size = len(leaves)
            remaining -= size

            for _ in range(size):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)