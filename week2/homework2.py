from collections import defaultdict


def bisec(a,x=0):
   if x==1:
       return a[len(a)//2: ]
   else:
       return a[0:len(a)]


def bisect_position(a,n):
    if (len(a)==0) or n <= a[0]:
        return 0
    if n >= a[-1]:
        return len(a)
    if len(a) == 2:
        if n >= a[0] and n < a[1]:
            return 1
    if n >= a[len(a)//2] and n < a[len(a) // 2 +1]:
        return len(a)//2+1
    else:
        if n <= a[len(a)//2]:
            return bisect_position(bisec(a[0:len(a)//2+1]), n)
        else:
            return bisect_position(bisec(a, 1), n)+len(a)//2



def pair_sums(i,m):
   return (i,m-i)

def all_sums(n):
    list=[]
    for i in range(1, n//2+1):
        list.append(pair_sums(i,n))

    return list

def dublicate_characters(a):
    d=defaultdict(int)
    for i in a:
        if a.count(i)>1 and i!=" ":
            d[i]=d[i]+1

    if len(d)==0:
        return dict(d.keys())
    else:
        return set(d.keys())


def compare_lists(a,b):
    a_dic=defaultdict(int)
    b_dic=defaultdict(int)


    for i in a:
        a_dic[i]=a_dic[i]+1
    for i in b:
        b_dic[i]=b_dic[i]+1
    if a_dic==b_dic:
        return True
    else:
        return False


def swapp(a,i,j):
    if a[j]<=a[i]:
        k=a[i]
        a[i]=a[j]
        a[j]=k
    return a
def roundd(n):
    return round(n+0.1)

def heapq(a,n):
    a.append(n)
    j = len(a)-1
    while j>0:
        if a[j] >= a[roundd(j / 2 - 1)]:
            return a
        else:
             swapp(a, roundd((j / 2) - 1), j)
             j = roundd (j-j/2-1)
    return (a)


def sort_list(a,b="ascending"):
    new_list = []
    if b=="descending":
        for i in range(0, len(a)):
            print(len(a),"lenA")
            new_list.append(max(a))
            a.remove(max(a))
        return new_list
    else:
        new_list = []
        for i in range(0,len(a)):
            new_list.append(min(a))
            a.remove(min(a))
        return new_list

print(compare_lists([1,1,5,4,2,1,2], [5,1,1,2,4,1,2]))

print(dublicate_characters("here we have some duplicates"))
