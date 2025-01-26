# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
user_word1 = input("Please enter a word. ")
user_multiplier = int(input("How many times would you like that word repeated? "))
print(" ".join([user_word1] * user_multiplier))

#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
user_name = input("What is your name? ")
user_age = int(input("How many years old are you? "))
user_age_next_year = (user_age + 1)
print("Hello, " + user_name + "! ")
print("You are " + str(user_age) + " years old. Next year, you will be " + str(user_age_next_year) + " years old.")

#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
user_sentence1 = input("Please enter a sentence. ")
user_word1 = input("Please enter a word. ")
count = user_sentence1.count(user_word1)
print("The word " + user_word1 + " is found " + str(count) + " times in that sentence.")

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
user_word1 = input("Please enter a word with three or more syllables. ")
user_number1 = int(input("Please enter a whole number less than 4. "))
user_number2 = int(input("Please enter a whole number less than 7. "))
print(user_word1[user_number1:user_number2])

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
print("|".join(["Bacon"] + ["is"] + ["awesome!"]))
