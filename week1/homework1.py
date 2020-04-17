def all_positive(*args):
    return len([x for x in args if x<0])>=1



def xor (a,b,c):
    return c and ((not a and not b) or (a and b)) or not c and((not a and b) or (a and not b))


print(xor(0,0,0))
print(xor(0,0,1))
print(xor(0,1,0))
print(xor(0,1,1))
print(xor(1,0,0))
print(xor(1,0,1))
print(xor(1,1,0))
print(xor(1,1,1))

print("*******************")


print("*******************")




print (all_positive(-1))