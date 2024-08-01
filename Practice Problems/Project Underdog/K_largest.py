"""
Mini interview question: `k` largest elements

Goal: solve this problem in < 30 minutes.

Write a function that takes as input two arguments:

1. An array of numbers
2. An integer `k`

and returns the `k` largest values from that array. The order of the elements in the returned array doesn’t matter.

Example

- Input array: `[5, 16, 7, 9, -1, 4, 3, 11, 2]`
- `k`: 3
- Result: `[16, 9, 11]`
"""

import heapq

def k_largest_elements(arr, k):
    # Create a min-heap with heapq
    min_heap = []
    
    # Iterate over each element in the array
    for num in arr:
        if len(min_heap) < k:
            # If the heap has fewer than k elements, push the current number onto the heap
            heapq.heappush(min_heap, num)
        else:
            # If the heap has k elements, check if the current number is larger than the smallest in the heap
            if num > min_heap[0]:
                # Replace the smallest element with the current number and maintain the heap property
                heapq.heapreplace(min_heap, num)
    
    # At the end, the heap contains the k largest elements
    return min_heap

# Example usage:
arr = [5, 16, 7, 9, -1, 4, 3, 11, 2]
k = 3
print(k_largest_elements(arr, k))  # Output: [9, 16, 11]

"""
root is element 0
index 1 is child, index 2 is child

array is more efficient than linked list

top k - n log k
sort n log n

scheduling - priority tasks

implement a heap from scratch

finding shortest paths in an algo- each step of where to go next uses a heap

"""