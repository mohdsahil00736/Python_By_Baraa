# dictonary methods 

# access 
user = {"id": 1, "age": 30, "city": "india"}


# print(user['name'])  
print(user.get("name", "unknoun "))

# checks 
print("age" in user)
print("name" not in user )

# View objects 
print(user.keys())
print(user.values())
print(user.items())

print()
print("=="*20)
print()



# looping  

for u in user:
    print(u, user[u])

for key , value in user.items():
    print(key, value)


print()
print("=="*20)
print()


# add , remove , update 

user['name'] = "sahil" # add 
user['age'] = 35   # update
user.update({'age': 40, "city": "spain"}) # update 

print(user)

age = user.pop('salary', "not found")  # remove
print(user)
print('removed item :',age)
user.popitem()
print(user)

print()
print("=="*20)
print()


# fromkeys 


user2 = {
    'id': None,
    'age':None,
    'name':None,
    'city':None
}

print(user2)

user3 = dict.fromkeys(['id', 'age', 'name', 'city'], None)

print(user3)
user3['age'] = 40
print(user3)

print()
print("=="*20)
print()


# dict chalanges 

user_detail = {'id': 10, 'name': "shil", "age": 25, "city": "india"}

user_str = {
    k.upper(): v   # exploratiion 
    for k , v in user_detail.items()  # loop 
    if isinstance(v, str)  #filter
}

print(user_str)