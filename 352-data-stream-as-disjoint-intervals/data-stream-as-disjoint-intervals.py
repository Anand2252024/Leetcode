class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        if not self.nums:
            return []

        arr = sorted(self.nums)
        intervals = []

        start = end = arr[0]

        for num in arr[1:]:
            if num == end + 1:
                end = num
            else:
                intervals.append([start, end])
                start = end = num

        intervals.append([start, end])
        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()