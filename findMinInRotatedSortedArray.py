class Solution:
    def findMin(self, nums):
        # First we maintain a result and set it to a default value. I'm gonna choose the leftmost value.
        res = nums[0]
        # Then we initialize the left and the right pointer
        l, r = 0, len(nums) - 1
        # Keep running a binary search until the condition is in a vlaid position
        while l <= r:
            # Check if the subarray is sorted
            if nums[l] < nums[r]:
                # In that case, we update the result which is the minimum of itself and the leftmost value of the sorted portion, then break out of the while loop
                res = min(res, nums[l])
                break
            # If the subarray is not sorted, we do our binary search portion to compute the mid pointer
            m = (l + r) // 2
            # We now determine if we're gonna search the left or the right portion of the array. We wanna know of the mid value is part of the left sorted array
            # For that, we check if the value at mid index is greater than or equal to the value at the left indexes
            if nums[m] >= nums[l]:
            # In that case, search the right sorted portion and set the left pointer to mid + 1
                l = m + 1
            else:
                r = m - 1
        return res