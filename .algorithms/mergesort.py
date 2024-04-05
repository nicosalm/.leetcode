from typing import List

# we will define functions merge and mergesort

def mergesort(arr: List[int]):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        merge(left, right, arr)

def merge(left: List[int], right: List[int], arr: List[int]):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# T(n) = 2T(n/2) + O(n) = O(nlogn)
