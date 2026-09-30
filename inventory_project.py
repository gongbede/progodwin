inventorys = {
    "apple": {"price": 200, "quantity": 50},
    "bread": {"price": 500, "quantity": 20},
    "milk": {"price": 800, "quantity": 15}

}
inventorys["egg"] = {"price": 1000, "quantity": 10}
inventorys["apple"]["quantity"] = inventorys["apple"]["quantity"] - 10
print(inventorys["apple"])
print(inventorys)

for name, info in inventorys.items():
    print(name, "-", info["price"], "-", info["quantity"])

total = 0

for name, info in inventorys.items():
    total = total + info["price"] * info["quantity"]

print(total)

print(inventorys.get("sugar", "Item not in stock"))

for name, info in inventorys.items():
    if info["quantity"] < 20:
        print(name, info["quantity"])

del inventorys["milk"]
print(inventorys)
