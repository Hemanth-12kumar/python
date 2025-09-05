# Day-1
#python=Python is a high-level, general-purpose programming language known for its
#  readability and simplicity.
#  It was created by Guido van Rossum 
print("hello world")
#variable=a reusable container  for storing a value(strings,variables,integers,floats,
# booleans).
#         a variable behaves as if it were the value it contains

#strings=represented by quotes
age =18
print (age)
#f-string="formatted string literal," is a feature introduced in Python 3.6 that provides 
#          a concise and readable way to embed expressions inside string literals.
print ("I am years "+ str(age) + "old")
print("I am years", age , "  old")
print (f"I am years {age} old" )
print(f"hello{"hemanth"}")

#integers = shouldn't contain strings or quotes
age =18
players=11
bats =5
print(f"Each should be above {age} years")
print(f"No.of {players} palyers in team")
print(f"There are {bats} bats only")

#Floats= it is a number that contains decimal component 
gpa =9.2
distance=12.5
price=15.90

print(f"My first gpa is {gpa}")
print(f"I travel from {distance}kms everyday")
print(f"The cost of my pen is ${price}")

#boolean=it is either true or false(they should be CAPITAL)
is_student=True
print(f"are you a student? {is_student}")
for_sale=False
if for_sale:
   print("you car on for_sale ")
else:
   print("your car NOT on for_sale")
is_online= False
if is_online:
   print("you are online")
else:
   print("you are offline")   
