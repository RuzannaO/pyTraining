#find a missing number
a=[1,2,3]

print(int(((len(a)+1)/2)*(2+len(a))-sum(a)))


#another solution

my_list=[]
for i in range(1,len(a)+2):
     my_list.append(i)

print(list(set(my_list)-set(a))[0])
