password = "123456789"
type = " "
number_of_try = 0
number_max_of_try = 3
max_try = "Not Reached"

while type!=password and max_try!='Reached':
    if number_of_try<number_max_of_try:
        type=input("Type your password:")
        number_of_try=number_of_try+1
    else:
        max_try="Reached"

if max_try=="Reached":
    print("Account blocked")
else: print("Access granted.")

