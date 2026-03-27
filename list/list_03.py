
# Unpacking in the list 

person = ['sahil', 23, 'Data Eng', 'India']

# name = person([0])
# age = person([1])
# role = person([2])
# country = person([3])

# ==========  Unpackig method  =============

# for all element of list 
name, age, role, country = person
print(name)
print(role)


# for only first element of list 
# first , rest 
name , *details = person 
print(name)
print(details)


# for last elem
# rest , last 
*deta , country = person
print(deta)
print(country)


# for only first and last element 
# first, rest , last 
name , *details , country  = person 
print(name)
print(details)
print(country)


# all Same task by the help of " _ "

name, _ , role, _  = person
print(name)
print(role)



# Both " * " , " _ " use for unpacking 

name , *_, country = person
print(name)
print(country)

*_ , country = person
print(country)


name, *_ = person 
print(name)

