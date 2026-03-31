#action function
def write_log(message):
    with open(r"D:\NEW\Bara Pyhon\app.log", "a") as file:
        file.write(message +  " \n")


# validation function 
def is_vlaid_email(email):
    return "@" in email and "." in email 


# transformation function 
def clean_and_split_email(email):
    cl_email = email.strip().lower()

    username, domain = cl_email.split('@')
    return {"username" : username,
            "domain": domain}


# Orcastorator Function 
def process_email(email):
    write_log("Application Started ")
    if  not is_vlaid_email(email):
        write_log(f"Invalid Eamil recived : {email}")
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed Email :  {clean_email}")
    write_log("Applictin Stoped ")


email = input("please Enter the email : ")
process_email(email)