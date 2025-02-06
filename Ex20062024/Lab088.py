x = 120
print(x)
q,w,e =(1,2,3) #tuple is assign values to separate param/variable = unpacking
print(q)
print(w)
print(e)

#we can check item available in tuple answer will be in boolean
cities =("amalner","jalgaon","bhusawal","chopada","parola")
print ("chopada" in cities)


#if we want to add in tuple
t =(23,24,25)
print (t)
new_tuple = t + (26,)
print (new_tuple)

new_list = list(new_tuple)
print (new_list)
new_list.append(27) #list is mutable
print(new_list)

new_tuple2 = tuple(new_list)
print (new_tuple2)

