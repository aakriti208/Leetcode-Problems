class Solution(object):
    def lengthOfLastWord(self, s): 
        # For this solution, we directly start from the last position of the array
        i = len(s) - 1
        # We also keep a variable count that counts the length of the word
        count = 0
        # We check to see if the word has reached to a point where there is empty space
        while s[i] == " ":
            # if there is, we decrement the pointer by one
            i -= 1
        while i >= 0 and s[i] != " ":
            # We then keep on going until we find another blank space, and in the meantime, we also increment our count variable
            count += 1
            # We update our pointer everytime we do that
            i -= 1
        # and the result is the count of the length of the last string
        return count