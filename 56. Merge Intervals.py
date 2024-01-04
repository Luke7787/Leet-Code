class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            last_value = res[-1][1]
            if start <= last_value:
                res[-1][1] = max(last_value, end)
            else:
                res.append([start, end])
        return res