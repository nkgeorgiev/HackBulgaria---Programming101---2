def unique_words_count(arr):
    s = set()
    for word in arr:
        s.add(word)
    return len(s)
