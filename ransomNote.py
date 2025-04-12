from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d = {}
        for char in magazine:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
                
        for char in ransomNote:
            if char not in d or d[char] <= 0:
                return False
            else:
                d[char] -= 1
        return True  