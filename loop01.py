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



for x in range(5):
    print(x)

friends = ['Nadir', 'Iname', 'Shahrukh', 'Danish']
for friend in friends:
    print("Hello " + friend)


values = [24,53, 68,99,35]
sum = 0
length = 0

for value in values:
    sum += value
    length += 1
print("Total sum: " + str(sum) + " Average: " + str(sum/length))



for n in range(1,5,6):
    print(n)


for n in range (0,11,2):
    print(n)


for n in range (2, 7+1):
    print(n *3)

for n in range (2, -2, -1):
    print(n)
    
for x in range(25):
    print(x)
friends = ['ahmed', 'nadir', 'Danish', 'Shahrukh', 'inam']


def friend_greeting (friends):
    for friend in friends:
        print("Hello " + friend + "!")


friend_greeting(friends)

