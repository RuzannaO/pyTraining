def com_div(a,b):
     if  a%b==0:
          return b
     else:
          return com_div(b, a % b)

print(com_div(120,50))
