class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        k = len(nums)-1
        count = 0
        while right < k:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, nums[i] + i)
            count += 1
            left = right
            right = farthest
        return count