from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0

        queue = deque([s])
        visited = {s}
        result = []

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                curr = queue.popleft()

                if isValid(curr):
                    result.append(curr)

                if result:
                    continue

                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue

                    nxt = curr[:i] + curr[i + 1:]

                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

            if result:
                return result

        return [""]