class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        start, end = 0, 0
        res = []
        nums.append(nums[-1])
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                end += 1
            else:
                if start < end:
                    res.append(str(nums[start]) + "->" + str(nums[end]))
                else:
                    res.append(str(nums[start]))
                start = end = i + 1
        return res