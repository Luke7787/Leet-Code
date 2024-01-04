class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rm = collections.Counter(ransomNote)
        mg = collections.Counter(magazine)
        for char, value in rm.items():
            if char not in mg or mg[char] < value:
                return False
        return True
        