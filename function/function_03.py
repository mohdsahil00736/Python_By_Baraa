# Action function 

# Task to store application log message ina file 

def write_log(message):
    with open(r"D:\NEW\Bara Pyhon\app.log", "a") as file:
        file.write(message +  " \n")


write_log("App Started ")
write_log("user logged in ")
write_log("App stopped ")


# Data Transformation 

def clean_and_split_email(email):
    cl_email = email.strip().lower()

    username, domain = cl_email.split('@')
    return {"username" : username,
            "domain": domain}

print(clean_and_split_email(" Mohdsahil@gmail.com "))


# Validation 

# task check if a password meets the minimun length of a 8 char 

def is_valid_password(password):
    return len(password) >= 8 

print(is_valid_password("123456"))
print(is_valid_password("123456789"))


# check a valid email 

def is_vlaid_email(email):
    return "@" in email and "." in email 


print(is_vlaid_email("mohdashil@gmail.com"))