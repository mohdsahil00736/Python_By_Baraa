# lambda function 

mult = lambda x: x*2
print(mult(2))

check = lambda i : i in "pyhton"
print(check('z'))


# map in lambda 


price = ['$12.50', '$9.98', '$100.00']
print(list(map(lambda p : float(p.replace("$", "")), price)))


# filter in lambda

student = [['Maria', 88],
           ['kumar', 90],
           ['max', 55]]

print(student[2][1]> 70)

print(list(filter(lambda row : row[1] > 70, student)))


print(list(filter(lambda row : row[0].startswith('M'), student)))

print()

print("=="*20 , '\n')

''' Comphrenshion-> 1 Data transformation
                    2 for loop 
                    3 data filtering  '''


domain = ['www.google.com',
          'openai.com',
          'localhost',
          'www.datawithbaraa.com']

cleaned = [ 
    d.lower().replace("www.", '')
    for d in domain
    if "." in d 
]                   

print(cleaned)
