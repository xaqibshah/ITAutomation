my_variable = 2

while my_variable < 10:
    print(my_variable, "Hello")
    my_variable += 1


x = 1 
sum = 0

while x <10:
    sum = sum + x
    x = x + 1

product = 1
while x < 10:
    product = product * x
    x = x + 1

print("Sum", sum)
print("Product", product)


def count_factors (given_num):
    count = 1
    factor = 1
    if given_num == 0:
        return 0
    while factor < given_num:
        if given_num % factor == 0:
            count += 1
        factor += 1
    return count


print(count_factors(0))
print(count_factors(10))
print(count_factors(11))
