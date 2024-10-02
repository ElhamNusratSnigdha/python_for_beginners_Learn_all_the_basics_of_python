"""
Exercise: Array DataStructure
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""
monthlyExpense = [2200, 2350, 2600, 2130, 2190]

#Task1
print(f"1. In Feb, {monthlyExpense[1]-monthlyExpense[0]} dollars I spent extra compare to January.")

#Task2
total3monthExpense=0
for i in range(3):
    total3monthExpense=total3monthExpense+monthlyExpense[i]
print(f"2. Total expense in first quarter (first three months) of the year is {total3monthExpense}.")

#Task3
try:
    print(f"3. Yes! I spent exactly 2000 dollars in month {(monthlyExpense.index(20000)+1)}.")
except:
    print("3. No! I did not spent exactly 2000 dollars in any month.")

#Task4
monthlyExpense.append(1980)
print(f"4. June month just finished and my expense is 1980 dollar. The item is added to my monthly expense list: {monthlyExpense}")

#Task5
monthlyExpense[4-1]=monthlyExpense[4-1]-200
print(f"5. I have returned an item that I bought in a month of April and got a refund of 200$. My new monthly expense list based on this: {monthlyExpense}")
