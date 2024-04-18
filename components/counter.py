from collections import Counter

# -- collections.counter

nums = [1,1,1,2,2,3]
counter = Counter(nums)
result = [num for num, _ in counter.most_common()]
result_with_counts = [(num, count) for num, count in counter.most_common()]
print(result_with_counts)

seq = ['red', 'blue', 'red', 'green', 'blue', 'blue']
counter = Counter(seq)
result = {count: word for word, count in counter.most_common()}
print(result)

# Counter.most_common(k - the top k most frequent elements)
# Counter.elements() - an iterator over all elements repeating each 
#                      as many times as its count
# CounterA.subtract(CounterB) - subtrack the counts of one Counter from another
# Counter.total() # the sum of counts
