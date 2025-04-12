def longestConsecutive(self, nums):
    numSet = set(nums)
    longest = 0
    for n in numSet:
        if (n-1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest


# We use a set to keep track of each elements, the lookup time is O(1) for a set. It also eliminates any duplicates. 
# we initialize a variable longest to keep track of the longest sequence in the set
# we iterate through each of the numbers in our set....when we iterate through the nums itself, it results in maximum amount of time
# as there might be a lot of duplicates too which we wanna ignore.
# Then we check if the number is the first in the sequence, if it is we initialize a variable length and set it to 1, indicating that 
# the sequence has one element till now
# we then check if the number in the right (n + length) is in nums. if it is we increment the length by 1
# then we update the value of longest to the the max of length and longest till now
# finally we return the longest sequence

# TC: O(n)
# MC: O(n)