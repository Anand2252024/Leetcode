class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337

        def mod_pow(x, n):
            # fast exponentiation
            res = 1
            x %= MOD
            while n:
                if n & 1:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                n >>= 1
            return res

        def helper(b):
            if not b:
                return 1
            last = b.pop()
            part1 = mod_pow(helper(b), 10)
            part2 = mod_pow(a, last)
            return (part1 * part2) % MOD

        return helper(b)
