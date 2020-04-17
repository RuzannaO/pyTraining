my_list=[101, 110, 220, 100, 103, 606, 603]

for i in my_list:
    new_list=[]
    if (len(set(str(i))))==len(str(i)):
        print(i)
        new_list.append(i)
        break
if  not new_list:
    print(-1)
