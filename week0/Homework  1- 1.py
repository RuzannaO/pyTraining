#remove all elements from a list that are equal to given element   / using remove method

m=[[1, 2], [1, 2, 3], [1, 2]]
l=[1.2]
copy_list=m.copy()
for i in m:
    if i == l:
        copy_list.remove(i)

print(copy_list)

#remove all elements from a list that are equal to given element   / using list comprehension


print([x for x in m if x!=l])




