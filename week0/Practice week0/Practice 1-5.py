
def bigger_factorial(number):

    result = 1
    i = 1
    while (result < number):
        result = result * i;
        i = i + 1

    return(result)

print(bigger_factorial(int(input())))
