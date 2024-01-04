class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(words) != len(pattern):
            return False
        mapchar, mapword = {}, {}
        for i in range(len(pattern)):
            char, word = pattern[i], words[i]
            if (char in mapchar and mapchar[char] != word) or (word in mapword and mapword[word] != char):
                return False
            mapchar[char] = word
            mapword[word] = char
        return True