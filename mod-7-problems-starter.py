'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
Test: aeiou (5), mississippi (4), test (1)
Input: string (s)
Output: integer (int)
Function body: lowercase s, for in s add one to count, return count, print count()
'''
'''
def count_vowels(input):
    lower_input = input.lower()
    vowels = "aeiou"
    count = 0
    for i in lower_input:
        if i in vowels:
            count += 1
        if i == "y":
            print("sad sometimes y")
    return count

print(count_vowels("test"))
'''

'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
Test: racecar (True), Racecar (True), pokemon (false)
Input: string (s)
Output: boolean
Function body: lowercase s, flip s, save to new variable (flipped_s), compare s & flipped_s
'''
'''
def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return lower_s == flipped_s

print(is_palindrome("raCecar"))
'''
'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
Test: ("Water", "Fire"))  # "Super Effective"; ("Fire", "Water"))  # "Not Very Effective"; ("Electric", "Grass"))  # "Neutral"
Input: tuple, two strings
Output: strings: "Super Effective", "Not Very Effective", or "Neutral"
Function body: lower case, if a return super, elif b return not, else return neutral, print
'''
'''
def type_advantage(attacker, defender):
    attacker = attacker.lower()
    defender = defender.lower()
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "fire" and defender == "water":
        return "Not Very Effective"
    else:
        return "Neutral"

print(type_advantage("Water", "Fire"))  # "Super Effective"
print(type_advantage("Fire", "Water"))  # "Not Very Effective"
print(type_advantage("Electric", "Grass"))  # "Neutral"
'''

'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
Test: 70, y (15); 70, n (5); 20, y (20); 20, n (10); 10 (0)
Input: tuple: int, s
Output: int
Function body: prompt for user's age, if under 18 vehicle n, else prompt for vehicle, sum cost, return cost, print
'''
'''
def ferry_fare(age, vehicle):
    cost = 0
    if age <= 18:
        cost += 0
    elif age <=64:
        if vehicle == "n":
            cost += 10
        else:
            cost += 20
    else:
        if vehicle == "n":
            cost += 5
        else:
            cost += 15
    return cost
while True:
    number = int(input("How old are you? "))
    if number <= 18:
        car_status = "n"
        break
    else:
        car_status = input("Are you taking a vehicle onto the ferry? (y/n) ")
    break

print(ferry_fare(number, car_status))
'''
'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
# test: 0 (1), 99 (1), 100 (2), 199 (2), 200 (3)
# input: experience points
# output: level
# function body: prompt for user exp, if in range(0,99) return 1, elif in range(100-199) return 2, else return 3
'''
def level_up(experience):
    level = 0
    if experience in range(0,99):
        level += 1
    elif experience in range(100,199):
        level += 2
    else:
        level += 3
    return level

print(level_up(110))
'''
