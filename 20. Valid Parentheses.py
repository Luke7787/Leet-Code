class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        openToClose = {'}':'{', ']':'[', ')':'('}
        for char in s:
            if char in openToClose:
                if stack and stack[-1] == openToClose[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True