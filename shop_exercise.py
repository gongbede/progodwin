products = ["Rice", "Bean", "Milk", "Bread"]
prices = [5000, 3000, 1500, 1000]

for number in range(len(products)):
    if prices[number]  >= 3000:
        print(products[number], prices[number], "EXpensive")

    else:
        print(products[number], prices[number])
