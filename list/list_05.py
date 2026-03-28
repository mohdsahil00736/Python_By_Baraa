# Adding in a list

print("=="*20 )
print()
print("Add Item to the list ")
print("=="*20 )

letters1 = ['a', 'b', 'c', 'd']
# Add item at end
letters1.append('x')
letters1.append(3)
print(letters1)
print()

print("=="*20)

letters2 = ['a', 'b', 'c', 'd']
# Add item by position 
letters2.insert(0, 'x')
letters2.insert(2, 3)
print(letters2)
print()

print("=="*20)

matrix = [
    ['a', 'b', 'c'],  # Row 0 
    ['p', 'q', 'r'],  # Row 1
    ['x', 'y', 'z'],  # Row 2
]

matrix.append(['l', 'm', 'n'])  # add at last 
matrix.insert(0, ['a','a','a']) # add by postion
print(matrix)
print()


matrix2 = [
    ['a', 'b', 'c'],  # Row 0 
    ['p', 'q', 'r'],  # Row 1
    ['x', 'y', 'z'],  # Row 2
]

matrix2[1].append('x')
matrix2[2].insert(0, 'z')
print(matrix2)
print()



print("=="*20 )
print()
print("Remove Item from the list ")
print("=="*20 )



# Remove Item from the list

letters5 = ['a', 'b', 'c', 'd']
# remove everything 

# letters5.clear()
print(letters5)
print()

letters5.remove('a')  # by value 
letters5.pop()  # By default it remove the last one 
# letters5.pop(2)  # By index 
print(letters5)
print()


matrix3 = [
    ['a', 'b', 'c'],  # Row 0 
    ['p', 'q', 'r'],  # Row 1
    ['x', 'y', 'z'],  # Row 2
]

# matrix3.remove(['a', 'b', 'c'])
# matrix3.pop()  # By default it remove the last one 

matrix3[0].remove('a')
matrix3[2].pop(0)
print(matrix3)
print()


print("=="*20 )
print()
print("Update Item In the list ")
print("=="*20 )

# Update Item In the list 

letters6 = ['a', 'b', 'c', 'd']

letters6[0] = 'x'
letters6[3] = 'y'
print(letters6)
print()

matrix4 = [
    ['a', 'b', 'c'],  # Row 0 
    ['p', 'q', 'r'],  # Row 1
    ['x', 'y', 'z'],  # Row 2
]

# matrix4[0] = ['l', 'm', 'n']
matrix4[0][0] = '_'
matrix4[1][1] = '_'
matrix4[2][2] = '_'
print(matrix4)