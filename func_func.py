def calculate_discounted_cost(cost, discount_percent):
    discount_amount = cost * discount_percent / 100
    final_price = cost -  discount_amount
    return final_price
    
precent = calculate_discounted_cost(10000, 20)
print(precent)
