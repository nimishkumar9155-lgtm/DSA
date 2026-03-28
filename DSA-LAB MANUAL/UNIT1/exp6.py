def binarySearch(arr, key, low, high):
    
    # Base case: not found
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # Key found
    if arr[mid] == key:
        return mid
    
    # Search left half
    elif key < arr[mid]:
        return binarySearch(arr, key, low, mid - 1)
    
    # Search right half
    else:
        return binarySearch(arr, key, mid + 1, high)


# 🔹 Input
arr = list(map(int, input("Enter sorted elements separated by space: ").split()))
key = int(input("Enter key to search: "))

# Handle empty list case
if len(arr) == 0:
    print("Array is empty. Output: -1")
else:
    result = binarySearch(arr, key, 0, len(arr) - 1)
    print("Output (Index):", result)  