# Global customer list
cust_list = []

class RewardsProgram:
    """This class stores rewards customer information"""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Enail: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cut_list(self):
        customer_data = (self.cust_name, self.phone, self.email)
        cust_list.append(customer_data)

# Create customer instances
customer1 = RewardsProgram(
    "Dahlia Sanchez",
    "831-555-1234",
    "dahli@email.com"
)

customer2 = RewardsProgram(
    "Gabriela Islas",
    "400-555-5678",
    "gabi@gmail.com"
)

customer3 = RewardsProgram(
    "Natalia Miranda",
    "650-555-8888",
    "natalia@gmail.com"
)

# Run methods
customer1.profile()
customer1.thank_you()
customer1.add_to_cut_list()

customer2.profile()
customer2.thank_you()
customer2.add_to_cut_list()

customer3.profile()
customer3.thank_you()
customer3.add_to_cut_list()

# Print final customer list
print(cust_list)