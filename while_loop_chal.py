
# 3 attempt 
# Yes within 3 attempt -> "Glad we are on the same page
# Otherwise 3 strike You out 

attempts = 0
while attempts < 3:
    answer = input("Do you Agree? (yes/no) ")
    if answer == "yes":
        print("Glad we are on the same page")
        break
    else:
        attempts += 1
else:  
    print(" 3 strike hit, you are out .")