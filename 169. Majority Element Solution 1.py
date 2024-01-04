class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        k = len(nums)
        count = 0
        while i < k-1:
            if nums[i] == nums[i+1]:
                count += 1
                i += 1
            elif count >= (k/2):
                return nums[i]
            else:
                count = 0
                i += 1
        return nums[i]