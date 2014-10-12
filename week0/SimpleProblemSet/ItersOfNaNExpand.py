def iterations_of_nan_expand(expanded):
    if expanded == "":
        return 0
    size = len(expanded)
    text = "Not a NaN"
    count = 1
    while len(text) < size:
        text = text.replace("NaN", "Not a NaN")
        count += 1
    if text == expanded:
        return count
    return False


print(iterations_of_nan_expand(""))
print(iterations_of_nan_expand("Not a NaN"))
print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
print(iterations_of_nan_expand("Show these people!"))
