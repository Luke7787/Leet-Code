class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        for index, element in enumerate(nums):
            if element in hashmap and index - hashmap[element] <= k:
                return True
            hashmap[element] = index