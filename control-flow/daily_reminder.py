#/usr/bin/python3

task = input("Enter your task: ")
priority=  input(" Priority (high/medium/low): ")
tim-bound= input("Is it time-bound? (yes/no): ")

match case priority :
    case "high":
        if time-bound == "yes" :
            print("'task' is a high priority task that requires immediate attention today!")
        else:
            print("'task' is high priority task. Consider completing it when you have free time.")
    case "medium":
        if time-bound =="yes"
        print("'task' is medium priority task that requires your immediate attention today!")
        else :
            print("'task' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time-bound== "low":
            print("'task' is a low priority task that requires immediate attention today!")
        else :
            print("'task' is a low priority task. Consider completing it when you have free time.")

