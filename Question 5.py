
print("Enter the first list of friends:")
list1 = input("Enter names separated by commas: ").split(',')
list1 = [friend.strip() for friend in list1]


print("Enter the second list of friends:")
list2 = input("Enter names separated by commas: ").split(',')
list2 = [friend.strip() for friend in list2]


merged_list = list(set(list1 + list2))


merged_list.sort()

print("Merged list of friends without duplicates:")
print(merged_list)