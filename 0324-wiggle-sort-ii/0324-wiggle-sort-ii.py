class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        half = (n + 1) // 2

        # smaller half reversed
        left = nums[:half][::-1]
        # larger half reversed
        right = nums[half:][::-1]

        nums[::2] = left
        nums[1::2] = right
