def is_valid_parentheses(s: str):
    """
    :type s: str
    :rtype: bool
    """

    #initially check if len of string is odd
    if len(s) % 2 > 0:
        return False
    
    #make use of stacks
    start_stack=[]
    
    #first create dict with corresponding parentheses
    d={'(':')','{':'}','[':']'}
    
    for element in s:
        if element in d:
            start_stack.append(element)
        elif len(start_stack)>0:            
            if d[start_stack[-1]]==element:
                start_stack.pop()
            else:
                return False
        else:
            return False
    
    if len(start_stack)>0:
        return False
    else:
        return True

#test cases
print(is_valid_parentheses(''))
print(is_valid_parentheses('()[][((()))]'))
print(is_valid_parentheses('(]]'))
print(is_valid_parentheses('(]'))
print(is_valid_parentheses('()'))
print(is_valid_parentheses("()[]{}"))




















