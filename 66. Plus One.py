class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        temp = ""
        for char in digits:
            temp += str(char)

        result = str(int(temp)+1)
        for char in result:
            res.append(int(char))
        return res