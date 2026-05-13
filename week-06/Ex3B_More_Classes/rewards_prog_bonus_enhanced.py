# Lab 2 (Optional)

class RewardsProgram:
    """This class tracks restaurant rewards points."""

    def __init__(self, cust_name):
        self.cust_name = cust_name
        self.restaurants_visited = []
        self.rewards_points = 0

    def visit_rest(self):
        restaurant = input("Name of restaurant: ")

        if restaurant not in self.restaurants_visited:
            self.restaurants_visited.append(restaurant)

            bill = float(input("What was the total food bill for this visit? "))

            points = int(bill)

            self.rewards_points += points

            print(f"Points for this visit: {points}")
            print(f"Total rewards points earned: {self.rewards_points}")
            print(f"Thank you for visiting {restaurant}!")

# Create customer
customer1 = RewardsProgram("Dahlia Sanchez")

# Test method
customer1.visit_rest()
customer1.visit_rest()

print(customer1.restaurants_visited)