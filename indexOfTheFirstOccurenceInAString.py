class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        
        i = j = 0
        while i < len(haystack) and j < len(needle):
            start = i
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return start
            i = start + 1
            j = 0
        return -1
    

