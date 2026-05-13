# Displaying mailing label
def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(f"{city}, {state} {zip_code}")

display_mailing_label(
    "Maria Lopez",
    "123 Main Street",
    "San Jose",
    "CA",
    "95112"
)

# Add numbers
def add_numbers(*numbers):
    total = sum(numbers)

    equation = " + ".join(str(num) for num in numbers)

    print(f"{equation} = {total}")

add_numbers(5)

add_numbers(5, 10)

add_numbers(1, 2, 3, 4, 5)

# Display receipt
def display_receipt(total_due, amount_paid):

    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${amount_paid}")

    if amount_paid > total_due:
        change = amount_paid - total_due
        print(f"Change due: ${change}")

    elif amount_paid == total_due:
        print("Exact amount paid. No change due.")

    else: 
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance}")

display_receipt(25, 40)
display_receipt(25, 25)
display_receipt(25, 10)
