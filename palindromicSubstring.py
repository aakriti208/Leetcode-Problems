class Solution:
    def countSubstrings(self, s):
        res = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
    

class Solution:
    def countSubstring(self, s):
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i+1 )
        return res
    
    def countPali(self, s, l, r):
        res = 0
        while l >=0 and r <= len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res