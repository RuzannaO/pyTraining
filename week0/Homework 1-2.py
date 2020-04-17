#a/ delete dublicates in a list   w/ for loop

a=[[1,2], [1,2], [1,2,3]]
result=a[0:1]
for i in a[1::]:
    if i not in result:
        result.append(i)
print(result)


#b  delee dublicates in a list   w/ list comprehension

print( [x for i, x in enumerate(a) if i == a.index(x)])


#c/ delete dublicates in a list   w/  competition

#1 example
def del_dubs1(a):
    return([x for i, x in enumerate(a) if i == a.index(x)])


#2 example
def del_dubs(a):
    res = []
    [res.append(x) for x in a if x not in res]
    return(res)


print(del_dubs(a))

print(del_dubs1(a))



del_dubs(a)

del_dubs1(a)







