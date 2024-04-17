
def binary_search(x: int, arr: list) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == x:
            return x
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# O(log n) time complexity
