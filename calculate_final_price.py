def calculate_final_price(price, discount):
    discount = price * discount / 100
    final_price = price - discount
    return final_price

def calculate():
    final_price = calculate_final_price(1000, 10)
    print(final_price)

calculate()