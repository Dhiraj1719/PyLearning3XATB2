#List - shopping list
shopping_list = ["milk", "pasta", "eggs", "bread", "rice"]

print(len(shopping_list))

#Print the entire list
print(shopping_list)

#Print the type of the list
print(type(shopping_list))

#Print the first item in the list
print(shopping_list[0])

#Print the last item in the list
print(shopping_list[-1])

#Print the second to last item in the list
print(shopping_list[-2])

#Print a slice of the list
print(shopping_list[1:3])

#Modify the list
shopping_list[0] = "chocolate"
print(shopping_list)

#Add an item to the list in end
shopping_list.append("cookies")
print(shopping_list)

#Add an item to the list in middle
shopping_list.insert(2,'jam')
print(shopping_list)

#Remove an item from the list
shopping_list.remove("cookies")
print(shopping_list)

#Add multiple items to the list
shopping_list.extend(["cookies", "cake"])
print(shopping_list)

#Remove the last item from the list
shopping_list.pop()
print(shopping_list)

#Remove the first item from the list
shopping_list.pop(0)
print(shopping_list)

#Sort the list
shopping_list.sort()
print(shopping_list)

#Clear the list
shopping_list.clear()
print(shopping_list)

my_list = [1,2,"bread",3.24,True]
print(my_list)
print(type(my_list))

'''length start from 1 and
index start from 0'''