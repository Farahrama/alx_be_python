from datetime import datetime
# and to calculate a future date based on user input.
def display_current_datetime():
    """Display the current date and time."""
    current_datetime = datetime.now()
    print("current datetime: ", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
def calculate_future_date():
    import datetime
    """calculate a future date based on user input."""
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.datetime.now() + datetime.timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))
# and to calculate a future date based on user input.

display_current_datetime()
calculate_future_date()
# This code snippet demonstrates how to work with datetime in Python.
# It includes functions to display the current date and time,