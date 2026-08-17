from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        # bestL[l][r] = max over k in [l, r] of (sum(l..k) + dp[l][k])
        # bestR[l][r] = max over k in [l, r] of (sum(k..r) + dp[k][r])
        bestL = [[0] * n for _ in range(n)]
        bestR = [[0] * n for _ in range(n)]

        for i in range(n):
            bestL[i][i] = stoneValue[i]
            bestR[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                total = prefix[r + 1] - prefix[l]

                # pos1: largest k in [l, r-1] with 2*leftSum(k) <= total  (left <= right)
                lo, hi = l, r - 1
                pos1 = l - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if 2 * (prefix[mid + 1] - prefix[l]) <= total:
                        pos1 = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                # pos2: smallest k in [l, r-1] with 2*leftSum(k) >= total  (right <= left)
                lo, hi = l, r - 1
                pos2 = r
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if 2 * (prefix[mid + 1] - prefix[l]) >= total:
                        pos2 = mid
                        hi = mid - 1
                    else:
                        lo = mid + 1

                best = 0
                if pos1 >= l:
                    best = max(best, bestL[l][pos1])
                if pos2 <= r - 1:
                    best = max(best, bestR[pos2 + 1][r])

                dp[l][r] = best
                cur = total + dp[l][r]
                bestL[l][r] = max(bestL[l][r - 1], cur)
                bestR[l][r] = max(bestR[l + 1][r], cur)

        return dp[0][n - 1]