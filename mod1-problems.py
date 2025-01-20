# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
import math
num1 = int(input("Pick a number. "))
num2 = int(input("Pick a second number. "))

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
import math
print("There is a triangle. How long are its sides?")
a = int(input("Pick a number. "))
b = int(input("Pick another number. "))
c = int(input("Pick yet another number. "))

s = (.5*(a+b+c))
print ("The triangle's area is", ((math.sqrt(s*(s-a)*(s-b)*(s-c)))))

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import math
num1 = float(input("Pick a number. "))
num2 = float(input("Pick a second number. "))
num3 = float(input("Pick a third number. "))
num4 = float(input("Pick a fourth number. "))
num5 = float(input("Pick a fifth number. "))

numbers = [num1, num2, num3, num4, num5]

total = sum(numbers)
average = total/5
range = ((max(numbers))-(min(numbers)))
diff_avg = (((num1-average)**2)+((num2-average)**2)+((num3-average)**2)+((num4-average)**2)+((num1-average)**2))
std_dev = math.sqrt((diff_avg/5))

print("Statistics:")
print("Total:", total)
print("Average:", average)
print("Minimum of range:", (min(numbers)))
print("Maximum of range:", (max(numbers)))
print("Range:", range)
print("Standard deviation:", std_dev)
