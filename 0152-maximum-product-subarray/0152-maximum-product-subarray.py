from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_so_far = nums[0]
        max_so_far = nums[0]
        
        for num in nums[1:]:
            # Swap if num is negative
            if num < 0:
                min_so_far, max_so_far = max_so_far, min_so_far
            
            # Update max/min products ending at current index
            max_so_far = max(num, max_so_far * num)
            min_so_far = min(num, min_so_far * num)
            
            # Update global max
            max_prod = max(max_prod, max_so_far)
        
        return max_prod
