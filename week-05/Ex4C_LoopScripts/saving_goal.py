bank_balance = 100
savings_goal = 500
weekly_savings = 75

while bank_balance < savings_goal:

    bank_balance += weekly_savings

    if bank_balance >= savings_goal * 0.75:
        bank_balance -= 10
        print("So close! After treating myself, my balance is up to", bank_balance)

    elif bank_balance > savings_goal / 2:
        print("Almost there! This week my balance is up to", bank_balance)

    else: 
        print("This week my balance increased to", bank_balance)

print("Goal met! My current balance is", bank_balance)