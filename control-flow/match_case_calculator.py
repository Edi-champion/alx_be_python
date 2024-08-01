#!/usr/bin/python3


# match_case_calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation :
    case "+" :
        summ = num1 + num2
        print("The result is {} + {} = {}" .format(num1, num2, summ))
    case "-" :
        dif = num1 - num2 
        print("The result is {} - {} = {}".format(num1, num2, dif))
    case "*" :
        product = num1 * num2
        print ("The result is {} * {} = {}" .format(num1, num2, product))
    case "/": 
        if num2 == 0:
            print ("Cannot divide by 0")
        else :
            div = num1 / num2 :

            print ("The result is {} / {} = {}" .format(num1, num2, div))
    case_:
        print("Invalid operation")
