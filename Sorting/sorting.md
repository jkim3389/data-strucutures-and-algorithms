# Insertion Sort

## Overview
Insertion Sort is a simple and intuitive sorting algorithm that builds the final sorted array one element at a time. It is efficient for small datasets and partially sorted arrays.

## Algorithm
The algorithm works by iterating through the array and inserting each element into its correct position relative to the elements before it.

### Steps:
1. Start from the second element (index 1) in the array.
2. Compare the current element with the elements before it.
3. Shift all larger elements one position to the right.
4. Insert the current element into its correct position.
5. Repeat until the entire array is sorted.


### How it works?
![insertion](./images/insertion-sort/insertion-sort.png)
![insertion-animation](./images/insertion-sort/Insertion-sort-animated.gif)

## Time Complexity
- **Best Case**: \(O(n)\) (when the array is already sorted)
- **Worst Case**: \(O(n^2)\) (when the array is sorted in reverse order)
- **Average Case**: \(O(n^2)\)

## Space Complexity
- **Auxiliary Space**: \(O(1)\) (in-place sorting)

## Advantages
- Simple to implement.
- Efficient for small or nearly sorted datasets.

## Disadvantages
- Inefficient for large datasets due to \(O(n^2)\) time complexity.


# Merge Sort

## Overview
Merge Sort is a divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and then merges the sorted halves back together. It is efficient and guarantees \(O(n \log n)\) time complexity for all cases.

## Algorithm
1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves into a single sorted array.

### How it works?
![merge-sort-mechanism](./images/merge-sort/merge-sort-1.png)
![merge-sort-mechanism](./images/merge-sort/merge-sort-2.png)
![merge-sort-animation](./images/merge-sort/merge-sort-animation.gif)

## Time Complexity
- **Best Case**: \(O(n \log n)\)
- **Worst Case**: \(O(n \log n)\)
- **Average Case**: \(O(n \log n)\)

## Space Complexity
- **Auxiliary Space**: \(O(n)\) (due to temporary arrays used during merging)

## Advantages
- Guarantees \(O(n \log n)\) time complexity for all cases.
- Stable sorting algorithm (preserves the order of equal elements).

## Disadvantages
- Requires \(O(n)\) additional space for merging.
- Not an in-place sorting algorithm.

