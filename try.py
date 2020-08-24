try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Can not divide by zero")
    print(err)
except ValueError:
    print("Invalid input")
