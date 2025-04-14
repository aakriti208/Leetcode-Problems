class Solution:
    def reverseWords(self, s):
        s = s.strip()
        words = s.split()
        reversedWords = words[::-1]
        return ' '.join(reversedWords)