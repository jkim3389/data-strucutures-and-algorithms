
def insertionsort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j+1] = arr[j]
      j-=1
    arr[j+1] = key
  return arr


print(insertionsort([6, 5, 3, 1, 8, 7, 2, 4]))
assert insertionsort([6, 5, 3, 1, 8, 7, 2, 4]) == [1, 2, 3, 4, 5, 6, 7, 8], "Test Case 1 Failed"
assert insertionsort([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8], "Test Case 2 Failed"
assert insertionsort([8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8], "Test Case 3 Failed"
assert insertionsort([4, 2, 7, 3, 2, 8, 1, 4]) == [1, 2, 2, 3, 4, 4, 7, 8], "Test Case 4 Failed"
assert insertionsort([-3, -1, -7, 2, 0, 5, -2]) == [-7, -3, -2, -1, 0, 2, 5], "Test Case 5 Failed"
assert insertionsort([42]) == [42], "Test Case 6 Failed"
assert insertionsort([]) == [], "Test Case 7 Failed"
assert insertionsort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "Test Case 8 Failed"

print("All test cases passed!")




