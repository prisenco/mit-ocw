semi_annual_raise = 0.07
r = 0.04
current_savings = 0
total_cost = 1_000_000
portion_down_payment = 0.25

down_payment_required = total_cost * portion_down_payment

original_annual_salary = float(input("Enter your annual salary: "))

epsilon = 100
min_rate = 1
max_rate = 10_000

"""
All we really have to think about is bisecting the rate.
The rest of the calculations will fall into place.
And we use results to decide how to update the rate (from bottom or top).
"""

steps = 0
while abs(min_rate - max_rate) > 1:
    steps += 1
    rate_guess = int((min_rate + max_rate) / 2)

    current_savings = 0
    annual_salary = original_annual_salary

    """
    Calculate savings after 36 months at the current rate
    NOTE: This should be a function
    """
    for month in range(1, 37):
        current_savings += current_savings * r / 12  # Monthgly interest
        portion_saved = annual_salary / 12 * rate_guess / 10_000  # Savings rate
        current_savings += portion_saved
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    difference = abs(current_savings - down_payment_required)

    if difference <= epsilon:
        print("Best savings rate:", rate_guess / 10_000)
        print("Steps in bisection search:", steps)
        exit()
    elif difference > epsilon and current_savings > down_payment_required:
        max_rate = rate_guess
    elif difference > epsilon and current_savings < down_payment_required:
        min_rate = rate_guess

print("It is not possible to pay the down payment in three years.")
