#This program determines the greatest common divisor of two numbers.
def gcd(number1, number2):
    if number1 == 0:
        return number2
    elif number2 == 0:
        return number1
    else:
        return gcd(number2, number1%number2)
def inputValues():
    number = input("Enter new value: ")
    try:
        return int(number)
    except ValueError:
        print("Enter Integer numbers")

number1 = inputValues()
number2 = inputValues()

if number1 == None or number2 == None:
    pass
elif (number1 < 0) or (number2 < 0):
    print("Enter positive numbers")
else:
    print(gcd(number1, number2))