#Compound interest calculator
principal=float(input("enter the principal amount: "))
rate = float(input("enter the rate of interest: "))
time =float(input("enter the time in years: "))
amount=principal*pow((1+rate/100),time)
print(f"the total amount after {time} years is Rs.{amount:.2f}") 

interest=amount-principal
print(f"the interest earned is Rs.{interest:.2f}")
