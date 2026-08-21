import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Precompute all subset LCMs
        lcms = []
        for mask in range(1, 1 << n):
            lcm = 1
            bits = 0
            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    lcm = lcm * coins[i] // math.gcd(lcm, coins[i])
            lcms.append((lcm, bits))
        
        def count(x):
            total = 0
            for lcm, bits in lcms:
                total += (x // lcm) * (1 if bits % 2 == 1 else -1)
            return total
        
        # Binary search
        lo, hi = 1, 10**18
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
