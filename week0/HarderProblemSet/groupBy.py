def groupby(func, seq):
    d = {}
    for value in seq:
        key = func(value)
        if key in d.keys():
            d[key].append(value)
        else:
            d[key] = [value]
    return d
