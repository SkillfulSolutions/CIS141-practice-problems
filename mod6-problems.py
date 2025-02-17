#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
[ 2, 5, 6, 7, 9, 10 ]
print(sum([ i for i in [ 2, 5, 6, 7, 9, 10 ] if i % 2 == 0 ]))

#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
list = [ "bacon", "Olympic", "test", "purple", "chocolate", "rain", "Olympic" ]
keyword = "Olympic"
count = list.count(keyword)
print(count)

#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters.
#   Print the resulting filtered list.
list = [ "bacon", "bed", "test", "purple", "chocolate", "rain", "pat" ]
for s in list:
    if len(s) > 3:
        print(s)

#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
list = [ -1, -3, 4, -2, -6, -5, 7, 9, -8 ]
pos_list = [ i for i in list if i > 0 ]
neg_list = [ i for i in list if i < 0 ]
print("There are", len(pos_list), "positive numbers and", len(neg_list), "negative numbers.")

#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list.
#   Print the new list.
list = [ -1, -3, 4, -2, -6, -5, 7, 9, -8 ]
new_list = [ i**2 for i in list ]
print(new_list)
