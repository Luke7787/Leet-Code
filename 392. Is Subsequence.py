class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        i = 0
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                count += 1
                i += 1
        return count == len(s)