class Solution(object):
    def remainingMethods(self, n, k, invocations):
        from collections import defaultdict, deque
        
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
        
        # Step 2: Find suspicious set via BFS/DFS
        suspicious = set()
        queue = deque([k])
        while queue:
            node = queue.popleft()
            if node in suspicious:
                continue
            suspicious.add(node)
            for nei in graph[node]:
                if nei not in suspicious:
                    queue.append(nei)
        
        # Step 3: Check incoming edges
        for a, b in invocations:
            if b in suspicious and a not in suspicious:
                # Removal impossible
                return list(range(n))
        
        # Step 4: Return remaining methods
        return [i for i in range(n) if i not in suspicious]
