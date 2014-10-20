def count_words(arr):
    d = {}
    for word in arr:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1
    return d
