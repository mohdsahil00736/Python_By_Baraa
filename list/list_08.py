# Combining in the list 

letters = ['a','b', 'c']
numbers = [1,2,3]

comb = letters + numbers

comb2  = [letters , numbers]
print(comb) # gives a single list 
print(comb2) # gives a list of list seperated with comma 
print(letters * 2)

# extend a original list , 

numbers.extend(letters)
print(numbers)
print(letters)


# zip , we can pair list with string value

letters = ['a','b', 'c']
numbers = [1,2]

comb3 = list(zip(letters, numbers ))   # it goes with least no of item 
print(comb3)

comb4 = list(zip(letters, numbers, "Hi"))  # it goes with defalut value which you are given 
print(comb4)

