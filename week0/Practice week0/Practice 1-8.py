#get the second max

def sec_max(a):
     if len(set(a))<=1:
          return(0.5)
     return(sorted(list(set(a)))[-2])


k=[1,1,1,2,6]

print(sec_max(k))

