def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left_half = arr[mid:]
        right_half = arr[:mid]

        return merge_helper(merge_sort(left_half), merge_sort(right_half))


def merge_helper(left, right):
    sorted_array = [None] * (len(left) + len(right))
    i = k = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array[k] = left[i]
            i += 1
        else:
            sorted_array[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        sorted_array[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        sorted_array[k] = right[j]
        k += 1
        j += 1

    return sorted_array


print(merge_sort([10, 2, 1, 5, 22]))
