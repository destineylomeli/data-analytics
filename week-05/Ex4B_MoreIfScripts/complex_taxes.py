pay_rate = float(input("Enter pay rate: "))
hours_worked = float(input("Enter hours worked: "))
filling_status = input("Enter filling status (single/joint): ")

# Calculate weekly gross pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else: 
    gross_pay = hours_worked * pay_rate 

# Annual gross pay
annual_income = gross_pay * 52

# Determine tax rate
if filling_status == "single":
    if annual_income < 12000:
        tax_rate = 0.05
    elif annual_income < 25000:
        tax_rate = 0.10
    elif annual_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filling_status == "joint":
    if annual_income < 12000:
        tax_rate = 0.00 
    elif annual_income < 25000:
        tax_rate = 0.06
    elif annual_income < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

# Tax calculations
tax_withheld = gross_pay * tax_rate
net_pay = gross_pay - tax_withheld

# Output
print("You worked", hours_worked, "hours this period.")
print("Because you earn $", pay_rate, "per hour, your gross weekly pay is $", gross_pay)
print("Your filling status is", filling_status)
print("Your tax withholding for the week is $", tax_withheld)
print("Your net pay is $", net_pay)