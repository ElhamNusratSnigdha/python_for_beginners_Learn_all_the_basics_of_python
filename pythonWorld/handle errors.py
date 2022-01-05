#syntax error print(1/1).
#logical error print(1/0)

#value error
try:
    a = int(input("Enter number : "))
    print(1+a)
except ValueError:
    print("Please write a number.")