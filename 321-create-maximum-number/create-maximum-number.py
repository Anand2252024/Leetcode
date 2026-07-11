class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int):

        def maxSubsequence(nums, k):
            stack = []
            drop = len(nums) - k

            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:k]

        def merge(a, b):
            res = []
            while a or b:
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res

        ans = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):
            part1 = maxSubsequence(nums1, i)
            part2 = maxSubsequence(nums2, k - i)
            candidate = merge(part1[:], part2[:])

            if candidate > ans:
                ans = candidate

        return ans