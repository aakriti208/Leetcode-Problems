class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        hashMap = {}
        for i in range(len(pattern)):
            charP, wordsS = pattern[i], words[i]
            if charP not in hashMap:
                if wordsS in hashMap.values():
                    return False
                hashMap[charP] = wordsS
            else:
                if hashMap[charP] != wordsS:
                    return False
        return True
