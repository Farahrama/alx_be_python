def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return ("The result of the division is ", result)
    except ZeroDivisionError:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
    except ValueError:
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise ValueError("Error: Please enter numeric values only.")