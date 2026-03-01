class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    
    
    # Alternative
    
    def lengthOfLongestSubstring(self, s):
        charMap = {}
        result = 0
        l = 0
        for r in range(len(s)):
            if s[r] in charMap and charMap[s[r]] >= l:
                l = charMap[s[r]] + 1
            charMap[s[r]] = r
            result = max(result, r-l+1)
        return result
            