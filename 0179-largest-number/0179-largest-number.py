import functools

class Solution:
    def largestNumber(self, nums):
        # Convert integers to strings
        nums = map(str, nums)

        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        # Sort using comparator
        nums.sort(cmp=compare)  # Python 2 allows cmp directly

        # Concatenate sorted strings
        result = ''.join(nums)

        # Handle case like [0,0] → "0"
        return '0' if result[0] == '0' else result


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestNumber([3, 30, 34, 5, 9]))  # "9534330"
    print(sol.largestNumber([0, 0]))             # "0"
