def lyrics_to_frequencies(lyrics):
    myDic = {}
    for word in lyrics:
        if word in myDic:
            myDic[word] += 1
        else:
            myDic[word] = 1
    return myDic

def most_common_words(freq):
    values = freq.values()
    best = max(values)
    word = []
    for k in freq:
        if freq[k] == best:
            word.append(k)
    return (word,best)

