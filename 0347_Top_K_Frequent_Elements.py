from collections import Counter
from typing import List

# Problem: Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [num for num, _ in counter.most_common(k)]

# Time: O(NlogK), where N is the length of nums. We count the frequency of
# each number in O(N) time, then we add N numbers to the heap, each in O(logK)
# time. Finally, we pop from the heap K times. 
# As K ≤ N, this is O(NlogK) in total.
