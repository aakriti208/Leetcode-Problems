# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                count[index] += 1
            key = tuple(count)
            res[key].append(s)
        return list(res.values())       