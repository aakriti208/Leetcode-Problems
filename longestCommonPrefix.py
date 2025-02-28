def longestCommonPrefix(strs):
    # first lets handle the case where the string is empty, in that case, we just resturn ""
    if len(strs) == 0:
        return ""
    
    # Then lets take the first word of the array, called base
    # We compare this with every other word in the array to make sure that the prefix matches, it's okay to pick whatever word we want though
    base = strs[0]
    # we then enter a loop that will traverse through each letter of the base word using the counter variable 'i'
    # we then enter an inner loop, and this loop uses a variable called word to traverse through all the different words in the array. We'll start from index one and go to the end
    # we start from 1 because we've already used the first word as the base, and we dont compare it with itself 
    for i in range(len(base)):
        for word in strs[1:]:
            # The we'll check for two things : if either of them are true, we return early
            # First, we check if index is out of bound, then we compare the character at index i of the base word to the index of the current word we're on
            # If the character at both word does not match, we return the letters upto that point. 
            # this returns character from index 0 to index i, excluding i
            if i == len(base) or base[i] != word[i]:
                return base[0:i]
            # Suppose we have ["action", "actor", "a"]
            # if we reach the last line, we know that it is the longest word on the array, and we can directly return it
            
    return base
            
    

        
    