#calculator

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
   print("Error!")
