def calculate_final_price(price, discount_percent, service_fee):
    discount_amount = price * discount_percent / 100 
    final_price = price - discount_amount + service_fee
    return final_price

final_price = calculate_final_price(
    price=10000,
    discount_percent=20,
    service_fee=500
)
print(final_price)
