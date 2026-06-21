class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_all = 0
        max_i = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = (j-i)* min(height[i], height[j])
                max_i = max(area, max_i)
            # max_all = max(max_all, max_i)
        return max_i