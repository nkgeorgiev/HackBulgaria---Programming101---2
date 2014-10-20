def reduce_file_path(path):
    l = path.split('/')
    res = []

    for item in l:
        if item == '..':
            res.pop()
        elif not item == '' and not item == '.':
            res.append(item)
    if len(res) == 0:
        return "/"
    ans = ""
    for item in res:
        ans += "/" + item
    return ans


def main():
    print(reduce_file_path("/srv/www/htdocs/wtf"))


if __name__ == '__main__':
    main()
