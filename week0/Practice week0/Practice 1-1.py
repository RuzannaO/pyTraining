#the program changes vowels in a list with the same vowels in inverse order

def vowelsSwap(word):

#the following function swaps letters in a list - list[a] swaps with list[b], a and b are int
   def swap(list, a, b):
        temp = list[a]
        list[a] = list[b]
        list[b] = temp

        return list

   vowels = "aoiueAUOIE"

   word_list = list(map(str, word))

   j = len(word_list) - 1

   for i in range(0, len(word_list) // 2):
       if word_list[i] in vowels:
           while word_list[j] not in vowels:
               j = j - 1
           new_list = swap(word_list, i, j)
           j = j - 1

   return "".join(new_list)

print(vowelsSwap("AAmerica"))


