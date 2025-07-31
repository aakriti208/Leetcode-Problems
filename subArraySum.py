class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0:1}
        prefixSum = 0
        count = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            remove = prefixSum - k
            count += hashMap.get(remove, 0)
            hashMap[prefixSum] = hashMap.get(prefixSum,0) + 1
        return count
        