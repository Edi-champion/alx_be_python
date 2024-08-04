#!/usr/bin/python3


def display_menu ():
    print("\nShopping List Manger")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


option=input("Choose an option: ")

def add_item(shopping_list):

    item=input("Enter the item to add: ").strip()
    shopping_list.append("item")
    print(f"{item} has been added to the shopping list.")

def remove_item(shopping_list):
    item = input("Enter the name of the item to remove: ")
    shopping_list.remove("item")
    print(f"{item} has been removed from the shopping list: ")

def view_list (shopping_list):
    if not shopping_list:
        print("The shopping list is empty")
    else :
        print("Shopping list:")
        for item in shopping_list :
            print(f"- {item}")

if __name__ == "__main__":
    shopping_list = []

def main():

while True :
    display_menu()
    choice = input("Choose an option (1, 2, 3, 4): ").strip()
    if choice == "1":
        add_item (shopping_list)
    elif choice == "2":
        remove_item(shopping_list)
    elif choice == "3":
        view_list (shopping_list)
    elif choice == "4":
        print("Exiting the shopping list manager")
        break 
    else :
        print("Invalid choice.")

