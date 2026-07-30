class Solution:
    def minimumPushes(self, word: str) -> int:
        m = len(word)  
        pushes = 0
        cost = 1
        while m > 0:
            take = min(8, m)
            pushes += take * cost
            m -= take
            cost += 1
        return pushes
