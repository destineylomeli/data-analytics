savings = 1000
interest_rate = 6

years = 72 / interest_rate
double_balance = savings * 2

print(f"Your current savings is {savings}")

print(
    f"At a {interest_rate}% interest rate, "
    f"your savings account will be worth "
    f"{format(double_balance, '.2f')} "
    f"in {format(years, '.1f')} years"
)