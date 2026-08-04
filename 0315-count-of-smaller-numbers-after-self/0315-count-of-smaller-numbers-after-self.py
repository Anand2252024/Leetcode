class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Coordinate compression
        sorted_unique = sorted(set(nums))
        ranks = {v: i+1 for i, v in enumerate(sorted_unique)}  # 1-based index

        # Fenwick Tree
        def update(i):
            while i <= len(sorted_unique):
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        bit = [0] * (len(sorted_unique) + 1)
        res = []
        # Traverse from right to left
        for num in reversed(nums):
            rank = ranks[num]
            res.append(query(rank - 1))  # count of smaller elements
            update(rank)
        return res[::-1]
