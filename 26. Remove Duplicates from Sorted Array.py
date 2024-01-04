class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        k = len(nums)
        while i < k-1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
                k -= 1
            else:
                i += 1
        return k