user1 = input("What is your name?")
gender1 = input("Male or Female?")
if gender1=="Male":
    user1= "Mr. "+user1
else:
    user1= "Ms. "+user1
user2 = input("What is your name?")
gender2 = input("Male or Female?")
if gender2=="Male":
    user2= "Mr. "+user2
else:
    user2= "Ms. "+user2
user3 = input("What is your name?")
gender3 = input("Male or Female?")
if gender3=="Male":
    user3= "Mr. "+user3
else:
    user3= "Ms. "+user3

slices_of_pizza = int(input("How many slices in the pizza?"))
price_of_pizza = float(input("What is the price of the pizza?"))
price_of_aSlice = price_of_pizza/slices_of_pizza


user1_ate_in_percentage = float(input(user1+", how much did you ate? (in percentage)"))
user2_ate_in_percentage = float(input(user2+ ", how much did you ate? (in percentage)"))
user3_ate_in_percentage = float(input(user3+ ", how much did you ate? (in percentage)"))

number_of_slices_ate_by_user1 = int(slices_of_pizza*(user1_ate_in_percentage*(1/100)))
number_of_slices_ate_by_user2 = int(slices_of_pizza*(user2_ate_in_percentage*(1/100)))
number_of_slices_ate_by_user3 = int(slices_of_pizza*(user3_ate_in_percentage*(1/100)))

user1_needs_to_pay = str(price_of_aSlice*number_of_slices_ate_by_user1)
user2_needs_to_pay = str(price_of_aSlice*number_of_slices_ate_by_user2)
user3_needs_to_pay = str(price_of_aSlice*number_of_slices_ate_by_user3)

print(user1+" had "+str(number_of_slices_ate_by_user1)+" slices. Please, pay "+user1_needs_to_pay+". ")
print(user2+" had "+str(number_of_slices_ate_by_user2)+" slices. Please, pay "+user2_needs_to_pay+". ")
print(user3+" had "+str(number_of_slices_ate_by_user3)+" slices. Please, pay "+user3_needs_to_pay+". ")




