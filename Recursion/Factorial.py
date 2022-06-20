# Non-tail recursion
def factorial(number):
    if number == 0:
        return 1
    else:
        return factorial(number-1)*number

def inputValues():
    number = input("Enter new value: ")
    try:
        return int(number)
    except ValueError:
        print("Enter a Integer number")

x = inputValues()

if x < 0:
    print("Enter a positive number")
elif x == None:
    pass
else:
    print(factorial(x))