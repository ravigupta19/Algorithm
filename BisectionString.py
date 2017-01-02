def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0 or len(char) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr
    else:
        mid = int(len(aStr) / 2)
        if aStr[mid] == char:
            return True
        else:
            if char > aStr[mid]:
                return isIn(char, aStr[mid:])
            else:
                return isIn(char, aStr[0:mid])


print(isIn('p','abcdefghijklmnop'))