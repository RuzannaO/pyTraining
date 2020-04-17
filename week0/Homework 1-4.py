# calculate sum of input digits with for loop
def sum1(x):
    s=0
    for i in x:
        s+=int(i)
    return(s)

print(sum1(str(input())))

# the same task w/ "competition"
def sum_dig(a):
    return (sum(list(map(int,str(a)))))

print(sum_dig(168))
