
# -- enumeration

# well, why exactly do we like enumerate? consider the alternative:

a = [1,2,3]
for i in range(len(a)):
    print(f"indx: {i}, val: {a[i]}", end=", ")

print()
# this is long and tedious. now, with enumerate:

for idx, val in enumerate(a):
    print(f"indx: {idx}, val: {val}", end=", ")

# enumerate works on any iterable while range(len()) only works on
# countable, indexable objects


