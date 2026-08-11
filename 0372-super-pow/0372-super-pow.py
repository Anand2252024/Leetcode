class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        
        # Fast modular exponentiation
        def mod_pow(x, n):
            result = 1
            x %= MOD
            while n > 0:
                if n % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                n //= 2
            return result
        
        def helper(b_digits):
            if not b_digits:
                return 1
            last = b_digits.pop()
            # Compute recursively: a^last * (a^(remaining))^10
            part1 = mod_pow(a, last)
            part2 = mod_pow(helper(b_digits), 10)
            return (part1 * part2) % MOD
        
        return helper(b[:])
