class Solution:
    def isValid(self, s: str):
        #Initialize an empty stack. We use a stack to keep track of the opening brackets
        stack = []
        # Create a dictionary to check if the closing bracket matches its opening bracket
        closeToOpen = {')':'(','}':'{', ']':'['} 
        # Iterate through each character in the input string
        for c in s:
            # if c is a closing bracket we need to check if it correctly matches an opening bracket
            if c in closeToOpen:
            # if stack is not empty and the top of stack matched the closing bracket, we remove top from the stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    #if there is no match, we return False
                    return False
            else:
                # if the character is an opening bracket, we simply push it to the stack
                stack.append(c)
        # we check if the stack is empty at the end
        return True if not stack else False



