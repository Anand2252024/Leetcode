class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        ans = 10
        unique = 9
        available = 9

        while n > 1 and available > 0:
            unique *= available
            ans += unique
            available -= 1
            n -= 1

        return ans