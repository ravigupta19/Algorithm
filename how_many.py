def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = ''
    biggest = 0
    for key in aDict:
        length = len(aDict[key])
        if length == 0:
            continue
        elif length >= biggest:
            biggest = length
            result = key
    if biggest > 0:
        return result

print(how_many({'B': [], 'u': []}))