
def implications3(a,b,c):

    if a == 0:
        result = True
    else:
        if b == 0:
            result = True
        else:
            if c == 1:
                result = True
            else:
                result = False

    return result

def expr_value(a):
    def split_numbers(a):
        signs = "+-*/"
        signs_list = []
        res = []
        for i in (a):
            if i in signs:
                signs_list.append(i)
                a = a.replace(i, "x")
        new_list = a.split("x")
        for i in range(len(new_list) - 1):
            res.append(new_list[i])
            res.append(signs_list[i])
        res.append(new_list[len(new_list) - 1])
        return (res)

    def split_by_plus(init):
        res = []
        a = "".join(init)
        pluses = []
        for i in a:
            if i == "+":
                pluses.append(i)
            else:
                if i == "-":
                    pluses.append(i)
        for i in a:
            if i == "+" or i == "-":
                a = a.replace(i, "#")

        a = a.split("#")
        for i in a:
            if i != "#":
                res.append(i)
        return (res, pluses)

    def fin_oper(a):
        a = split_numbers(a)
        b = []
        s = 0
        if len(a) == 1:
            return int(a[0])
        for i in range(1, len(a) - 1, 2):
            if a[i] == "*":
                s = int(a[i - 1]) * int(a[i + 1])
                a[i + 1] = s
            else:
                s = int(a[i - 1]) / int(a[i + 1])
                a[i + 1] = s
        b.append(s)
        return s

    prodd, pluses = split_by_plus(split_numbers(a))
    for i in range(0, len(prodd)):
        prodd[i] = fin_oper(prodd[i])
    s = prodd[0]
    for i in range(0, len(pluses)):
        if pluses[i] == "+":
            s = s + prodd[i + 1]
        if pluses[i] == "-":
            s = s - prodd[i + 1]
    return(f'{s:.2f}')

print(expr_value("6-5*4/3+3-2*4"))



def quick_or (a):
    return len(list(filter(lambda x: x==False, a)))!=len(a)
    
    
def is_polindrome(a):
    set_a = set(a)
    counter = 0
    for i in set_a:
        if a.count(i)%2==1:
            counter+=1
    if counter>1:
        print(counter,"counter")
        return False
    else:
        return True
    
    
def last_digit(a):
    b = a % 20
    return round((b*(b + 1) * (2 * b + 1) / 6) % 10)
