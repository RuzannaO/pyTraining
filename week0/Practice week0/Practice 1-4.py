def factr(num):
    result=1
    for i in range (1,num+1):
        result=result*i
    return(result)


def factr1(num):
    if num==1 or num==0:
        return(1)
    else:
        return(num*factr1(num-1))


print(factr(int(input())))
print(factr1(int(input())))

