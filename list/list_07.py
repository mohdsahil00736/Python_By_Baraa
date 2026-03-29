
# Copying in the list 
import copy

letters = ['a', 'b', 'c', 'd']

# by Reference (  =  )
copy_list = letters
letters.pop()
copy_list.append('e')
print("original ", letters)
print("Copy :" , copy_list)

print()
print("=="*20)
print()

# by .Copy() , it create new copy in memory 
# it is a Shallow copy 

letters1 = ['a', 'b', 'c', 'd']

copy_list1 = letters.copy()
letters.pop()
copy_list1.append('e')
print("original ", letters1)
print("Copy : " , copy_list1 , "\n")


matrix = [
    ['a', 'b'],  # Row 0 
    ['p', 'q'],  # Row 1  
]

mat_copy = matrix.copy()
matrix.pop()
mat_copy[0].append('g')
print("original ", matrix)
print("Copy :" , mat_copy)



print()
print("=="*20)
print()

# deepcopy is used for fully independent copy at any level 

matrix1 = [
    ['a', 'b'],  # Row 0 
    ['p', 'q'],  # Row 1  
]

mat_copy1 = copy.deepcopy(matrix1)
matrix1.pop()
mat_copy1[0].append('g')
print("original ", matrix1)
print("Copy :" , mat_copy1)

