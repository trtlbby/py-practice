#This is a simple calculation built using python

#Operation
numberOne = int(input("Enter first number: "))
numberTwo = int(input("Enter second number: "))
numberSum = 0

operation = str(input("Enter operation (+, -, *, /)"))

#Conditions
if operation == '+':
    numberSum = numberOne + numberTwo
    print(numberSum)
elif operation == '-':
    numberSum = numberOne - numberTwo
    print(numberSum)
elif operation == '*':
    numberSum = numberOne * numberTwo
    print(numberSum)
elif operation == '/':
    numberSum = numberOne / numberTwo
    print(numberSum)
else:
    print("Error. Check Input")

#Worked properly. Ready to add.