def all_sevens(arr):
    for i in arr:
        if i != 7:
            return False
    return True


def sevens_in_a_row(arr, n):
    for i in range(len(arr)):
        if arr[i] == 7 and i + n < len(arr) and all_sevens(arr[i:i + n]):
            return True

    return False

print(sevens_in_a_row([1, 7, 1, 7, 7], 4))
print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
print(sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))
print(sevens_in_a_row([7, 2, 1, 6, 2], 2))
