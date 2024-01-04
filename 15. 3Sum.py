class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for index, value in enumerate(nums):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            left, right = index + 1, len(nums)-1
            while left < right:
                threeSum = value + nums[left] + nums[right]
                if threeSum == 0:
                    res.append([value, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1
        return res