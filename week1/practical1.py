
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
  
def quick_or (a):
    return len (list (filter (lambda x: x==False,a))) > 0
    
    
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
    
    
def last_digits(a):
    b = a % 20
    return round((b*(b + 1) * (2 * b + 1) / 6) % 10)
