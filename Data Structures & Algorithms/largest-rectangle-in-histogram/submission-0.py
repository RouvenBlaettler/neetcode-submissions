class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] >= h:
                index = stack[-1][0]
                area = stack[-1][1] * (i - index)
                if area > maxArea:
                    maxArea = area
                stack.pop()
            stack.append([index, h])
        for s in stack:
            area = s[1] * (len(heights) - s[0])
            if area > maxArea:
                maxArea = area
        return maxArea



