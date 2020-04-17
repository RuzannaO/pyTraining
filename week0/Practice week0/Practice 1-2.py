#the program is counting number of common symbols in a given array
#it returns 2 values, first, common symbols without considering repetition
#second, considering repetition

# in this part the program constructs a new list - "result", which contains the common symbols
# the length of the "result" list is the number of common elements
def count_commons(initalArray):
    result = []
    d = set("".join(map(str, initalArray)))

    for i in d:
        counter = 0
        for j in initalArray:
            if i in j:
                counter = counter + 1
        if counter == len(initalArray):
            result.append(i)
        else:
            counter = 0



    #in the folowing part the program constructs a new list "result1". This list is filled in by
    # the number of each element from the "result" list in the initial list items,
    # Min(result1) shows how many times each element is seen in the initial list.
    #summing up all min(result1) figures we get the number of common elements (considering repetition)

    result1 = []
    counter2 = 0
    for i in result:
        for j in initalArray:
            result1.append(j.count(i))

        counter2 = counter2 + min(result1)
        result1 = []


    return (len(result),counter2)

test_array=["abab", "baab", "aaabb"]

print(count_commons(test_array))

