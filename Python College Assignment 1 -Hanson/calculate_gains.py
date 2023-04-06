"""calculate_gains.py"""
# global variable
multiplier_amount = 1000000

def calculate_gains(amount_inv=0.0):
    """ Calculating the return gains of an investment."""
# base amount gain margin
    gain_margin = .001
    total_amount_gains = 0
    total_gains = 0

    if amount_inv > 1000:

        # check whether the invested amount is greater than the multiplier amount
        if amount_inv > multiplier_amount:
            # gather the value of the division
            mod = amount_inv // multiplier_amount
            # update the `gain_margin` by the multiplier mod
            gain_margin = ((mod /100)+ gain_margin)
        # calculate the total amount of gains
        total_amount_gains = (amount_inv * gain_margin) + amount_inv
        # calculate the total amount plus the gain margin
        total_gains = amount_inv * gain_margin
    # return the gains, the full amount and the gain margin
    return total_gains, total_amount_gains, gain_margin

    print(calculate_gains(amount_inv=2000000))