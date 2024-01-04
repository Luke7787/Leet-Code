class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s = collections.Counter(s)
        t = collections.Counter(t)
        for char, value in s.items():
            if char not in t or t[char] < value:
                return False
        return True