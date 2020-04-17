#the program creates a dictionary telling the number of words in a frase

#function changing a string to a list
def str_to_list(a):
    return(a.split(" "))


#function removing punctuation
def rem_puntuation(a):
     puncts_list="?!,:.'"
     for i in a:
         if i in puncts_list:
               a=a.replace(i,"")
     return(a)

my_txt="What is this book about? This book is about python coding"

# it makes all lower case
my_txt_low=my_txt.lower()

#creates dictionary

d=str_to_list(rem_puntuation(my_txt_low))
dict1={}
for i in d:
    dict1[i]=d.count(i)
print(dict1)
