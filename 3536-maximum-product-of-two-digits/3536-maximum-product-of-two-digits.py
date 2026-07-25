class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        # Find the two largest digits
        first = max(digits)
        digits.remove(first)
        second = max(digits)
        return first * second
