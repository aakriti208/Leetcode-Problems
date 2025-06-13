class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        if left == -1: return [-1, -1]
        right = self.binarySearch(nums, target, False)
        return [left, right]
        
        
    def binarySearch(self, nums, target, leftBias):
        ans = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                ans = mid
                if leftBias:
                    r = mid - 1
                else:
                    l = mid + 1
        return ans
            