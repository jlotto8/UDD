"""
Mini interview question: pair sum
Goal: solve this problem in < 30 minutes.
Write a function that takes as input two arguments:
1. An array of numbers
2. An integer `k`
and returns an array with all of the pairs of numbers from that array that sum to `k`. You can’t use the same number twice. You can assume that there are no duplicate numbers in the array.
Example
- Input array: `[1, 9, 6, 3, 5, 4]`
- `k`: 10
- Result: `[[1, 9], [6, 4]]` // Note that `[5, 5]` is not in the solution

pseudocode

copy the array to a set
create a list to hold lists of pairs
subtract each integer in the set from k- called target; if the result of k - int is in the set,  that target and the number substracted are a pair sum
add the target and interget to the result
 
problems with above code after attempt: 
- modifiying the set during the loop caused problems
- the pairs were counted twice e.g [6,4], [4,6]

made a set, added num, and target to it (pair), checked to see if pairs were in it, then added to results list only if the target and num (pair) were not in the set and if the target was not the same as the num ( to avoid [5,5])
"""

def pair_sum(lst,k):

    list_to_set = set(lst)
    results = []
    seen_nums = set()

    for num in list_to_set:
        target = k - num
        if target in list_to_set and num not in seen_nums and target not in seen_nums and target != num:
            results.append([num,target])
            seen_nums.add(num)
            seen_nums.add(target)

    return results

print(pair_sum([1, 9, 6, 3, 5, 4], 10))

