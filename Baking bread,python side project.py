# Baking bread 

#ingredients for a loaf of bread

tsps_instantYeast = 1 + (1/2) 
tsps_salt =  1 + (1/2)  # with tsps denoting teaspoons
tsps_sugar = 1 + (1/2)   # variables 
CupsOfFlour = 2 + (1/2)
CupsOfSourdough = 2
CupsOfWater = 1/2  


bread_weight = float(input("Enter the wieght of a loaf(in ounces):"))  # one ounce is 28 grams by the way.
serving_size = float(input("Enter the wieght of a slice(in ounces):"))  # user input
num_guests = int(input("Enter the number of guests:"))

servings_wieght = num_guests * serving_size    # weight of the total slices served 
bread_needed = servings_wieght / bread_weight   # Necessary calculations

print(f"For {num_guests} people, you will need {bread_needed} loaves of bread:", "\n"  # Output
       "\n" 
        f"  {bread_needed * tsps_instantYeast} teaspoons instant yeast", "\n"
        f"  {bread_needed * tsps_salt} teaspoons salt", "\n"
        f"  {bread_needed * tsps_sugar} teaspoons sugar", "\n"
        f"  {bread_needed * CupsOfFlour} cups all-purpose flour", "\n"    
        f"  {bread_needed * CupsOfSourdough} cups sourdough starter", "\n"
        f"  {bread_needed * CupsOfWater} cups of lukewarm water", "\n"
        )
