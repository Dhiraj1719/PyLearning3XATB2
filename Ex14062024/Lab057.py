# example to use function
# def allowd_to_class(name, password):
#     if name == "Dhiraj":
#         if password == "Yes":
#             print("you are allow to class")
#         else:
#             print("you are not allow to class")
#
#
# allowd_to_class("Dhiraj", "No")


def Allowed_to_class(name):
    match name:
        case "Dhiraj":
            print("you are allow to class")
        case "Bhavana":
            print("you are allow to class")
        case _:
            print("you are not allow to class")

Allowed_to_class("arnav")