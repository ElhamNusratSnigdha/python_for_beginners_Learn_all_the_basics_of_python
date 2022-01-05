person_name = "Elham"
object_1 = "car"
object_1_color = 'red'
object_name_2 = 'house'
object_2_age = "20 years old"

print("Hello, "+person_name)
print("I am very interested by your "+object_1+". Is it "+object_1_color+" ?")
print("Also, "+person_name+" is your "+object_name_2+" older than "+object_2_age)
print("Thank you "+person_name)

having_a_house = False
if having_a_house:
    print("I own a small house.")
else:
    print("I don't own a house.")


print("I love pizza.")
sentence = "I love Pizza."
print(sentence)

#Functions
print(sentence.upper())
print(sentence.lower())

print(sentence.islower())
print(sentence.isupper())
print(sentence.lower().islower())

#find length function
print(len(sentence))

#replace 1st one with 2nd
print(sentence.replace("Pizza","Burger"))

#find index
print(sentence.index("P"))

# break lines \n
print("I love pizza\nand coke.")

print("Find the max")
print(max(1,5,6,2,9,4,30))

print("Find the min")
print(min(1,5,6,2,9,4,30))
print(min(-1,-5,0.0006,2,9,4,30))

#to write all math functions
from math import*

print("All math functions")
complete_number = 45
negative_number = -6
floating_number = 4.89

print(10+19)
print(10+5*6)
print((10+5)*6)
print((((10+8)/2)*3)-9)

print("Cascading or convert")
print(int((((10+8)/2)*3)-9))
print(int("2"))
age = 24
print("My age "+str(age+10))

print("Power function")
print(5**2)
print(pow(5,2))
print(52/36+pow(5,2))

print("Round function")
print(round(52/36+pow(5,2)))
print(-round(52/36+pow(5,2)))

print("Absolute function")
print(abs(round(52/36-pow(5,2))))

print("Square function")
print(sqrt(25))

#Ceiling Function: the least integer that is greater than or equal to x.
print("Ceiling function")
print(ceil(23.00001))
print(ceil(23.999999))

#Floor Function: the greatest integer that is less than or equal to x.
print("Floor Function")
print(floor(23.00001))
print(floor(23.999999))

print("Factorial function")
print(factorial(3))
print(factorial(100))

print("Python input function")
print(input("What is your name?"))
age = input("What is your age?")
print("My age is "+age)
food = input("What would you like to eat?")
drink = input("What would you like to drink?")
print("I would love to have "+food+" and "+drink)

print("Working with Functions") #crreate your own function
def love(name):
    print("I love "+name)
love("You")

def person1(name): #'name' parameter
    print(name+": Hello, how can I help you?")

def person2(food,drink,dessert,name): #'food,drink,dessert,name' parameters
    name = input("What is your name?")
    food = input("What would you like to have?")
    drink = input("Which beverage you want?")
    dessert = input("Which dessert do you want?")

    print(name+', I would like have '+food+". I want to drink "+drink+'. And as dessert '+dessert)

def person1_2(name):
    print(name+', thank you.')

person1("Elham")
person2('food','drink','dessert','name')
person1_2("Elham")

print("Return statement in function") #a statement that completes the execution by returning something

def calculation(a,b,c):
    print(a+b+c)
    return print(a-b-c)
    print(a*b/c)

calculation(1,2,3)


print("if elif and else statement. yaay")
i_want_to_eat = True
i_want_to_drink = False

if i_want_to_eat:
    print("Let's have a Pizza.")
else:
    print("I am full.")

if i_want_to_eat and i_want_to_drink: #both needs to be True
    print("Let's have Pizza and a Coke")
else:
    print("I am full.")

if i_want_to_eat or i_want_to_drink: #one of them True
    print("Let's go to restaurant.")
else:
    print("I am full")

if i_want_to_eat:
    print("I want food")
elif i_want_to_drink:
    print("I want drink")
else:
    print("I am full")

if not i_want_to_drink:
    print("I am full")
else:
    print("I want food")



var1=5
var2=5
var3=2

if var1==var2!=var3:
    print("Both Equal")
else:
    print("Not equal")

if var1>=var3:
    print("Greater or equal")
else:
    print("lesser")

person1_name = input("What is your name?")
person1_wallet = float(input("How much money do you have?"))
person2_name = input("What is your name?")
person2_wallet = float(input("How much money do you have?"))
person3_name = input("What is your name?")
person3_wallet = float(input("How much money do you have?"))

if person1_wallet > person2_wallet and person1_wallet > person3_wallet:
    print(person1_name+" is the richest.")
elif person2_wallet > person1_wallet and person2_wallet > person3_wallet:
    print(person2_name+" is the richest.")
elif person3_wallet > person2_wallet and person3_wallet > person1_wallet:
    print(person3_name+" is the richest.")


def question():
    rules = input("You need to answer every question by Yes or No. Do you understand?")
    question1 = ' '
    question2 = ' '
    question3 = ' '

    if rules!='Yes':
        return print("Try again!")
    else: question1 = input("Are you Hungry?")

    if question1!='Yes':
        return print("Then, let's go for a walk.")
    else: question2 = input("Do you want to go outside for dinner?")

    if question2!='Yes':
        return print("Okay. Then, let me cook something for you.")
    else: question3 = input("Do you wanna have Pizza?")

    if question3!="Yes":
        return print("We will find out later. Let's go, love.")
    else: print("Great, love. Let me get our jackets.")

question()

print("Lets learn Lists and its functions")
variable_1 = 'apple'
list_1 = ['apple', 'banana', 'grapes', 'lemon']
print(list_1)

list_1[3] = 'avocado'
list_1[1] = 'tomato'
print(list_1)

print(list_1[0]) #prints first element
print(list_1[1:3]) #print index 1 to before index 3
print(list_1[2:]) #prints index 2 till last

list_1.index(1,'watermelon') #index. new element (adding)
print(list_1)
list_1.clear() #clear everything
print(list_1)

list_2 = ['blank', 'blank', 'blank']
list_1.extend(list_2) #adding list 2 end of the list 1
print(list_1)

print(list_1.index('lemon')) #prints element index number

print(list_2.count('blank'))

random = list_1.copy()+list_2.copy()
print(random)

print('Difference between List and Tuple') #tupple unmutable

list = ['red', 'yellow', 'blue']
list.insert(2,'pink')
print(list)

colors =('blue','yellow','red')
shapes = ('square','triangle','circle')

tupple = colors+shapes
print(tupple)

print("Let's learn Dictionary")
colors = {'B':'Blue',
          'R':'Red',
          'O':'Orange'}
print(colors.get('B','stop')) #if we don't have the value of 'B', prints 'stop

students = { 1:'Jake',
             2:'Amir',
             3:'Hansa'}
print(students.get(1,"don't exist"))
print(students.get(5,"don't exist"))

print("Let's see While loop")
variable_1=25
variable_2=2000

while variable_1<variable_2:
    print(variable_1)
    print("not enough")
    variable_1=variable_1+5

print("Let's see For-loops")
for x in colors:
    print(x)

for letter in 'blue':
    print(letter)

for one_color in colors:
    if one_color=="red":
        break
    else: print(one_color)

for number in range(6):
    print(number)

for number in ramge(20,30):
    print(number)





