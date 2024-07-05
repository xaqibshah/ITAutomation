string1 = 'Greetings, Earthlings'

print(string1[0])
print(string1[4:8])
print(string1[11:])
print(string1[:5])

print(string1[-5:])
# print(string1[55:])

string2=  'thequickbrown'
print(string2[0::2])

numstring = "123456789"

print(numstring[1::])

phonenum = '2025551212'

area_code = "(" + phonenum[ :3] + ")"
print(area_code)
exchange = phonenum[3:6]
print(exchange)
line = phonenum[-4:]
print(line)

print(area_code + " " + exchange + "-" + line)


def format_phone(phonenum):

    area_code = "(" + phonenum[ :3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line


print(format_phone('2211445578'))