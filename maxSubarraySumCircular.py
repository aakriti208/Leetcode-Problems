def maxSubarraySumCircular(self, nums):
    # Initialize the global max and min to an arbitrary valu. We take the first value in the array
    # Initialise the current max and min to 0 and then the total to 0
    
    globMax, globMin = nums[0], nums[0]
    currMax, currMin = 0, 0
    total = 0
    
    # Now iterate through each value in the input array
    for n in nums:
        # The first thing we do is update our current maximum value. So we take the maximum of the currentMax and add n, or the value n itself
        # Same for current min
        currMax = max(currMax + n, n) 
        currMin = min(currMin + n, n)
        
        # The global max will also be the maximum of itself and the current max value
        globMax = max(globMax, currMax)
        globMin = min(globMin, currMin)
        
        total += n   # for the total sum, we take the sum of all the values in the array
        totalMax = total - globMin   # The totalMax will be the total subtracted by the minimum value present in the array, this gives us the total of first and last value in the array too
        
    return max(globMax, totalMax) if globMax > 0 else globMax
    
    # We handle the edge case, where all the elements are negative. In that case, the max sum will be the global Maximum value, which is the closest to a positive number
    # suppose we have total = -5 and globMin = -2. totalMax would be -3 which is not the right answer
    
    