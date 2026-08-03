class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # prev1 = max profit up to previous house
        # prev2 = max profit up to house before previous
        prev1, prev2 = 0, 0

        for num in nums:
            # Either rob this house (num + prev2) or skip it (prev1)
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp

        return prev1


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1,2,3,1]))     # Output: 4
    print(sol.rob([2,7,9,3,1]))   # Output: 12
