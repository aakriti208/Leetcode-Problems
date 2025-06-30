def priority(self, c):
    if c == '^':
        return 1
    elif c in ('/', '*'):
        return 2
    elif c in ('+', '-'):
        return 3
    else:
        return -1
    
def infixToPrefix(self, str):
    # reverse the infix
    # infix to postfix
    # reverse the answer
    
    str = reversed(str)
    st = []
    res = ''
    for c in str:
        if c.isalnum():
            res += c
        elif c == '(':
            res += c 
    