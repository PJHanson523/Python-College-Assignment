"""Create a user-defined function called calculate_gains(), which receives the amount desired to be invested.
Outside this function, create a global variable, multiplier_amount that would be accessible at any point in
your code to store the "multiplier amount", which will be the amount that would trigger the increase on the gain
margin in case the invested amount is greater than this value. In our case, this amount is set to 1 million.

Inside your function, create a variable to store the gain margin, which is 0.1% by default. Also create variables
for total_gains and total_amount, setting default values to 0. After these declarations, the first thing to check
is whether the amount invested is greater than 1000 (one thousand), which is the minimum application value to start
using the app.

Next, check if the amount is greater than the multiplier value (1 million). If it is greater, then update the gain
margin variable with the new gain margin and add the estimated amount to the original amount, otherwise just multiply
the values to obtain the return on investment for the given amount.

Finally, you need to return the total gains amount, the amount invested updated with the return on investment added to
it, as well as the gain margin (the ordering is important for testing purposes). To test your function, enter the
following amount: 2000000 ($2 million).

To summarize:

• In the user-defined function declare a global variable inside the python file to store the multiplier amount.

• Declare a variable to store the gain margin.

• Declare variables to store the total gains and the total amount.

• Check if the amount is greater than the minimum value (which is 1000).

• Check if the amount is greater than the multiplier amount (which is 1000000).

• If so, update the gain margin.

• Calculate the total gains by multiplying the gain margin by the amount.

• Return the total gains, total updated amount, and gain margin.

Example:

Input :

calculate_gains(amount_inv=2000000)
Output:

(42000.0, 2042000.0, 0.021)
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
Part 2:
Another functionality for the app is the ability to estimate the return on investment
over a period of time. In order to implement this feature, you will have to update the
investment calculator algorithm.

The base function to calculate the return on investment from Task 1 can be reutilized
here to simplify our task. This feature will take into consideration a 12-month period by default.

To calculate the total amount earned over a period of time, you will have to loop through
the n-months period, increase the amount for each period. The other rules from the previous task
apply here as well.

For example: If you invest $3 million on the first month, and obtain a return of $93,000 dollars,
then the amount to be invested in the second month is $3.093 million.

To summarize:

Loop over a period of 12 months to calculate the total for each period
Return the accumulated estimated value for a period of 12 months"""