# Lab 1

class Restaurant: 
    """This class represents a restaurant."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0 
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        customers = int(input("How many customers served today? "))
        self.number_served += customers

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        rating = input("How would you rate your experience today on a scale of 1-5?")

        if rating.isdigit():
            rating = int(rating)

            if 1 <= rating <= 5:
                self.customer_ratings.append(rating)

                average = sum(self.customer_ratings) / len(self.customer_ratings)

                print(f"Your rating was {rating}.")
                print(f"The average rating for this restuarant is {average:.2f}")
            else:
                print("Please enter a number between 1 and 5.")

        else: 
            print("Invalid input. Please enter a whole number from 1-5.")

# Create restaurant instances
restaurant1 = Restaurant("In n Out", "Burgers")
restaurant2 = Restaurant("Subway", "Sandwiches")
restaurant3 = Restaurant("Chick-fil-a", "Chicken")

# Test methods
restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()

restaurant1.customer_rating()
restaurant1.customer_rating()

# ============================

restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()

restaurant2.customer_rating()
restaurant2.customer_rating()

# =============================

restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()

restaurant2.customer_rating()
restaurant2.customer_rating()