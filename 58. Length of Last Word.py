class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        start = False
        k = len(s)-1
        while k >= 0:
            if s[k] == " " and not start:
                k -= 1
            elif s[k] != " ":
                count += 1
                k -= 1
                start = True
            else:
                return count
        return count