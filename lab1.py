# Calculations lab 1 in assignment 2

# 1. Prompt the user to input the principal amount (P), rate of interest (R), and the time period in years (T).
# 2. Use the formula for simple interest: [ \text{Simple Interest} = \frac{P \times R \times T}{100} ]
# 3. Store the calculated simple interest in a variable.
# 4. Display the calculated interest using print().


enterprinciple = input ("Enter the principle amount: ")
principleamount = int (enterprinciple)

interest_rate = input ("Enter the interest rate: ")
rateamount = int (interest_rate)

yearinput = input ("Enter the number of years: ")
yearamount = int (yearinput)

#calculate the interest

simpleinterest = (principleamount * (rateamount/100)  * yearamount)
print ("The simple interest is ", simpleinterest)
