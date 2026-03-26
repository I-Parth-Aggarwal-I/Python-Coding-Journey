def add_items(list):
    item = input("Enter the item to add: ")
    list.append(item)
    print(f"{item} added to the list.")

def remove_items(list):
    if list is None or len(list) == 0:        
        print("The shopping list is empty. Nothing to remove.")
        return
    item = input("Enter the item to remove: ")
    if item in list:
        list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")

def view_list(list):
    if list is None or len(list) == 0:        
        print("The shopping list is empty. Nothing to view.")
        return
    print("Shopping List:")
    for item in list:
            print(f"- {item}")

def modify_items(list):
    if list is None or len(list) == 0:
        print("The shopping list is empty. Nothing to modify.")
        return
    item = input("Enter the item to modify: ")
    if item in list:
        new_item = input("Enter the new item: ")
        index = list.index(item)
        list[index] = new_item
        print(f"{item} modified to {new_item}.")
    else:
        print(f"{item} not found in the list.")

def main():
    shopping_list = []
    while True:
        print("1. Add items")
        print("2. Remove items")
        print("3. View list")
        print("4. Modify items")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_items(shopping_list)
        elif choice == '2':
            remove_items(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            modify_items(shopping_list)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

main()