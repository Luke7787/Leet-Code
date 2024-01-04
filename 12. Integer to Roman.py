class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbol = [['I',1],['IV',4],['V',5],['IX',9],['X',10],['XL',40],['L',50],['XC',90],['C',100],['CD',400],['D',500],['CM',900],['M',1000]]
        count = 0
        res = ""
        for char, value in reversed(symbol):
            if num // value:
                count = num // value
                res += count * char
                num = num % value
        return res
