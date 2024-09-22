# lab 3

#Objective:
#Create a program that converts a temperature given in Celsius to Fahrenheit.

#Instructions:

#Prompt the user to enter the temperature in Celsius.
#Use the conversion formula:
#[ \text{Fahrenheit} = (\text{Celsius} \times 9/5) + 32 ]
#Store the result in a variable.
#Print the temperature in Fahrenheit.
#Example Input/Output:

#Enter the temperature in Celsius: 25
#The temperature in Fahrenheit is: 77.0

celsius = input ("Enter the temperature in Celsius: ")
celsiustemp = float (celsius)

fahrenheit = (celsiustemp * (9/5) + 32)

print ("The temperature in Fahrenheit is: ", fahrenheit)