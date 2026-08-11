class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                    bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        # Area of first rectangle
        areaA = (ax2 - ax1) * (ay2 - ay1)
        # Area of second rectangle
        areaB = (bx2 - bx1) * (by2 - by1)
        
        # Overlap dimensions
        overlapX = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlapY = max(0, min(ay2, by2) - max(ay1, by1))
        
        # Overlap area
        overlap = overlapX * overlapY
        
        return areaA + areaB - overlap
