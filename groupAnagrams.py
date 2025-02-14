# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        return list(res.values())       