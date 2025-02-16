
#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
n = int(input("Enter a positive number: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(sum)

#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. Convert each character to uppercase before printing.
string = "Bacon"
for i in string:
    print((i).upper())

#3. Use a for loop and the range() function to print all even numbers from 2 to 20.
for i in range(2,22,2):
    print(i)

#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Example output:

# 1   2   3   4   5
# 2   4   6   8   10
# 3   6   9   12  15
# 4   8   12  16  20
# 5   10  15  20  25
num = range(1,6)
for n in num:
    for m in num:
        print(n*m, end="\t")
    print()

#5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered. Sample interaction:
'''
Enter a number (0 to stop): 4
You entered 4
Enter a number (0 to stop): 7
You entered 7
Enter a number (0 to stop): 0
Exiting...
'''
string = "y"
while string == "y":
    num = int(input("Please enter a number. Enter 0 to exit.\n"))
    if num == 0:
        break
    else:
        print("\nYou entered",num,".")
        print()
        print()
