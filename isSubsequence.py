def isSubsequence(self, s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    return True if i == len(s) else False


# initialize the left and write pointer to the first position of s and t strings
# we're gonna keep running the loop while both the strings are in bounce
# we have two conditions, one is that the characters are equal. s at position i is equal to t at position j
# in that condition, we increment the i and j pointer
# in another case, we only increment the j pointer since we have to check if the subquence is there in the main string
# once we are done with this loop, how do we know if s was a subsequence of t or not
# if i has reached the end of the string s, we can say that for every character in s we've found a matching character in t
# then we're returning True, if thats not the case we're returning False

# TC : O(n), this is a linear time algorithm
# SC : O(1)