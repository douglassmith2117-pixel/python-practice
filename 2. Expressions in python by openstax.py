# 2.1 The python shell   
"""  
x = 5
3 * x - 5
3 * (x - 5)
x
type(1)
type("2")
len('hello')
str(2)
int('3')
print(round(9.97))
print(abs(-89))
"""
# 2.1.2 correcting mistakes

x = 123
y = 456

#feel free to correct the errors and leave it flawed as you found it
"""
print("Easy as ", X)   
print("y divided by 2 is ", y / 0)

name = input("what is your name ?")

print(name,"is",int(name), "letters long.")
print("That's all folks!)
"""

# 2.2 Type conversion
"""
x = 4.9
y = int(x)
z = round(x)

print(type(z))
print(y)"""

#Grade average
"""
exam_1 = float(input('Enter grades from the first exam:'))
exam_2 = float(input('Enter grades from the second exam:'))
exam_3 = float(input('Enter grades from the third exam:'))

def average():
    result = (exam_1 + exam_2 + exam_3) / 3 
    return result
 

print(int(average()))
print(float(average()))"""

# Cups of water 2.0
'''
print('Welcome to Hydration stats!', "\n") # A program that tracks how much water the user has drank based on user input 

daily_goal = float(input("Enter the number of cups of water you want to drink today as your daily goal.(6 - 8 cups recommended):"))
cups_drank = float(input("Enter the number of cups of water you've drank today:")) # These variables help track and compute certain info the user needs to know

ounces = cups_drank * 8 # since 1 cup is 8 ounces
cups_left = daily_goal - cups_drank                                                                                                                                                                 

print("\n",
     f"The amount of ounces of the cups of water you drank are equal to  {ounces} ounces. ", "\n" # This block diplays the output through explicit joining using one print statement
      f"You have drank {cups_drank} cups today, "
      f"You have {cups_left} cups left out of {daily_goal} cups. Daily goal {round((cups_drank/daily_goal) * 100)}% complete.")
'''
# Product as float
"""
x = int(input("Enter the first integer: "))
y = int(input('Enter the second interger: '))
z = float(x * y)

print(f'The product of the first and second integer is {z} , {type(z)}')
"""

# 2.3 Mixed data types

"""print("Keep out of my room!!!" * 3)"""  # Intresting to see the * operator work this way, only works between ints and strs but not floats

# After the point

"""print(f"{0.2 : .30f}") , # This needs further explanation, copilot can help
num = '2'
nums_beyond_decimal = input("Enter a number :")

print(num + '.' + nums_beyond_decimal)"""

# Print n times 
"""
str_1 = "Red "
str_2 = "John"
count = 5

print((str_1 + str_2 +  "\n"  )   * count )
"""

# 2. 4 Floating point errors
    # Hmmm
"""
print(8.0 ** 7286)  # Overflow errors caused by storing floats that are too large or to small(outside a range perhaps)
print(8.9 ** 4)   
"""
# Round function
"""
number = 6.6626

print(round(number,3)) # Its pretty cool that it has a second argument to actually choose which decimal place to round it to, i never knew of that
print(round(3.5,2) # Oh and by the way ,the round function fixes floating point errors)"""
 
# Inaccurate tips 
"""
bill = 33.33
tip_ratio = 0.20
tip_amount = tip_ratio * bill

print(f"The tip is {round(tip_amount ,1)} dollars")

#  Calculate the area of a triangle
#  
print("Welcome to calculating the area of a triangle.")

base = float(input(f"Enter the base of your triangle:"))
hieght = float(input(f"Enter the hieght of your triangle:"))

def area_of_triangle():
    result = (base * hieght) / 2
    return result

print(f"The area of your triangle is equal to {round(area_of_triangle() , 1)} cm squared.")
print(f"The area of your triangle is equal to {round(area_of_triangle())} cm squared.")

#print(type(base), type(hieght))
"""

# 2.5 Dividing integers

# Unit conversions 
"""print(f"1 meter is {193 // 100}")
print(f"93 Centimeters is {193 % 100}")"""

# Arrival time 2.5
"""
print("Hello, welcome to arrival time, a program that estimates your arrival"  # I think the print statment is evaluating enough
      " depending on your current time and how long your trip will take.", "\n")

current_hour = int(input("What is the current hour(0 - 23)?:"))
current_minute = int(input("What is the current minute(0 - 59)?:")) # User input, stored in three variables each with a different purpose at play
trip_time = int(input("How long will the trip take(in minutes)?:" ))

trip_time_in_minutes = trip_time % 60 # calculating how many minutes remain through the use of the modulo oprand
trip_time_in_hours = trip_time // 60 # Calculating how many times an hour can fit in the trip time through the use of floor division

minute_calc = trip_time_in_minutes + current_minute # Necessary variable calculation,addition of like terms
hour_calc = trip_time_in_hours + current_hour

hour_span = minute_calc // 60 # sometimes the minute_calc variavble can go beyond sixty, so if thats the case, its an hours span
 
arrival_minutes = minute_calc % 60 
arrival_hour = hour_calc + hour_span 

days_span = arrival_hour // 24 # This is a sortta minor update,if your not confortable with displaying days, you can always revert back to displaying arrival hours
new_arrival_hour = arrival_hour % 24

print(f"\n" ,f"Estimated time of arrival is {days_span} days, {new_arrival_hour} hours and {arrival_minutes} minutes.")
# Output
"""
# Change machine 
"""
print("Hello , Welcome to the change machine.")

item_cost = 18.76
print(f"Your items cost {item_cost}")

cash_payment = int(input("Enter Cash payment:"))

change = round((cash_payment - item_cost) , 2)
print(f"Change Due ${(change)}")


print(f" Dollars: {round(change)}")  
money = change - round(change)

print(f"Quarters: {int(money // 0.25)}")
cash_flow = (money - int(money // 0.25) * 0.25 )
 
print(f'   Dimes: {int(cash_flow // 0.10 )}')
cash_flow = round((money - int(cash_flow // 0.10) * 0.10) , 2)


print(f" Nickels: {int(cash_flow // 0.05)}")
cash_flow = round((cash_flow - int(cash_flow // 0.05) * 0.05) , 2)

print(f" Penny's: {int(cash_flow // 0.01)}")
"""
# 2.6 The Math Module

# finding the distance (magnitude of the resultant)
"""
import math

x1 = float(input("Enter x 1 coordinates:"))
y1 = float(input("Enter y 1 coordinates:"))
z1 = float(input("Enter z 1 coordinates:"))
x2 = float(input("Enter x 2 coordinates:"))
y2 = float(input("Enter y 2 coordinates:"))
z2 = float(input("Enter z 2 coordinates:"))

Overall_resultant = math.sqrt((x1 + x2) ** 2 + (y1 + y2) ** 2 + (z1 + z2) ** 2)

print(f"The distance is {round(Overall_resultant , 1)} meters")"""

# some math functions i know of 
"""
import math 

print("Welcome to some fun facts about math")
print(f" The log of 8 base 2 is equal to {math.log(8,2)}") # The first argument is the x variable and the second argument is the base
print(f"3 to the exponent of 4 equals {math.pow(3 , 4)}") # The first argument is the x variable and the second argument is the exponent
print(f"The square root of 81 is {math.sqrt(81)} ")
print(f"A complete revolution around a circle is {round(math.tau , 2)} Radians")
print('The log of a natural log multiplied by pi is ', (math.log(math.e) * math.pi))
print(round(math.cos(90))) # You can insert Radians as angles , you know the lot
print(round(math.sin(90)))
print(round(math.tan(90)))""" 

#  Quadratic formula
"""
import math

print("Hello, welcome to solving quadratics through the quadratic formula.(solution genaration only.)")

a = int(input("Enter (a) from quadratic:"))
b = int(input("Enter (b) from quadratic:"))
c = int(input("Enter (c) from quadratic:"))

def positive_res():
    solution = math.ceil(( -b + math.sqrt(abs(math.pow(b, 2) + 4 * a * c))) / (2 * a))
    return solution

def negative_res():
    solution = math.floor(( -b - math.sqrt(abs(math.pow(b, 2) + 4 * a * c))) / (2 * a))
    return solution

x1 = positive_res() 
x2 = negative_res()
 
print("Your x1 is equal to " , x1 , "and your x2 is equal to", x2 ,".")
"""
# The cylinder formula  
"""
import math

print("Welcome to how to find the area and volume of cylinders.(solution generation only.)","\n","Make sure that your metrics are in centimeters")

h = float(input("Enter the hieght:"))
r = float(input("Enter the radius:"))

def area_of_cylinder():
    solution = (math.tau * r * h) + (math.tau * math.pow(r , 2))
    return solution 
def volume_of_cylinder():
    solution  = math.pi * math.pow(r , 2) * h
    return solution

print(f"The area of your cylinder is equal to {round(area_of_cylinder() , 2)} centimeters squared." ) 
print(f"The volume of your cylinder is equal to {round(volume_of_cylinder() ,2)} centimeters cubed.")
"""
# Formatting code 
"""
print("My " "name "  "is" " Douviq") # Automatic concatenation , i never knew that python can do that

name = 'Ada ' \
"chow"
print("Hello", name)
print("Hello" ,"\n" ,name )
print("happy"
      "new year")
""" 
 # Five quotes
"""
print("If you'er talking about Java in particular, Python is about the best fit "
      "you can get amongst all the order languages. Yet the funny thing is, from a "
      "language point of view, JavaScript has a lot in common with Python, but it is sort " 
      "of a restricted subset.")

print("The second stream of materail that is going to come out of this project is "
      "a programming environment and a set of programming tools where we really want to "
      "focus again on the needs of the newbie. This environment is going to have to be "
      "extremely user-friendly.")

print("I have this hope that there is a better way. Higher-level tools that "
      "actually let you see the structure of the software more clearly will be of " 
      "tremendous value")

print("Now, it's my belief that Python is a lot easier than to teach to students "
      "programming and teach them C or  C++ or Java at the same time because all the "
      "details of the languages are so much harder. Other scripting languages really don't "
      "work very well there either.")

print("I would guess that the decision to create a small special purpose language "
      "or use an existing general purpose language is one of the toughest decisions that "
      "anyone facing the need for a new language must make.")"""