class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        i = 0
        k = len(nums)
        while i < k-1:
            if nums[i] == nums[i+1]:
                count += 1
                if count > 2:
                    nums.remove(nums[i+1])
                    k -= 1
                else:
                    i += 1
            else:
                count = 1
                i += 1
        return k