def all_positive(*args):
    s=1
    for i in args:
        s=s*i
        print(s,i)
    return not (s+abs(s))




def xor3 (a,b,c):
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


def bit_concat(a):
    new_list = [f'{x:08b}' for x in a]
    result = []
    for i in range(0, len(new_list)):
        result.append((new_list[i])[len(new_list[i])-2*i-2:len(new_list[i])-2*i])
    result.reverse()
    return int("".join(result), 2)


def binary_sum (a,b):
    return(int(a,2)+int(b,2))


def only_names(a):
    i=0
    while i<len(a):
        if len(a[i])==0:
            a.remove(a[i])
        i=i+1
    return a


discriminant=lambda a,b,c: b**2-4*a*c


full_name=lambda list1,list2: list1 + " " +list2


