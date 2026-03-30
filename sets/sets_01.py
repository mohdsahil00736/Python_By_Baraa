# sets 

my_set = {10, 20, 30 ,10}
print(my_set)  # Unordered , Unique 

# print(my_set[1])  # Not indexed 
my_set.remove(20)  # Sets are mutable
print(my_set)

print()
print("=="*20)
print()


# sets method 

a = {10, 20, 30, 40 }

a.add(50)
print(a)

# a.update(60)  # any thing is iterable but int not allowed bec int is not iterable 
print(a)

a.update({5,7})
print(a)

a.update(['hi'])
a.update("hi")
print(a)

a.update((3, 5,6))
print(a)

# shortcut 

a |= {14, 15}
print(a)

# remove and discard 
# remove breaks the code but discard does not , if item not present 

a.remove(14)
a.discard(15)
a.pop()  # totaly random 
print(a)


