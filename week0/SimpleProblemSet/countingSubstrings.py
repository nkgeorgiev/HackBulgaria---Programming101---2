def count_substrings(haystack, needle):
    count = 0
    index = 0
    while index < len(haystack):
        index = haystack.find(needle, index)
        if index == -1:
            break
        else:
            count += 1
            index += len(needle)
    return count

print(count_substrings("babababa", "baba"))
print(count_substrings("Python is an awesome language to program in!", "o"))
print(count_substrings("We have nothing in common!", "really?"))
