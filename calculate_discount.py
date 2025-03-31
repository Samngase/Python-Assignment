def calculate_discount(price, discount_percent):
    """Calculate final price after applying discount if it's 20% or more."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price  # Return original price if discount < 20%

# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"Discount applied! The final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. The price remains: ${price:.2f}")
