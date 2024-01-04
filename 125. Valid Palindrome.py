class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        temp = ""
        for char in s:
            if 'a' <= char <= 'z' or '0' <= char <= '9':
                temp += char
        s = "".join(reversed(temp))
        return s == temp