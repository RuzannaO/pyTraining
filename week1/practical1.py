
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
  
