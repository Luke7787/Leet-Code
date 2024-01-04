class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h_idx = 0
        citations.sort()
        k = len(citations)
        for i in range(k):
            if citations[i] >= k - i:
                h_idx = k - i
                break
        return h_idx