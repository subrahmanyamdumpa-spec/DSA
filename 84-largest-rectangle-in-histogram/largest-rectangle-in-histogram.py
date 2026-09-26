class Solution:
    def largestRectangleArea(self, heights):
        stack = []          # stores indices
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            current = 0 if i == n else heights[i]

            while stack and heights[stack[-1]] > current:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area