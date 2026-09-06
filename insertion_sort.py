def insertion_sort_decreasing(arr):
    # Start from the second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move smaller elements to the right
        # to arrange the array in decreasing order
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Test the insertion sort
numbers = [5, 2, 4, 6, 1, 3]

print("Original array:", numbers)
insertion_sort_decreasing(numbers)
print("Decreasing order:", numbers)