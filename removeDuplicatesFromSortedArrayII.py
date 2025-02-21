# You are designing an inventory management system where products are stored in a sorted list 
# based on their SKU (Stock Keeping Unit). Due to system constraints, each unique product 
# should appear at most **twice** in the inventory record. Given a sorted list of product 
# SKUs, modify it **in-place** to ensure each SKU appears at most twice while maintaining 
# order. Return the new valid inventory size.  


def removeDuplicates(self, nums):
    l, r = 0, 0
    # I'm gonna have a left and right pointer both initialized at the beginning of the array
    
    # The right pointer will iterate through the entire length of the array
    while r < len(nums):
        # We want to count how long the current streak is
        count = 1
        # Right now whatever number we have at index r is going to be a new number. We wanna 
        # compare it to the next value in the sequence.
        # What if r+1 is out of range? We put a guard for that too
        while r + 1 < len(nums) and nums[r] == nums[r+1]:
            # We want to then increment the right pointer as well as count
            count += 1
            r += 1
            
        # Now we have the count of this streak. It could have any number of values. But we want
        # a maximum of 2 copies of this value. 
        minCount = min(2, count)
        # That is how many time we're gonna iterate through this 
        for i in range(minCount):
            # For every iteration, we're gonna take the value at the right index, and put it in 
            # the left position, we also increment the left pointer each time we do that 
            nums[l] = nums[r]
            l += 1
        # After processing the current number and its duplicates, the right pointer moves to the 
        # next unique number
        r += 1
        
    # l now represents the new valid length of nums, as all valid elements have been placed in the first l indices
    return l
            
        
 
# **Follow-up:** How would your approach scale if the inventory contained millions of SKUs?
# The time complexity is linear : Even though we have nested loops, the two pointers we have iterate through the 
# entire array at most once. --> O(2.n) --> which reduces to O(n). Since we traverse the array only once, the 
# solution remains efficient even for millions of SKUs. the input is already sorted, which avoids an extra O(n log n) cost
# We are not using any extra memory so the memory complexity is O(1)

# Handling Large-Scale Data
# If the SKU list is stored in-memory: The in-place modification ensures minimal memory usage, making it feasible for millions of SKUs.
# If the data is streamed (e.g., in batches from a database):
# Instead of storing the entire list, process one batch at a time and apply the same two-pointer approach per batch.
# This prevents excessive memory usage.

# Edge Cases to Consider
# What if the inventory contains only unique SKUs? → The function should return the original length.
# What if all SKUs appear more than twice? → The function should retain only two occurrences per SKU.
# What if we allow more than two occurrences? → The approach could be modified to accommodate a configurable limit.
   
    