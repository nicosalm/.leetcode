
# -- list comprehensions 
# [[output value] for (i in iterable) if (filter conditions)]

# --- example 1: for loop with conditional
arr = [1, 2, 3, 4, 5]
res = []

# for i in arr:
    # if i % 2 == 0:
        # res.append(i**2)
# print(result)

print([ i**2 for i in arr if i%2 == 0])

# --- example 2: multiple for-loops
# TODO: flatten the 2d array and take only even numbers 

mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
# res = []
# for row in mat:
    # for i in row:
        # if i%2 == 0:
            # result.append(i)
# print(res)

print([i for row in mat for i in row if i%2==0])

# --- example 3: paired outputs
arr_1 = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
arr_2 = [6, 4, 6, 1, 2, 2]

# res = []
# for i in arr_2:
    # res.append((i, arr_1.index(i)))
# print(res)

print([(i, arr_1.index(i)) for i in arr_2])

# --- example 4: dictionary comprehension

arr_1 = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
arr_2 = [6, 4, 6, 1, 2, 2]

# res = {}
# for i in arr_2:
#     res[i]=arr_1.index(i)
# print(res)

print({i: arr_1.index(i) for i in arr_2})

# --- example 5: string tokenizing 

sentences = ["a new world record was set", 
             "in the holy city of ayodhya", 
             "on the eve of diwali on tuesday", 
             "with over three lakh diya or earthen lamps", 
             "lit up simultaneously on the banks of the sarayu river"]

stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']

# results = []    
# for sentence in sentences:
#     sentence_tokens = []
#     for word in sentence.split(' '):
#         if word not in stopwords:
#             sentence_tokens.append(word)
#     results.append(sentence_tokens)
# print(results)

# option A: flatten
print([word for sentence in sentences for word in sentence.split(' ') if word not in stopwords])

# option B: distinguish which words belong to which sentences
print([[word for word in sentence.split() if word not in stopwords] for sentence in sentences])
