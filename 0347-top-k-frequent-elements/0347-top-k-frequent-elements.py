import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
