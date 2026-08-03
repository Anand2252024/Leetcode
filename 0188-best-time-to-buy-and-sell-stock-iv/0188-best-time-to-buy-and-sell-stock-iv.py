class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # If k >= n/2, it's equivalent to unlimited transactions
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit

        # DP approach
        # dp[i][j] = max profit up to day j with at most i transactions
        dp = [[0] * (n + 1) for _ in range(k + 1)]

        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i][j-1], prices[j-1] + max_diff)
                max_diff = max(max_diff, dp[i-1][j-1] - prices[j-1])

        return dp[k][n]


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(2, [2,4,1]))          # Output: 2
    print(sol.maxProfit(2, [3,2,6,5,0,3]))    # Output: 7
