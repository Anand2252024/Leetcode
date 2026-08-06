class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def digit_product(x):
            prod = 1
            for ch in str(x):
                prod *= int(ch)
            return prod
        
        while True:
            if digit_product(n) % t == 0:
                return n
            n += 1
