# check if two lists are in cyclic order

def cycl(a,b):
    c = "".join(map(str, 2 * a))
    d = "".join(map(str, b))
    return(d in c)

a=[1, 3, 4, 5, 2]
b=[5, 2, 1, 3, 4]


print(cycl(a,b))