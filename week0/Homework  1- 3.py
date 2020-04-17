# a/ check if a string is symmetrical w/ for loop

a="aabbbbaa"

indicator = 1
for i in range (0, len(a)//2):
     indicator = indicator*(a[i]==a[len(a)-1-i])

print(indicator == 1)

# b/ the same task - short

print(a[::]==a[::-1])


# b/ another way

print(not [(a[i]) for i in range(0,len(a)//2) if a[i]!=a[len(a)-1-i] ])






