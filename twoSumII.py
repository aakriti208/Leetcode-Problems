class Solution:
    def twoSumII(self, nums, target):
        # First, we need to initialize the values of left and right pointer
        l, r = 0, len(nums) - 1
        # The left pointer should always be less than the right one, so that sum is not a negative value
        while l < r:
            # Then we calculate the sum of the numbers pointed by the left and the right pointer
            sum = nums[l] + nums[r]
            # Now, we need to know if the target value is less than or greater than the calculated sum
            # If it's less than the target, shift the left pointer by 1
            if sum < target:
                l +=1
            # Is the sum is greater than the target, shift the right pointer by 1
            elif sum > target:
                r -= 1
            # Else you just return the numbers 
            else:
                return [l+1, r+1]
        return []
