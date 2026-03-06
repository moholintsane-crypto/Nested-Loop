# binary conversion

def decimal_to_binary(decimal_num):
    """Converts a decimal integer to a binary string."""
    # bin() returns a string with a '0b' prefix, so we slice it off
    return bin(decimal_num)[2:]

def binary_to_decimal(binary_str):
    """Converts a binary string to a decimal integer."""
    # int() with base 2 converts a binary string to decimal
    return int(binary_str, 2)

# --- Example Usage ---
decimal_input = int(input("Enter a number: "))
binary_result = decimal_to_binary(decimal_input)
print(f"Decimal {decimal_input} is Binary {binary_result}")

binary_input = input("Enter a binary number: ")
decimal_result = binary_to_decimal(binary_input)
print(f"Binary {binary_input} is Decimal {decimal_result}")