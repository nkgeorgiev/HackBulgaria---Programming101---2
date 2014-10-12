def count_consonants(str):
    count = 0
    str = str.lower()
    for i in str:
        if i in "bcdfghjklmnpqrstvwxz":
            count += 1
    return count

print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
