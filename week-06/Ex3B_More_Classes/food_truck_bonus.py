# Lab 3 (Optional)

class Restaurant: 
    """This class represents a restaurant."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

class FoodTruck(Restaurant):
    """This class representsa food truck."""

    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)

        self.private_bookings = "N"
        self.truck_location = ""
        self.location_history = []

    def accepts_private_bookings(self):
        answer = input("Does this food truck accept private bookings? Y/N ")

        self.private_bookings = answer.upper()

        if self.private_bookings == "Y":
            print("This food truck currently accepts private bookings.")
        else:
            print("This food truck currently does not accept private bookings.")

    def relocate_truck(self):
            location = input("Enter current truck location: ")

            self.truck_location = location
            
            self.location_history.append (location)

            print(f"Truck is currently located at {location}")

# Create food truck object
truck1 = FoodTruck("Tasty Tacos", "Mexican Food")

# Test methods
truck1.accepts_private_bookings()

truck1.relocate_truck()
truck1.relocate_truck()

# I chose to allow duplcate locations so the history shows every place the truck visited over time.

print("Location History:")
print(truck1.location_history)