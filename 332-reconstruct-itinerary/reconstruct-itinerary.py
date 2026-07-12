from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                dfs(heapq.heappop(graph[airport]))
            itinerary.append(airport)

        dfs("JFK")
        return itinerary[::-1]