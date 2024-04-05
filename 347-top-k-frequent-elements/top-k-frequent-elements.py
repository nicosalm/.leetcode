class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # counter = Counter(nums)
        # return [num for num, _ in counter.most_common(k)] --- this is a cop out

        '''
        Intuition: We use bucket sort!
            (1) Create a hashmap to store the frequencies,
            (2) Create a bucket containing the max counts and the values corresponding to each max count, 
            (3) Pull the k-most counts and return it
        '''

        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        bucket = [[] for i in range(len(nums) + 1)]
        for key, val in hashmap.items():
            bucket[val].append(key)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            values = bucket[i]
            for val in values:
                result.append(val)
                if len(result) == k:
                    return result
        
        return [None]

        # O(n) time, O(n) space