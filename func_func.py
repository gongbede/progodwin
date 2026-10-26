def calculate_discounted_cost(cost, discount_percent):
    discount_amount = cost * discount_percent / 100
    final_price = cost -  discount_amount
    return final_price

precentage1 = calculate_discounted_cost(10000, 20)
percentage2 = calculate_discounted_cost(20000, 10)
percentage3 = calculate_discounted_cost(5000, 0)

print(precentage1)
print(percentage2)
print(percentage3)

