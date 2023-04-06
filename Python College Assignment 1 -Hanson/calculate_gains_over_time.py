"""calculate_gains_over_time.py"""
from calculate_gains import calculate_gains


def calculate_gains_over_time(amount_inv=0.0, period=12):
    """
    Calculating the return gains of a given amount invested based on a period of application.
    :param amount_inv: the money amount invested
    :param period: application period
    :return:
    """
    # call the base `calculate_gains` function to estimate the gains for the first period
    total_amount = calculate_gains(amount_inv)[1]
    # calculate the first period before entering the loop
    # loop through the specified period to calculate the gain of each month
    for i in range(1, period):
        # 1 to period-1 because the first period gains is already calculated above
        # call the function to update the value based on the period inside the loop and the updated amount
        total_amount = calculate_gains(total_amount)[1]
        new_amount = total_amount  # update the `new_amount` variable
    # return the final ammount
    return new_amount


print(calculate_gains_over_time(amount_inv=4000000, period=12))