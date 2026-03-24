
# email must not be emptyt 
# email must contain a '.' and '@ '
# email must contain exactly one '@' symbol 
# email must ends with .com, .org or .net 
# email must not be longer then 254 character 
# email must start and end with a letter a digit 
# email must not have any space in between 

email = "sahil@gamil .com" 
flag = True 
email = email.strip()
                                             
if email == "":    # email must not be emptyt 
    print( "Email cannot be empty ")
    flag = False

if  not ('.' in email and "@" in email ):  # email must contain a '.' and '@ '
    print("Email must contain . and @ ")
    flag = False

if email.count('@') != 1 :  # email must contain exactly one '@' symbol 
    print("Email must contain exactly one @ ")
    flag = False   

if  not email.endswith(('.com', '.net', '.org')):  # email must ends with .com, .org or .net 
    print("Email nust ends with .com , .net , .org")
    flag = False

if len(email) > 254 :   # email must not be longer then 254 character 
    print("Email must not greater then 254")
    flag = False

if not (email[0].isalnum() and email[-1].isalnum()):  # email must start and end with a letter a digit 
    print("Email stars and ends with num or alphabet")
    flag = False

if (" " in email ):  # email must not have any space in between 
    print("Email does not contain  any space in between ")
    flag = False

if flag :
    print("Email is valid ")

