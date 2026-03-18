def add_item(item_list):
    item = input("Enter an item to add: ").strip()
    if item not in item_list:
        item_list.append(item)
        print("Item has been added.")
    else:
        print("Item already in the list.")

def change_item(item_list):
    old_item = input("Enter the item to change: ").strip()
    if old_item in item_list:
        new_item = input("Enter the new item: ").strip()
        # หาตำแหน่งของ old_item ใน item_list และแทนที่ด้วย new_item
        # ใช้ index() เพื่อหาตำแหน่งของ old_item และแทนที่ด้วย new_item
        index = item_list.index(old_item)
        item_list[index] = new_item
        print("Item has been changed")
    else:
        print("Item is not in the list.")

def insert_item(item_list):
    item = input("Enter an item to insert: ").strip()
    position = int(input("Enter the position to insert: ").strip())

    # อยู่ระหว่าง 1 - ตำแหน่งสุดท้ายของรายการ ที่ +1
    if position <= len(item_list) + 1:
        item_list.insert(position, item)
        print("Item has been inserted.")
    else:
        print("Invalid position.")

def remove_item(item_list):
    item = input("Enter an item to remove: ").strip()
    if item in item_list:
        item_list.remove(item)
        print("Item has been removed.")
    else:
        print("Item is not in the list.")

def show_items(item_list):
    if item_list:
        print("Items in the list:", item_list)
    else:
        print("The list is empty.")

# Main program
print("What do you want to do?")
print("1. Add item")
print("2. Change item")
print("3. Insert item")
print("4. Remove item")
print("5. Show items")
print("6. Exit")

item_list = []
choose = input("Enter your choice: ").strip()
while choose != "6":
    
    if choose == "1":
        add_item(item_list)
    elif choose == "2":
        change_item(item_list)
    elif choose == "3":
        insert_item(item_list)
    elif choose == "4":
        remove_item(item_list)
    elif choose == "5":
        show_items(item_list)
    elif choose == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
    choose = input("Enter your choice: ").strip()