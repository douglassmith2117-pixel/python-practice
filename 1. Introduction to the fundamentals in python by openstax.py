# what ive learned from openstacks book on python programming 

#1.1 hello world

#print ("hello world!")
#print("what is your favourite song?")

#Basic intro ,you can undo the comments to re access what youve practiced on
#song = input("What is your favourite song?" )
#print("Cool! i like", song , "too!")
  
#1.2 : input and output 

"""print("Today is a friday i guess " , end = "")
print("no wait" , " its a saturday not a friday" , sep = "just kidding ")"""

"""print("I shall be telling this " , " a sigh" , sep = "with")
print("Somewhere ages " , " ages hence:" , sep = "and")
print("Two roads diverged " , " a wood, and I--" , sep = "in")
print("I took the one less traveled by,")
print("And that made " , " the difference." , sep = "all")"""

"""name = input("What is your name?: ").capitalize()
preffered_act = input("What do you like?: ").capitalize()
print(f"{name} likes {preffered_act}")"""

#1.3 Variables 
"""
team_1 = "Liverpool"
team_2 = "Chelsea"

score_1 = 2 
score_2 = 3

print(f"{team_1} versus {team_2}")
print(f"Final score :{score_1} to {score_2}")
"""
#1.4 Strings (data type ; string)
"""
number_1 = str(260973216390)
number_2 = str(260771268794)
number_3 = number_1 + number_2

print(len(number_3))"""

"""first_name = input('what is your first name?')
sir_name = input('what is your sir name?')

print(f'Your first name which is {first_name}, has {len(first_name)} letters.')
print(f'Your sir name which is {sir_name}, has {len(sir_name)} letters.', end ='')
print(f' Which makes a total of {len(first_name + sir_name)} letters.')"""

"""name = input('what is your name?')
feeling = input('what are you feeling?')

print('Hi', name , end = '')
print(', I hope you\'er feeling' ,feeling)"""

 #1.3 Number basics (data type ; intergers and floats)


print(2**4)
"""
import math

One_degree = math.pi / 180
users_degree = float(input('Type in an angle you want to convert:'))

def degrees_to_radians():
    result = One_degree * users_degree
    return result
        
print(f'{users_degree} degrees is equal to {degrees_to_radians()} Radians.')"""

""""
int_a = 16
float_a = 78.0
string_a = '39'

print(type(int_a) ,type(float_a) ,type(string_a))

meters = 10
meter2feet = 3.28
feet = meters * meter2feet

print(feet)""" 
'''
name = input('what is youer name?:')
print(f"Good morning {name},I hope you are doing great today.")

response = input('Are you ready to code today? (yes or no )').capitalize()

if response == 'Yes':
    print("Thats wonderfull, you can gladly begin!!!")
elif response == "No":
    print("well then, you can always come back when you are okay right")
'''
# 1.6 error messages 

"""print hello world    # feel free to identify the types of errors and correct them
name = 'Harry'
print('hi', Name)
 print('how are you?)
"""

# 1.7 Comments "im farmiliar with this , but why not go through it again?"
#yeah there wasnt much to do here

# 1.8 was pythons popularity and historical background in which i took some points in my physical notebook

# 1.9 summary practice

# 1.9.1 fun facts 
"""
print('Hello, welcome to todays fun facts about numbers.')

number = float(input("Enter any number of your choice:"))
number2 = float(input("Enter another number you would like to add and subtract from your first number: "))

def square_operator():
    result = number ** 2
    return result

def cube_operator():
    result = number ** 3
    return result

def one_tenth_operator():
    result = number / 10 
    return result

def add_operator():
    result = number + number2
    return result

def sub_operator():
    result = number - number2
    return result

print(f"{number} squared is {square_operator() }", "\n"
    f"{number} cubed is {cube_operator()} " ,"\n"
    f'One tenth of {number} is {one_tenth_operator()}', "\n "
    f'{number} plus {number2} is {add_operator()}', "\n"
    f"{number} minus {number2} is {sub_operator()}")
"""

# 1.9.2 Mad lib 

"""This is a game (mad lib) in which random adjectives and nouns are used in  pre written sentences to make it
 sound funnier.it is played by two people in which they take turns giving different nouns and adjectives to keep 
 the game funnier and on going."""

print ("Welcome to the mad lib.")

 # An adjective is a word that makes a noun more detailed , eg a black sphere
'''
adjective1 = input ("Give me one adjective: ") .capitalize() 
adjective2 = input("Give me another adjective: ").capitalize()
noun1 = input("Give me a noun: ").capitalize()
noun2 = input("Give me another noun:").capitalize()

print(adjective1 , 'place with your ' , adjective2 , 'family.' \
'Usually you go to some place that is near a/an ' , noun1 , 'or up on a/an' , noun2, '.')
print(f"A vacation is when you take a trip to some {adjective1} place with your {adjective2} family.")
print(f"Usually you go to some place that is near a /an {noun1} or up on a /an {noun2}.")
'''



