x = 0
while x < 5:
    print("Not there yet", x)
    x = x + 1
print("x " + str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x +=1
    print("Done")

attempts(5) 

def get_username(username):
    return username

# error code
# username = get_username("xaqib")

# while not valid_username(username):
#     print("Invalid username")
#     username = get_username()

