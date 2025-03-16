class Solution:
    def maxProduct(self, nums):
        # First we set a variable result to the maximum value of nums
        res = max(nums)
        # For maintaining the current minimum and the current maximum, we initialize them to 1
        curMin, curMax = 1, 1
        # We now iterate through the input array
        for n in nums:
            # If we get zero, we reset the min and max value and continue through the loop, this step is not really necessary
            if n == 0:
                curMax, curMin = 1, 1
                continue
            # Now we calculate the current max. It could be the maximum of the current input number multiplied by the current maa value, it could be the current number multiplied by the current min value or it could be the number itself.
            temp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            # We do the same for the current minimum value, finding the minimum among 3 values, but for this we use the initial current max value before it has been upated. So we need to have a temporary variable for the initial current max
            curMin = min(temp, n * curMin, n)
            # Now, we can update our result after each iteration. We can take the maximum of result itself, current maximum 
            # Then we can return the result
            res = max(res, curMax)

        return res
    
    # Time complexity : O(n)
    # Memory complexity : O(1)


















