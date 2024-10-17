x = 10
y = 20
result = (x != y) # 10 not equal to 20
print(result)

#ternary operator
a = 5
b = 10
min_val = a if a < b else b
print(min_val)
max_val = a if a > b else b
print(max_val)

print("min_val is a" if a < b else "min_val is b")
print ("max_val is b" if b > a else "max_val is a")