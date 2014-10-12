def biggest_difference(arr):
    #doesn't work when arr is of type range(..)
    arr.sort()
    return arr[0] - arr[len(arr)-1]

print(biggest_difference([1,2,3,4,5]))

