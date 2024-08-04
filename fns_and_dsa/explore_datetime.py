#!/usr/bin/python3


import datetime

def display_current_datetime():
    current_date=datetime.datetime.now()
    print(f"Current date and time: {current_date}")


def calculate_future_date(current_date):
    try:
        number_days=int(input("Enter the number of days to add to the current date: ")
    except ValueError:
        print("Enter an Integer.")
        return

    future_date= current_date + timedelta(days=number_days)
    print(f"Future date: {future_date}")

def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if __name__== "__main__":
    main()

