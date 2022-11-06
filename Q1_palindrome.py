def is_palindrome(s:str):
    """
    :type s: str
    :rtype: bool
    """
    phrase=""
    
    for j in range(len(s)):
        if s[j].isalnum():
            phrase=phrase+s[j].lower()
    
    for i in range(len(phrase)):
        if phrase[i]!=phrase[len(phrase)-1-i]:
            return False
    return True

#test cases
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("man"))
print(is_palindrome("getteg"))
print(is_palindrome("race a car"))
print(is_palindrome(" "))



