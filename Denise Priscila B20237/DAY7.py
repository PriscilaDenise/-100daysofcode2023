#enter the total cost of their shopping cart.
total_cost = float(input("Enter the total cost of your shopping cart: $"))

# Check if the condition is met.
if total_cost >= 50:
    # Apply a 10% discount to the total cost.
    discount = total_cost * 0.10
    discounted_total = total_cost - discount
else:
    # No discount is applied.
    discount = 0
    discounted_total = total_cost

# Output the original total cost and the discounted total cost (if a discount is applied) to the user.
print(f"Original Total Cost: ${total_cost:.2f}")
if discount > 0:
    print(f"Discount Applied (10%): ${discount:.2f}")
    print(f"Discounted Total Cost: ${discounted_total:.2f}")
else:
    print("No Discount Applied.")



