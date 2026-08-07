from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(index, path, value, prev):
            if index == len(num):
                if value == target:
                    res.append(path)
                return

            for i in range(index, len(num)):
                # Skip numbers with leading zeros
                if i > index and num[index] == '0':
                    break

                curr_str = num[index:i + 1]
                curr = int(curr_str)

                if index == 0:
                    dfs(i + 1, curr_str, curr, curr)
                else:
                    dfs(i + 1, path + "+" + curr_str, value + curr, curr)
                    dfs(i + 1, path + "-" + curr_str, value - curr, -curr)
                    dfs(
                        i + 1,
                        path + "*" + curr_str,
                        value - prev + prev * curr,
                        prev * curr
                    )

        dfs(0, "", 0, 0)
        return res