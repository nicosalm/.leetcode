
# top python tricks lol

# -- Lists
# --- Flatten the lists
import itertools

a = [[1, 2], [3, 4], [5, 6]]
b = list(itertools.chain.from_iterable(a))
print(b)

# --- Reverse the list
a = ["10", "9", "8", "7"]
print(a[::1])

# --- Combining different lists
a = ['a', 'b', 'c', 'd']
b = ['e', 'f', 'g', 'h']
for x, y in zip(a, b):
    print(x, y)

# --- Negative indexing lists
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[-3:-1])

# --- Analyzing the most frequent on the list
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(set(a), key = a.count))

# -- Strings
# --- Reversing the string
a = "python"
reversed = a[::-1]
print(f"Reverse is, {reversed}")

# --- Splitting the string
a = "Python is a language"
b = a.split()
print(b)

# Printing out multiple values of strings
print("on"*3 + ' ' + "off"*2)

a = ["I", "am", "not", "available"]
print(" ".join(a))

# -- Matrix
# --- Transposing a matrix
mat = [[8, 9, 10], [11, 12, 13]]
new_mat = zip(*mat)
for row in new_mat:
    print(row)

# -- Dictionary
# --- Inverting the dictionary
dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}
dict2 = {v: k for k, v in dict1.items()}
print(dict2)

# --- Merging multiple dictionaries 
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)

# -- Initialization
# --- Initializing empty spaces
import sys
a = 10
print(sys.getsizeof(a)) # 28

# --- Swapping values
x, y = 13, 26
x, y = y, x
print(x, y) 

# -- Map functions
# --- Implementing a map function

'''
    In competitive coding, you might come across an input like this:
    123456789

    To get the input as a list of numbers, perform the following
    list(map (int, input().split()))
'''
