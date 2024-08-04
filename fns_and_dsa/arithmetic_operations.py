#!/usr/bin/python3


def perform_operation(num1, num2, operation):
    print("Arithmetic Operations")
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    operation=input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

   # if operation not in ["add", "subtract", "multiply", "divide"]:
    #    print("Invalid operation. Please try again")

    match case operation:
        case "add":
            result= num1 + num2
            print(f"Result: {result}")
        case "subtract":
            result= num1 - num2
            print(f"Result: {}")
        case "multiply":
            result= num1*num2
            print(f"Result: {}")
        case "divide":
            if num2==0
                print("Cannot divide by 0, choose another number : ")
                return

           # else :
             result=num1 / num2
             print(f"Result: {}")

