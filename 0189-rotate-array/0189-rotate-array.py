class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # handle cases where k >= n

        # Helper function to reverse a portion of the list
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Reverse the entire array
        reverse(0, n - 1)
        # Reverse the first k elements
        reverse(0, k - 1)
        # Reverse the remaining elements
        reverse(k, n - 1)


# Example usage
if __name__ == "__main__":
    sol = Solution()
    arr1 = [1,2,3,4,5,6,7]
    sol.rotate(arr1, 3)
    print(arr1)  # Output: [5,6,7,1,2,3,4]

    arr2 = [-1,-100,3,99]
    sol.rotate(arr2, 2)
    print(arr2)  # Output: [3,99,-1,-100]
