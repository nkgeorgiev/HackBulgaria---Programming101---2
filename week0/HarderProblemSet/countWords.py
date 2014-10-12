def count_words(arr):
    d = {}
    for word in arr:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1
    return d


def main():
    print(count_words(["apple", "banana", "apple", "pie"]))


if __name__ == '__main__':
    main()
