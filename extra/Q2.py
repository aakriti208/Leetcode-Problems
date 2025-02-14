def getStablePeriodsCount(revenues, k):
    #take two arguments : a list of integers to represent revenue data
    #k- represents maximum number of distinct values
    MOD = 10**9 + 7
    #Ensures that result does not overflow for large inputs
    n = len(revenues)
    
    # Sliding window variables
    # left boundary
    #final count of valid subarrays
    # dictionary to store frequency of elements in the current window

    left = 0
    count = 0
    freq_map = {}
    
    # expand the right end of the window
    for right in range(n):
        # Iterates through revenues using right as the right boundary
        # if element already exists, increase its frequency
        # if its a new element, initialize it with 1
        if revenues[right] in freq_map:
            freq_map[revenues[right]] += 1
        else:
            freq_map[revenues[right]] = 1
        
        # If distinct values exceed k, shrink the window
        # if needed, shrink the window from the left
        while len(freq_map) > k:
            #decrement the frequency of revenues[left]
            freq_map[revenues[left]] -= 1
            # if the count drops to 0, delete the frequency map
            # update the left pointer
            if freq_map[revenues[left]] == 0:
                del freq_map[revenues[left]]
            left += 1
        
        # Count the number of subarrays ending at right
        count += (right - left + 1)
        # this ensures that results stay within the limits of large numbers
        count %= MOD
    #return the total count of valid subarrays
    return count