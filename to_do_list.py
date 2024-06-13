todo_list = []
while True:
    print("To-Do List Menu:")
    print("1. Add item")
    print("2. View list")
    print("3. Delete item")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        item = input("Enter the item to add: ")
        todo_list.append(item)
        print('Added: ',item)
    elif choice == '2':
        if not todo_list:
            print("The to-do list is empty.")
        else:
            print("To-do list:")
            for index, item in enumerate(todo_list, start=1):
                print(index,".",item)
    elif choice == '3':
        if not todo_list:
            print("The to-do list is empty.")
        else:
            try:
                index_to_remove = int(input("Enter the number of the item to remove: ")) - 1
                if 0 <= index_to_remove < len(todo_list):
                    removed_item = todo_list.pop(index_to_remove)
                    print(f'Removed: {removed_item}')
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '4':
        print("The to-do list is completed")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
