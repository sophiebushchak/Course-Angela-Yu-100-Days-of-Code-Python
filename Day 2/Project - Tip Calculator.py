# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# Greet user
print("Welcome to the tip calculator!")

# Ask out information
total_bill = input("What was the total bill? $")
tip_percentage = input("What tip percentage would you like to give? ")
amount_of_people = input("How many people are splitting the bill? ")

# Calculate
bill_with_tip = float(total_bill) * (float(tip_percentage) / 100 + 1)
amount_per_person = bill_with_tip / int(amount_of_people)

# Display amount to pay per person
print(f"Each person should pay ${'{:.2f}'.format(amount_per_person)}.")
