
# Analysing in the list

number = [1, 2, 3, 4, 5]

print("Max :", max(number))
print("Min :", min(number))
print("Sum :", sum(number))
print("Length :", len(number))

print("=="*10)

print("All :" , all(number))
print("All :" , all([1, 3 , 5]))
print("All :" , all([1, 0, 5]))
print("All :" , all(['a', 'b', 'c'] ))
print("All :" , all(['a' , '', 'b']))

print("=="*10)

print("Any :" , any(number))
print("Any :" , any([1, 3 , 5]))
print("Any :" , any([1, 0, 5]))
print("Any :" , any(['a', 'b', 'c'] ))
print("Any :" , any(['a' , '', 'b']))

print("=="*10)

print('Count :', number.count(3))
print("index " , number.index(3))

print("=="*10)

list = [1, 4, 6, 8, 3]
print(3 in list)
print(3 not in list)

print("=="*10)

list1 = [1,2, 3]
list2 = [1, 2, 3]

print(list1 == list2)
print(list1 is list2)  # false because of not the same index


