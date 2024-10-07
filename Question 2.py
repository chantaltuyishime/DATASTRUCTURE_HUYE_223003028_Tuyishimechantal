
shopping_list = [input("Enter item to add to the shopping list: ") 
for _ in range(int(input("Enter number of items: ")))]


print("\nShopping list:", shopping_list)


item_to_remove = input("\nEnter item to remove from the list: ")
shopping_list.remove(item_to_remove)


print("Updated shopping list:", shopping_list)