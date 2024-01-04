class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        prev = 0
        for char in s:
            current = hashmap[char]
            if current > prev:
                total += current - (2*prev)
            else:
                total += current
            prev = current
        return total