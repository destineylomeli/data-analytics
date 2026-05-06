# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
# str() converts numbers into text so they can be combined with strings in the print statement

# print("The total due is " + str(total+due))

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
print("Tip is " + str(tip))
print("Total due is " + str(total_due))

# Commented out old tip line
# print("Tip is " + str(tip))

print("Tip is " + format(tip, ".2f"))