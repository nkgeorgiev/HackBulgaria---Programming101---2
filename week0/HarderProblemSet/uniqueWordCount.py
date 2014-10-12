def unique_words_count(arr):
    s = set()
    for word in arr:
        s.add(word)
    return len(s)


def main():
    print(unique_words_count(["HELLO!"] * 10))
    print(unique_words_count(["apple", "banana", "apple", "pie"]))


if __name__ == '__main__':
    main()
