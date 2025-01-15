#list - it is collection of items

my_list = [1,2,3,4]

#indexing
print("enter index 0 : ", my_list[0])

#changing an element
my_list[1] = 20
print("list after changing list of index 1 :",my_list)

#append - add more one item to list
my_list.append(5)
print("list after append 5 :", my_list)

#extend - add more items to list i.e extending list
my_list.extend([6,7])
print("list after extending some items : ",my_list)

#insert - inserting any item to any particular index
my_list.insert(1,10)
print("list after inserting item to particular index : ", my_list)

#remove - removing any item in list
my_list.remove(10)
print("list after removing item to particular index : ", my_list)

my_copy_list = my_list.copy()
print("my copy list:",my_copy_list)

my_list.clear()
print("now my list is:", my_list)

my_copy_list.sort()
print("sorted lis :",my_copy_list)

my_copy_list.reverse()
print("reverse list :",my_copy_list)


