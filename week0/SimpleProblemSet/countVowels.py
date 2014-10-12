def count_vowels(str):
    str = str.lower()
    count = 0
    for i in str:
        if i in "aeiouy":
            count += 1
    return count

print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_vowels("grrrrgh!"))
