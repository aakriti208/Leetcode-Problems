class Solution:
    def threeSum(self, nums):
        # We know that we have to return the result as a list of lists
        result = []
        # The first things we do is sort the input array
        nums.sort()
        # We wanna use each number in the input array as a first possible value
        # We go through each values in the input and the index
        for i, a in enumerate(nums):
            # We dont want to reuse the same value in the same position twice. If we have it continue to the next iteration
            if i>0 and a == nums[i-1]:
                # If i>0, his means it isnt the first value in the array and it's not the same as the previous value. We dpnt want to reuse the same value twice
                continue
            # Simlilar to two sum
            l, r = i + 1, len(nums) - 1
            # Initialize the left and right pointer.
            # We need to ensure that the left pointer should always be less than the right pointer 
            while l < r:
            # Find the sum adding the first number, value pointed by the left and the right pointer
                sum = a + nums[l] + nums[r]
            # Check if the sum is too small, we need to make the sum bigger; in that case the left pointer should be shifted by one position
            if sum < 0:
                l += 1
            # Or  sum is too great, then we need to decrease it and our right pointer should be decremented
            elif sum > 0:
                r -= 1
            else:
            # If the sum is equal to 0, we have to add it to our result.
                nums.append([a, nums[l], nums[r]])
            # Now we need to update our pointers. 
            # We dont have to update both pointers because we already have two conditions up there, so we only update left pointer
                l =+ 1
            # Since we dont want to have the same sum, we have to use a loop; we also dont want our lef tpointer to pass the right pointer
                while nums[l] == nums[l - 1] and l < r:
                    # Keep shifting the left pointer
                    l += 1
            return result