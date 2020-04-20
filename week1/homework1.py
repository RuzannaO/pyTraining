def all_positive(*args):
    return len([x for x in args if x<0])>=1



def xor (a,b,c):
    return c and ((not a and not b) or (a and b)) or not c and((not a and b) or (a and not b))

def mirror_string(a):
    b = ""
    for i in a:
        if ord(i) <= 122 and ord(i) >= 97:
            b = b + chr(122 - (ord(i) - 97))
        else:
            if ord(i) <= 90 and ord(i) >= 65:
                b = b + chr(90 - (ord(i) - 65))
            else:
                b = b + i
    return(b)


def binary_sum(a,b):
    return(int(a,2)+int(b,2))


discriminant2=lambda a,b,c: b**2-4*a*c

full_name=lambda list1,list2: list1 + " " +list2

print(xor(0,0,0))
print(xor(0,0,1))
print(xor(0,1,0))
print(xor(0,1,1))
print(xor(1,0,0))
print(xor(1,0,1))
print(xor(1,1,0))
print(xor(1,1,1))





print (all_positive(-1))
