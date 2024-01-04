class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total = 0
        left, right = 0, len(height)-1
        while left <= right:
            width = right - left
            tall = min(height[left], height[right])
            area = width * tall
            if area > total:
                total = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return total
