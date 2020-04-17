def my_funct(a, b):
    def remove_dublicates(m):
        return[m[x] for x in range(len(m)) if m[x] not in m[x+1:]]

    new_string2 = remove_dublicates(b)
    c = ""
    for i in new_string2:
        if i in a:
            c += i * a.count(i)

    return c


string1 = "abaabbccabbed"
string2 = "bedac"
print(my_funct(string1, string2))
