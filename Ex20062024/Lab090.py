set1 = {1,2,3,5,6}
set2 = {4,5,6,6}
my_set = set1.union(set2) # combination both sets
print(my_set)

my_set2 =set1.intersection(set2) #only common items from both sets
print(my_set2)

my_set3 = set1.difference(set2) #it only differ from common items i.e 5,6 is common but not 1,2,3 so it gives it
print(my_set3)

my_set4 = set2.difference(set1) #vice versa for set2 to set1
print(my_set4)