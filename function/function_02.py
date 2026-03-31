# build a clean name 

def clean_name(first_name , last_name, country = "default parameter "):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last 
    print(full_name, "Form ", country)

clean_name(" marYia  ", "  smiyh  ")  # positional argument  put valuse by position 

clean_name(first_name= " muajj ", last_name= "  SmitH") # keyword Argument 

clean_name(" MohaMMad  " , " SAHil  ", " IndiA ")



# *args  -> Positional Arguments
# **Kwargs -> Keyword Arguments 

def total(*args):
    print(type(args))
    print(sum(args))

total(1,2)
total(1,2,3)
total(1,2,3,4)


def create_user(**Kwargs):
    print(type(Kwargs))
    print(Kwargs)

create_user(first_name = "Md",
            last_name = "sahil",
            age = 25,
            country = "india")

# return function 

def clean_name(name):
    if not name:
        return None 
    else :
        cleaned = name.strip().lower()
        return cleaned
    
cln_name = clean_name("")
print(cln_name)


# multiple return function 

def clean_name(name):
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().lower()
    return lo_cleaned, up_cleaned
        
    
lo_name , up_name = clean_name(" mariA " )
print(lo_name)
print(up_name)


