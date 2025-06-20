class Solution:
    def countSubarray(self, nums, max_allowed_sum):
        count = 1, totalSum = 0
        for num in nums:
            if totalSum + num <= max_allowed_sum:
                totalSum += num
            else:
                count += 1
                totalSum = num
        return count
    
    def findMinimum(self, nums, k):
        n = len(nums)
        if n < k:
            return -1
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2
            required_subarray = self.countSubarray(nums, mid)
            if required_subarray > k:
                low = mid + 1
            else:
                high = mid - 1
        return low
                