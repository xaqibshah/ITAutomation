
# def int_username(username):
#     if len(username) < 6:
#         print("Username must be at least 6 characters long")

#     else:
#         if len(username) > 15:
#             print("Username is too long, Must be less then 15 characters")
#         else:
#             print("Username is valid")


# int_username("xaqibshah123424")

def hint_username(username):
    if len(username) < 6:
        print( "Username must be at least 6 characters long")
    elif len(username) > 15:
        print( "Username is too long, Must be less then 15 characters")   
    else:
        print ("Username is valid")

hint_username("xaqibshah1234240")

def is_even(num):
    if num % 2 == 0:
        return True
    return False


answer = is_even(10)

#Sprint(answer)

