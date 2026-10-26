def calculate_final_price(price, discount_percent, service_fee):
    discount_amount = price * discount_percent / 100 
    final_price = price - discount_amount + service_fee
    return final_price

final_price = calculate_final_price(10000, 20, 500)
print(final_price)
