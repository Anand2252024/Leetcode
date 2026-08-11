from typing import List
from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        @lru_cache(None)
        def solve(exp):
            res = []

            for i, ch in enumerate(exp):
                if ch in "+-*":
                    left = solve(exp[:i])
                    right = solve(exp[i + 1:])

                    for l in left:
                        for r in right:
                            if ch == "+":
                                res.append(l + r)
                            elif ch == "-":
                                res.append(l - r)
                            else:
                                res.append(l * r)

            if not res:
                res.append(int(exp))

            return res

        return solve(expression)