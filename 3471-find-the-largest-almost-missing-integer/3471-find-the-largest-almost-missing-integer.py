from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        appearances = {}
        for i in range(n - k + 1):
            subarray = nums[i:i+k]
            for num in set(subarray): 
                if num not in appearances:
                    appearances[num] = set()
                appearances[num].add(i)  
        candidates = [num for num, subs in appearances.items() if len(subs) == 1]
        
        return max(candidates) if candidates else -1
