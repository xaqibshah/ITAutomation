def area_of_triangle(base, height):
    return base*height/2

a_area = area_of_triangle(10, 5)
b_area = area_of_triangle(20, 10)

sum = a_area + b_area

#print("The sum of the areas of the two triangles is: ", sum)


#print(7//2)   3
#print(8//2)   4


def convert_second(seconds):
    hours = seconds//3600
    minutes = (seconds%3600)//60
    remaining_seconds = seconds%60
    return hours, minutes, remaining_seconds


hours, minutes, seconds = convert_second(7600)
#print(hours, minutes, seconds)



#name = "Saqib"
#number = len(name) * 9
#print("Hello " + name + ". Your lucky number is " + str(number))

def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))


lucky_number("saqib")
lucky_number("ali")


