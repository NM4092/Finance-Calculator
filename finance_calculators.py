
""" Request user input either 'investment' or 'bond'
Store in a variable called calculator_input
If user selects 'investment'
Request the user input amount of money for depositing
Store input in a variable called 'user_deposit
Request user input the percentage interest rate
Store the input in a variable called 'interest_rate
Request user input the number of years for investing 
Store input in a variable called 'number_years'
Request user to input either 'simple' or 'compound interest'
Store in a variable called 'interest'
If the user inputs 'simple' interest
Calculate the answer using the formula
Print answer
Else
If the user inputs 'compound' interest
Calculate the answer using the formula
Print answer
Else if the user inputs 'bond'
Request user to input the value of the house
Store input in a variable called house_value
Request user inputs in interest rate
Store input in a variable called 'int_rate'
Request user input the number of months to repay
Store in a variable called number_months
Calculate the answer using formula 
Print answer
Else
Print ("Error. Please choose either 'investment' or 'bond'")

"""
# Importing math fucntions for calculations

import math

# User chooses which calculator to use

calculator_input= input("""Choose 'investment' or 'bond' from the menu below to proceed:\n
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan\n""") 
 
 
# Investment calculator

# Capitalisation should not affect program
if calculator_input.lower()=="investment" and calculator_input.upper() =="INVESTMENT":
        user_deposit=float(input("How much are you depositing ?")) 
        interest_rate=float(input("Pleae enter the percentage interest rate:")) 
        number_years=int(input("How many years of investment?"))     
        interest=input("Do you want simple or compound interest ?")
    
        #Changed variable names for calculations
        P= user_deposit
        #Divide interest by 100
        r=interest_rate/100 
        t=number_years
        
        # calculation for simple 
        if interest== "simple":
              A=round(P*(1+(r*t)))
              print(str("Your simple interest is R{}".format(A)))                               
        else: 
             A=round(P*(math.pow((1+r),t)))   
             print(str("Your compound interest is R{}".format(A)))
             
# Bond Calculator

# Capitalisation should not affect program                                
elif calculator_input.lower()== "bond" and calculator_input.upper()=="BOND":
      house_value=float(input("What is the current value of your house ?")) 
      int_rate=float(input("Please enter the percentage interest rate:"))
      number_months=int(input("How many months for repayment?"))
      
      
      # Changed variable names for calculations
      P= house_value
      #Divde interest by 100 then by 12
      i= (int_rate/100)/12
      n=number_months
      
      # Calculation for bond
      bond_price=round((i*P)/(1-(1+i)**(-n)))
    
      print(str("Your monthly repayment is R{}".format(bond_price)))
      
      # If user does not enter investment or bound
else:
      
    print("Error. Please choose either 'investment' or 'bond'")      
    

