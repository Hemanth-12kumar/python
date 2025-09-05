 #Typecasting= The process of converting a variable one data type to another data type 
 #  str(),int(),float(),bool()


#input=A function that prompts the user to enter data
#      Returns the entered data as string 


#print(f"Hello{name}")
#print(f"You are{age} years old.")
# EX-1: AREA OF RECTANGLRE
#length=int(input("enter the length:"))
#breadth=int(input("enter the breadth:"))
#3print(area)
# ex-2: shopping cart program 
#item=input("what are you going to buy?:")
#price=float(input("what is the price of the item?:"))
#quantity=int(input("how many are you going to buy?:"))
#total=price*quantity
#print(f"the total is:${total}
#print(f"you bought{quantity}{item}/s")



#MADLIDS GAME
''''
adjective=input("Enter an adjective (description):")
number=int(input("Enter a number:"))
noun1=input("Enter a noun1(person,thing,place):")
noun2=input("enter a noun2(person,thing,place):")
adverb=input("Enter a adverb:")
verb=input("Enter a verb ending with ing:")

print(f"I went to a {adjective}zoo.end")
print(f"It was around {number} acres.")
print(f"There are many {noun1}.")
print(f"The {noun2} was {adverb} friendly.")
print(f"The animals are {verb} the helpers.")'''

#arithmetic operators
#a=6
#a=a+1
#a+=1
#a=a-3
#a-=3
#a=a*7
#a*=7
#a= a/2
#a/=3
#a**=3
#remainder =a%2(modulus only give the remainder)
#print(remainder)
#z=5
#result=round(x)
#result=max(x,y,z)
#result=min(x,y,z
#result=pow(5,6)
#result=abs(y)
#print(result)

#import math
#x=9.1
#print(math .pi)
#print(math.e)
#result=math.sqrt(64)
#print(result)
#result = math.ceil(x)
#result=math.floor(x)
#print(result)

#import math
#to calculate circumference of a circle =( 2pi r)
#radius=float(input("enter the radius:"))
#circumference = 2*math.pi#*radius
#print(f"the circumference of a circle is{round(circumference)}:")


#import math
#to calculate area of a circle=pi. r**2
#radius = float(input("enter the radius:"))
#area=math.pi*radius**2 (or) math.pi*pow(radius,2)
#print(f"the area of a circle is {area}")


#import math
#to find hypotenuse of a right triangle=math.sqrt(a**2+b**2)
#a=float(input("enter the length of one side :"))
#b=float(input("enter the length of another side:"))
#hypotenuse=math.sqrt(pow(a,2)+pow(b,2))
#print(f"the hypotenuse of a triangle is {hypotenuse}")


#If statements
#If=do some code only do something condition  is True
#     Else do something else

'''age=int(input("enter your age:"))

if age>= 100:
    print("you are too old")
elif age>=18:
    print("you are signed up")
elif age<0:
    print("you haven`t born ")
else:
   print("you must be 18+ to sign up")'''



#even or odd 
#number =float(input(" enter the number:"))
#if   number %2==0:
 #   print("even number")
 # else:
 #    print("odd number")


''''
Order =input("would like food?(Y/N)")
if Order=="Y":
   print("your order is on the way! ")
else:
   print("waiting for your order?")'''
''''
name=input("Enter your name !")
if name=="":
   print ("your name is not entered.")
else:
   print(f"Hello{name}")'''

#is_student=False
#if is_student:
#    print("your a student.")
#else:
#    print("your are not a student")

''''
online=False
if online:
    print("you are online" )
else:
    print("you are offline ")'''



#calculator
''''
number1=float(input("Enter the number1: "))
number2 =float(input("Enter the number2: "))
operator= input("Enter the operator(+,-,*,/): ")
if operator == "+":
   result=number1+number2
   print(result)
elif operator=="-":
   result=number1-number2
   print(result)
elif operator=="*":
   result=number1*number2
   print(result)
elif operator=="/":
   result=number1/number2
   print(result)
else:
   print("Error!")'''

#weight convertor program
''''
weight= float(input("Enter the weight:  "))
unit=input("kilogram or pounds(K/L): ")
if unit=="k":
   weight=weight*2.205
   print(f" your weight is{weight}lbs")
elif unit=="L":
   weight=weight/2.205
   print(f"your weight is {weight}kg's")
else:
   print("in valid unit")'''


#temparature converter program
''''
temp=float(input("Enter the temparature: "))
unit=input("Celsius or Kelvin  (C/K): ")

if unit == "C":
    temp=temp+273
    unit="K"
elif unit=="K ":
    temp=temp-273
    unit="C"
else:
    print("invalid unit")

print(f"your temperature is {temp}{unit}")'''

print("hello world")
