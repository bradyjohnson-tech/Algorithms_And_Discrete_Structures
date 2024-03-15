def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle
        if arr[mid] == x:
            return mid

        # If element is smaller than mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element is in right half
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in array
        return -1


# Test the function
arr = [2, 3, 4, 10, 40, 50]
x = 50

result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")