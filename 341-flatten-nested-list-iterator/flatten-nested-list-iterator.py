# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation.
# """
# class NestedInteger:
#     def isInteger(self) -> bool:
#     def getInteger(self) -> int:
#     def getList(self) -> [NestedInteger]:

class NestedIterator:
    def __init__(self, nestedList):
        self.arr = []

        def flatten(lst):
            for x in lst:
                if x.isInteger():
                    self.arr.append(x.getInteger())
                else:
                    flatten(x.getList())

        flatten(nestedList)
        self.idx = 0

    def next(self) -> int:
        val = self.arr[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx < len(self.arr)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())