#  3.1 Strings revisited
"""
s = "Python"
print(s[0] + s[-5]) """

# Unicode
"""
print(ord("D")) # The ord function converts a character to a unicode
print(chr(78)) # The chr function converts a unicode into a character"""
"""
print(ord("n") , ord("A"))
print(ord("0")) # The ord and chr functions are only applicable to string objects and not integers ,well at least as far as i know
print(chr(126))
"""
# Special characters
'''
print("Hello \n douviq") # We are familiar of this but for explanatory sake, it creates a new line character, Usefull in paragraphing 
print("Hello\tdouviq") # This one is a new one and it is usefull in indenting paragraphs or long sentences
print('how was you\'er day today?') # The backslash is a classic but it is used to ignore the backslash and fun fact, it can ignore itself 
'''

# Hopper quote
"""
print("To me Programming is more than practical art.", "\n" 
       "It is also a gigantic undertaking in the foundations of knowledge. \n \t --Grace Hopper")
"""

# Shift cipher 2.0
"""
word = input("Enter a three letter word:")
shift = int(input("How many letters to shift by?:"))

shifted_keys = (ord(word[0]) + shift, ord(word[1]) + shift, ord(word[2]) + shift)

shifted_word = str(chr(shifted_keys[0])) + str(chr(shifted_keys[1])) + str(chr(shifted_keys[2]))

print(f"The shifted word is {shifted_word}")

"""

# 3.2 Formatted strings .  Yeah this might be a piece of cake if you ask me
"""
name = "Douviq"
print(f"Hello {name}")
"""
# Formatting numbers
'''
number =  2244408256
print(f"{number:d}") # The default way of fomating an integer 
print(f"{number:,d}")# separates integers by the character placed in which you can alter to your liking
print(f"{number:10d}")# Makes sure that a character is of 10 digits by adding spaces if its less 
print(f"{number:020d}")# Makes sure a character is of 20 digits by adding zeros instead of spaces'''
'''
import math

print(f"{math.pi:f}")# Formats to six decimal places basically the default ways of the object
print(f"{math.e:.4f}")# Formats to four decimal places ,in which i can adjust to my liking
print(f"{math.pi:8.4f}")# Formats to four decimal places of eight characters wide with spaces
print(f"{math.pi:08.4f} , \n")# Formats to four decimal places of eight characters wide,with zeros instead of spaces
# the round function also rounds of this the first argument being the number you wannna round off and the second argument being the decimal 
# place you want it to be rounded off to

# Mad lib (f string practice)

print("THE MAD LIB", "\n")

name = input("Enter a name:")
noun = input("Enter a noun:")
adj = input("Enter an adjective:")
verb = input ("Enter a verb ending in -ing:")

print(f"{name}, the {adj} {noun}, likes to go {verb}.")'''

# Wage calculator
"""
print("Welcome to wage calculator. \n")

starting_hr = int(input("Starting hour:"))
starting_min = int(input("Starting minute:"))
stoping_hr = int(input("Stoping hour:"))
stoping_min = int(input("Stoping minute:"))
hourly_rate = int(input("Hourly rate:"))

hour = stoping_hr - starting_hr
minute = abs(stoping_min - starting_min)
abv_min = minute / 60 # make sure that the minute is abbreviated eg 1.5 hours(This is how we get the .5)
payment = hourly_rate *  (hour - abv_min)


print("\n"
       f"Worked {starting_hr:02d}:{starting_min:02d} to {stoping_hr:02d}:{stoping_min:02d} \n"
       f"Total hours:{hour - abv_min:.2f} \n"
       f"Payment:${payment}")
"""
# 3.3  Variables revisted
"""
message = "Hello" # this is the most basic of examples but the value is sometimes know as the object and the variable is the reference
number = 9870
Boolean = True

print(id(message))# this gave me an integer which represents a memory location
print(type(message))

print(id(number))
print(type(number))

print(id(Boolean))
print(type(Boolean))
"""
























# 3.4 List Basics
"""
colours = ["violet" , "purple", "Blue", "Black", "green" , "Red"]
fruits = ("Grapes", "Strawberries", "berries", 'apples')
fruits = list(fruits) # yeah on this one i may have forgotten on how to make a list explicitly

# Used indexes to acess the items of our lists
print(f"my favourite kind of fruit with out a doubt must be {fruits[0]}, i also like the {colours[1]} it has, that to is a favourite color."
      f"The next fruit i tend to prefer are {fruits[3]} which have a sort of {colours[4]} to them, {colours[2] + fruits[2]} are kinda nice"
      f" too you know, some are {colours[0]} or {colours[3]} {fruits[2]}.And we come to the last but not the least, {fruits[1]}, which start"
      f" out {colours[4]} as they are little but grow to be a big, juicy {colours[5]}-{colours[0]} kinda fruit.")"""

# List basics
"""
# Lists are a set of mutable unodered objects that do not allow duplicates
numbers = [2, 23, 39, 6, -5]
numbers[2] = 35

print(numbers)
print(len(numbers))
"""

# 3.5 Tuple basics  

# Tuples are a set of immutable ordered objects that allow duplicates
"""
checklist = (3, 'bread', "milk", "eggs", "cheese", 4.5, ["bananas", "grapes", "berries",])

print(checklist[6])
print(checklist)  
print(len(checklist))

# Creating a tuple with user input

my_data = ( input(), input(), int(input()), int(input()))
print(f"my_data:{my_data}")"""