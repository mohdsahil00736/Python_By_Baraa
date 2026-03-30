# Iterator and Iterable 

letters = ['a','b', 'c']  # iterable 

print(enumerate(letters))   # iterator 

print(list(enumerate(letters)))  # by default it gives the index starts from zero , it gives the list of tuples

print(list(enumerate(letters, start = 1 )))

for index, value in enumerate(letters):
    print(index, value)


numbers = [1,2,3]
print(list(reversed(numbers)))


letters1 = ['a','b', 'c']
numbers1 = [1,2, 3 ]

print(list(zip(letters1, numbers1)))

for l, n in zip(letters1, numbers1):
    print(l, n)


# Map function it takes the data type and iterable 

print(list(map(str.upper, letters)))

numbers2 = ['1', '2', '3']
print(list(map(int,numbers2)))

# Filter fun it also takes data type , iterable 

list1 = ['a', '', 'b', None, 'c', False]
print(list(filter(None, list1)))

print(list((filter(bool, list1))))

items = ['sql', '12', 'pyt', '56']

print(list(filter(str.isalpha, items)))

for i in filter(str.isalpha, items):
    print(i)