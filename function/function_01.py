import math

# built in function 

name = "sahil"
print(len(name))

# function from libaries ( import first then call )

number = 43.5
print(math.ceil(number))

# User defined function 

def greet():
    print("Hello")

greet()

# Parameter and Argument 

def clean_name(name):
    cln_name = name.strip().lower()
    print(cln_name)

clean_name("  sahiL ")