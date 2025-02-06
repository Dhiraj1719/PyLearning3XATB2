my_details = {"name":"Dhiraj",
              "nickname":"bunty",
              "city":"jalgaon",
              "state":"maharashtra"
              }

print(my_details)
print(len(my_details))
print(my_details.get("city"))
print(my_details["city"])
print(my_details.keys())
print(my_details.values())

#keys should be unique but value can be duplicate

dict2 = {"a":"25","b":"54","c":"54","a":45}
print(dict2) #a = 45 will be store in dictionary but b and c will have same value of 54
print(list(dict2.keys()))
print(list(dict2.values()))
for i in (list(dict2)):
    print(i)

for k,v in dict2.items(): #to get key and value pairs.
    print(k,v)