class Solution:
    def maxSubArray(self, nums):
        # Initialize a variable maxSub to the first value in the array.
        maxSub = nums[0]
        # We need to constantly compute the current sum, so initialize it to 0.
        currentSum = 0
        # Now, we go through each number in the array
        for n in nums:
            # We check to see if we have a negative prefix, so that we can remove it from the currentSum
            if currentSum < 0:
                # In that case, reset the currentSum to 0
                currentSum = 0
            # After that, we add our current number to currentSum. This makes sure we're always computing the max
            currentSum += n
            # Then we find the maximum number, which is the max of the currentSum and the maxSub itself
            maxSub = max(maxSub, currentSum)
        return maxSub
    
    # Space complexity : O(1)
    # Time complexity : O(n)