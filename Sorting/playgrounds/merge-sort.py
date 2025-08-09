def merge_sort(arr):
    pass


# Test cases for mergesort
# Test case 1: Unsorted array
arr1 = [6, 3, 8, 5, 2, 7, 4, 1]
assert mergesort(arr1) == [1, 2, 3, 4, 5, 6, 7, 8], "Test Case 1 Failed"

# Test case 2: Already sorted array
arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
assert mergesort(arr2) == [1, 2, 3, 4, 5, 6, 7, 8], "Test Case 2 Failed"

# Test case 3: Reverse sorted array
arr3 = [8, 7, 6, 5, 4, 3, 2, 1]
assert mergesort(arr3) == [1, 2, 3, 4, 5, 6, 7, 8], "Test Case 3 Failed"

# Test case 4: Array with duplicate elements
arr4 = [4, 2, 7, 3, 2, 8, 1, 4]
assert mergesort(arr4) == [1, 2, 2, 3, 4, 4, 7, 8], "Test Case 4 Failed"

# Test case 5: Array with negative numbers
arr5 = [-3, -1, -7, 2, 0, 5, -2]
assert mergesort(arr5) == [-7, -3, -2, -1, 0, 2, 5], "Test Case 5 Failed"

# Test case 6: Single element array
arr6 = [42]
assert mergesort(arr6) == [42], "Test Case 6 Failed"

# Test case 7: Empty array
arr7 = []
assert mergesort(arr7) == [], "Test Case 7 Failed"

# Test case 8: Array with all identical elements
arr8 = [5, 5, 5, 5, 5]
assert mergesort(arr8) == [5, 5, 5, 5, 5], "Test Case 8 Failed"

print("All test cases passed!")