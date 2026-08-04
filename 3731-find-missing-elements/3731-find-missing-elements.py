class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Step 1: Find min and max
        start, end = min(nums), max(nums)
        
        # Step 2: Construct full range
        full_range = set(range(start, end + 1))
        
        # Step 3: Convert nums to set
        nums_set = set(nums)

        missing = sorted(list(full_range - nums_set))
        
        return missing
