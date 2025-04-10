class Solution(object):
    def majorityElement(self, nums):
        count = 0
        majorityElement = 0
        for n in nums:
            if count == 0:
                majorityElement = n

            if n == majorityElement:
                count += 1
            else:
                count -= 1
        return majorityElement