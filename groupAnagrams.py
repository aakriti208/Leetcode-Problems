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
    
    
    # res.items gives: [[[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],["eat","tea","ate"]],[[1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],["tan","nat"]],[[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],["bat"]]]
    # this means that each of the key is associated with all anagrams since their index position will be the same.
    # but we return only values