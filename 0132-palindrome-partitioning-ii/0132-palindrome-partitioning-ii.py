class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)

        # dp[i] = minimum cuts needed for s[0...i]
        dp = [0] * n

        # palindrome table
        palindrome = [[False] * n for _ in range(n)]

        for end in range(n):

            dp[end] = end

            for start in range(end + 1):

                if s[start] == s[end] and (end - start <= 2 or palindrome[start + 1][end - 1]):

                    palindrome[start][end] = True

                    if start == 0:
                        dp[end] = 0
                    else:
                        dp[end] = min(dp[end], dp[start - 1] + 1)

        return dp[-1]