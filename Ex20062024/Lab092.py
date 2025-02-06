

set_new = set(["the testing academy","for","the testing academy"])
print(len(set_new))

for i in set_new:
    print(i)    #set only print unique items from items present in the set , no repetition allowed


set1 = set([1,2,3,4,5,6,7,8,9])
# print(len(set1))
# set1.remove(5)
# print(set1)
# print(len(set1))

set1.add(100)
print((set1))

set1.pop() #it removes first item from set
print(set1)

set1.remove(2)
print(set1) #set can adda and remove any item present in set now