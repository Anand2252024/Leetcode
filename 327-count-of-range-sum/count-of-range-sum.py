from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def merge_sort(left, right):
            if right - left <= 1:
                return 0

            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid, right)

            j = k = mid
            temp = []
            r = mid

            for l in range(left, mid):
                while k < right and prefix[k] - prefix[l] < lower:
                    k += 1
                while j < right and prefix[j] - prefix[l] <= upper:
                    j += 1
                count += j - k

            p1, p2 = left, mid
            while p1 < mid and p2 < right:
                if prefix[p1] <= prefix[p2]:
                    temp.append(prefix[p1])
                    p1 += 1
                else:
                    temp.append(prefix[p2])
                    p2 += 1

            temp.extend(prefix[p1:mid])
            temp.extend(prefix[p2:right])

            prefix[left:right] = temp

            return count

        return merge_sort(0, len(prefix))