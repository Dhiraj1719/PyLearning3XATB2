# Multiple Conditions
# instead of Switch case in Python we used Match Case
# Match case is available from Python 3.10 onwards
# Match case is similar to Switch case in other languages

# numbers = int(input("Please input the number: "))
# match numbers:
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case 3:
#         print("three")
#     case 4:
#         print("four")
#     case 5:
#         print("five")
#     case _:
#         print("no match")

Browser = str(input("please mention your browser\n"))
#Browser = Browser.lower()
match Browser:
    case "Chrome":
        print("Chrome is being invoked")
    case "Firefox":
        print("Firefox is being invoked")
    case _:
        print("no match")

# http_status_code = int(input("Please input the HTTP status code: "))
# match http_status_code:
#     case 200:
#         print("Success")
#     case 400:
#         print("Bad Request")
#     case 404:
#         print("Not Found")
#     case 500:
#         print("Internal Server Error")
#     case _:
#         print("Unknown Error")
# if-elif-else ladder
# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

# age = int(input("Please input your age: "))
# if age==0 or age<0:
#     print("You can't watch")
# elif 0<age<=3:
#     print("Ticket price : Free")
# elif 3<age<=10:
#     print("Ticket price : 150")
# elif 10<age<=60:
#     print("Ticket price : 250")
# else:
#     print("Ticket price : 200")
