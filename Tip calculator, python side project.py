bill_amount = float(input("Enter bill amount: "))
percentage_tip = float(input("Percentage to tip: "))  # User input
num_of_people = int(input("Number of people: "))

Tip_amount = round((percentage_tip / 100)*bill_amount, 2)   # Necessary calculations stored in variables 
Total_amount = Tip_amount + bill_amount
Tip_per_person = Tip_amount / num_of_people
Total_per_person = round(Total_amount / num_of_people, 2)

print(f"Tip amount: ${Tip_amount}" "\n"  # Output 
      f"Total amount: ${Total_amount}" "\n"
      "\n"
      "\n"
      f"Tip per person: ${Tip_per_person}" "\n" 
      f"Total per person: ${Total_per_person}")