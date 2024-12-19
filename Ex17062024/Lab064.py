def make_pizza(*toppings):
    for topin in toppings:
        print(topin)

Dhiraj = make_pizza("tomato")
Bhavana = make_pizza("corn")
amisha = make_pizza("paneer")

#list and tuple ----------
#tuple object cannot be changed
t = ("orange", "green", "white","black")
t[0] = "blue"
#TypeError: 'tuple' object does not support item assignment
#-----------------------------------------------------------------------------------
#list can change any object
l =["orange", "green", "white","black"]
l[0]= "blue"
print(l)