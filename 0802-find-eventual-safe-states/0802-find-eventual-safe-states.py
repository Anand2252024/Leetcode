from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n  # 0=unvisited, 1=visiting, 2=safe
        
        def dfs(node: int) -> bool:
            if state[node] != 0:
                return state[node] == 2  # already safe or unsafe
            state[node] = 1  # mark as visiting
            for nei in graph[node]:
                if state[nei] == 2:  # neighbor already safe
                    continue
                if state[nei] == 1 or not dfs(nei):  # cycle detected
                    return False
            state[node] = 2  # mark as safe
            return True
        
        return [i for i in range(n) if dfs(i)]
