def nan_expand(times):
    if times <= 0:
        return ""
    text = "Not a NaN"
    for i in range(times - 1):
        text = text.replace("NaN", "Not a NaN")
    return text


def main():
    print(nan_expand(1))


if __name__ == '__main__':
    main()
