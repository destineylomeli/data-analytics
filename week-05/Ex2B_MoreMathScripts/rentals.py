# Calculates vans needed and cost per person 

import math

people = int(input("Enter number of tourists: "))

vans_needed = math.ceil(people / 15)

total_cost = vans_needed * 250 

cost_per_person = total_cost / people

print(f"Vans needed: {vans_needed}")
print(f"Total rental cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")

# Testing script with 38 tourists:
    # Vans needed = 3
    # Total cost = $750
    # Cost per person = $19.74