class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(x):
            total = 0
            while x > 0:
                x, digit = divmod(x, 10)
                total += digit * digit
            return total
        
        slow, fast = n, get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1
