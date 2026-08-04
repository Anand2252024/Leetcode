import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # Step 1: Create events
        events = []
        for l, r, h in buildings:
            events.append((l, -h))  # start event
            events.append((r, h))   # end event

        # Step 2: Sort events
        events.sort(key=lambda x: (x[0], x[1]))

        # Step 3: Sweep line
        result = []
        heap = [0]  # max heap (store negative heights)
        active = {0:1}  # count of heights
        prev_max = 0

        for x, h in events:
            if h < 0:  # start
                heapq.heappush(heap, h)
                active[-h] = active.get(-h, 0) + 1
            else:      # end
                active[h] -= 1
                if active[h] == 0:
                    del active[h]

            # Clean heap top
            while heap and -heap[0] not in active:
                heapq.heappop(heap)

            curr_max = -heap[0]
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max

        return result
