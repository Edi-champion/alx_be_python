#!/usr/bin/python3


# match_case_calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation :
    case "+" :
        summ = num1 + num2
        print("The result is {}".format(summ))
        
    case "-" :
        dif = num1 - num2 
        print("The result is {}".format(dif))
    case "*" :
        product = num1 * num2
        print ("The result is {}".format(product))
    case "/": 
        if num2 == 0:
            print ("Cannot divide by 0")
        else :
            div = num1 / num2 :

            print ("The result is {}".format(div))
    case_:
        print("Invalid operation")
