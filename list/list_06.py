# sorting in the list 

letters = ['a', 'e', 'c', 'd']

(letters.sort())
# letters.sort(reverse= True)
print(letters)

matrix = [
    ['a', 'e', 'c'],  # Row 0 
    ['h', 't', 'r'],  # Row 1
    ['x', 'y', 'z'],  # Row 2
]

# matrix.sort()
print(matrix)

matrix[1].sort()
print(matrix)


new_list = sorted(letters)
print(new_list)
new_list2 = sorted(letters, reverse= True)
print(new_list2, "\n")

letters.reverse()
print(letters , "\n")

new_let = list(reversed(letters))  
print(new_let , "\n")


matrix2 = [
    ['a', 'e', 'c'],  # Row 0 
    ['h', 't', 'r'],  # Row 1
    ['x', 'y', 'z'],  # Row 2
]

# matrix2.reverse()
# print(matrix2 , "\n")

new_matrix = list(reversed(matrix2))
print(new_matrix)