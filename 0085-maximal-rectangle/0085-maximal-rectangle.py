from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        def largestRectangleArea(heights: List[int]) -> int:
            stack = []
            area = 0
            for i, h in enumerate(heights + [0]):  # sentinel
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    area = max(area, height * width)
                stack.append(i)
            return area
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, largestRectangleArea(heights))
        
        return max_area
