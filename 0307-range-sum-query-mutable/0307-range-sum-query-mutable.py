class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums = nums[:]  # keep original values
        self.bit = [0] * (self.n + 1)  # Fenwick tree array

        # build Fenwick tree
        for i, val in enumerate(nums):
            self._add(i + 1, val)

    def _add(self, i, delta):
        """Add delta to index i in Fenwick tree"""
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def _prefix_sum(self, i):
        """Sum from start to index i (1-based)"""
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self._prefix_sum(right + 1) - self._prefix_sum(left)
