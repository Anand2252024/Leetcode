from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            # If frequency of current element exceeds k, shrink window
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len
