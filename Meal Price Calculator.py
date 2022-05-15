#Meal Price Calculator

import math     
#Ask user for the input
child_meal = float(input("Price of a child meal: "))
adult_meal = float(input("Price of an adult meal: "))
number_of_children = int(input("Number of children: "))   #Used int for this variable because human beings can't be divided into 2
number_of_adult = int(input("Number of adults: "))
sales_tax_rate = float(input("Sales tax rate: "))

meal_subtotal = (number_of_children * child_meal) + (number_of_adult * adult_meal) 
print()
print(f"Subtotal: ${meal_subtotal:.2f}") # Used .2f to round up the entry to 2 decimal places
sales_tax = (meal_subtotal * sales_tax_rate) / 100

print(f"Sales Tax: ${sales_tax:.2f}")   
total_price = meal_subtotal + sales_tax  #total_price is meal_subtotal + sales tax
print(f"Total: ${total_price:.2f}") #total price of the item bought

#Asked user for the amount that will be used for payment
print()
payment_amount = float(input("What is the payment amount: $"))
change = payment_amount - total_price   # Deduct the total_price from the payment amount to give the user the change
print(f"Your change is: ${change:.2f}")    #Converts change to 2 decimal places


add_donation = math.ceil(total_price)    #This will round up the change to the next int
change_after_donation = payment_amount - add_donation     #The final amount after donation has been made

print()
donate = input("Would you like to round up the total and donate to a charity? Yes or No? ").lower()  #Converts all entries into lower case 
if donate == "yes":      #If user answers yes, it rounds up the total price o the next whole number and deducts it from the payment amount
    print(f"Thank you! Your change is ${change_after_donation:.2f}")
else:
    print("Thank you. Enjoy the rest of your day.")






