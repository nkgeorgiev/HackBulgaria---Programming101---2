def is_decreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i+1]:
            return False
    return True

print(is_decreasing([5, 4, 3, 2, 1]))
print(is_decreasing([1, 1, 1, 1]))
