def verify_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example of use
number = 5
result = verify_odd_even(number)
print(f"The number {number} is {result}.")
