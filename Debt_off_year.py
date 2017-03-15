
balance = 320000
annualInterestRate = 0.2

e = 0.1
Monthly_interest_rate = annualInterestRate/12.0
Monthly_payment_lower_bound = round((balance / 12), 2)
Monthly_payment_upper_bound = round((balance * (1 + Monthly_interest_rate) ** 12)/ 12.0, 2)

def lowest_amount_paid(unpaid_balance, monthly_interest_rate, fixed_amount):
    for i in range (1,13):
        monthly_unpaid_balance = unpaid_balance - fixed_amount
        unpaid_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    return round(unpaid_balance,1)

guess = False

while not guess:
    fixed_monthly_payment = round((Monthly_payment_upper_bound + Monthly_payment_lower_bound) / 2, 2)
    result = lowest_amount_paid(balance, Monthly_interest_rate, fixed_monthly_payment)
    if result == 0.0 or result == e:
        guess = True
        print(round(fixed_monthly_payment,2))

    elif result > 0:
        Monthly_payment_lower_bound = fixed_monthly_payment
    else:
        Monthly_payment_upper_bound = fixed_monthly_payment