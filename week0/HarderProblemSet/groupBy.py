def groupby(func, seq):
    d = {}
    for value in seq:
        key = func(value)
        if key in d.keys():
            d[key].append(value)
        else:
            d[key] = [value]
    return d

def main():
    print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))


if __name__ == '__main__':
    main()