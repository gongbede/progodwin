resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]

fellows = {
    "F001": "Ada",
    "F002": "John",
    "F003": "Grace"
}

borrow_records = []

def find_resource(resource_id):
    for resource in resources:
        if resource["id"].upper() == resource_id.upper():
            return resource
    return None

def add_resource():
    resource_id = input("Enter resource ID: ").strip()

    if find_resource(resource_id):
        print("Error: Resource ID already exists.")
        return

    name = input("Enter resource name: ").strip()
    category = input("Enter category: ").strip()

    if not name or not category:
        print("Error: Name and category cannot be empty.")
        return

    while True:
        try:
            total = int(input("Enter total units: "))

            if total <= 0:
                print("Enter a positive number.")
                continue

            break

        except ValueError:
            print("Please enter a valid integer.")

    resources.append({
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    })

    print("Resource added successfully.")

def list_resources():
    if not resources:
        print("No resources available.")
        return

    print("\n--- Resource Inventory ---")

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        print(
            f"ID: {resource['id']} | "
            f"Name: {resource['name']} | "
            f"Category: {resource['category']} | "
            f"Total: {resource['total']} | "
            f"Available: {resource['available']} | "
            f"Borrowed: {borrowed}"
        )

def get_positive_integer(prompt):
    while True:
        try:
            quantity = int(input(prompt))

            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue

            return quantity

        except ValueError:
            print("Please enter a valid integer.")

def borrow_resource():
    fellow_id = input("Enter fellow ID: ").strip().upper()

    if fellow_id not in fellows:
        print("Error: Fellow ID not found.")
        return

    resource_id = input("Enter resource ID: ").strip().upper()

    resource = find_resource(resource_id)

    if resource is None:
        print("Error: Resource ID not found.")
        return

    quantity = get_positive_integer("Enter quantity to borrow: ")

    if quantity > resource["available"]:
        print(
            f"Error: Only {resource['available']} "
            f"units of {resource['name']} are available."
        )
        return

    resource["available"] -= quantity

    borrow_records.append({
        "fellow_id": fellow_id,
        "resource_id": resource["id"],
        "quantity": quantity
    })

    print(
        f"{fellows[fellow_id]} borrowed "
        f"{quantity} {resource['name']}(s)."
    )

    print(f"Available units: {resource['available']}")

def return_resource():
    fellow_id = input("Enter fellow ID: ").strip().upper()

    if fellow_id not in fellows:
        print("Error: Fellow ID not found.")
        return

    resource_id = input("Enter resource ID: ").strip().upper()

    resource = find_resource(resource_id)

    if resource is None:
        print("Error: Resource ID not found.")
        return

    quantity = get_positive_integer("Enter quantity to return: ")

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource["id"]
        ):
            if quantity > record["quantity"]:
                print(
                    f"Error: {fellows[fellow_id]} only has "
                    f"{record['quantity']} {resource['name']}(s) on loan."
                )
                return

            record["quantity"] -= quantity
            resource["available"] += quantity

            if record["quantity"] == 0:
                borrow_records.remove(record)

            print(
                f"{fellows[fellow_id]} returned "
                f"{quantity} {resource['name']}(s)."
            )

            print(f"Available units: {resource['available']}")
            return

    print(
        f"Error: {fellows[fellow_id]} does not have "
        f"{resource['name']} on loan."
    )

def search_resources():
    search_term = input("Enter resource name: ").strip().lower()

    found = False

    for resource in resources:
        if search_term in resource["name"].lower():
            print(
                f"ID: {resource['id']} | "
                f"Name: {resource['name']} | "
                f"Category: {resource['category']} | "
                f"Available: {resource['available']}"
            )
            found = True

    if not found:
        print("No matching resources found.")

def filter_by_category():
    category = input("Enter category: ").strip().lower()

    found = False

    for resource in resources:
        if resource["category"].lower() == category:
            print(
                f"ID: {resource['id']} | "
                f"Name: {resource['name']} | "
                f"Category: {resource['category']} | "
                f"Available: {resource['available']}"
            )
            found = True

    if not found:
        print("No resources found in that category.")

def generate_report():
    total_units = 0
    available_units = 0

    for resource in resources:
        total_units += resource["total"]
        available_units += resource["available"]

    borrowed_units = total_units - available_units

    print("\n========== INVENTORY REPORT ==========")

    print(f"Overall units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Units currently borrowed: {borrowed_units}")

    print("\nResources with fewer than 3 available units:")

    low_stock = []

    for resource in resources:
        if resource["available"] < 3:
            low_stock.append(resource)

    if low_stock:
        for resource in low_stock:
            print(
                f"- {resource['name']} "
                f"({resource['available']} available)"
            )
    else:
        print("None")

    borrowed_by_resource = []

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        borrowed_by_resource.append({
            "resource": resource,
            "borrowed": borrowed
        })

    if borrowed_by_resource:
        highest = max(
            item["borrowed"]
            for item in borrowed_by_resource
        )

        leaders = [
            item["resource"]
            for item in borrowed_by_resource
            if item["borrowed"] == highest
        ]

        print("\nResource(s) with most units currently borrowed:")

        for resource in leaders:
            print(
                f"- {resource['name']} "
                f"({highest} borrowed)"
            )

    print("======================================\n")

def main_menu():
    while True:
        print("\n===== Learn2Earn Equipment System =====")
        print("1. Add resource")
        print("2. List resources")
        print("3. Borrow resource")
        print("4. Return resource")
        print("5. Search inventory")
        print("6. Filter by category")
        print("7. Generate report")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_resource()

        elif choice == "2":
            list_resources()

        elif choice == "3":
            borrow_resource()

        elif choice == "4":
            return_resource()

        elif choice == "5":
            search_resources()

        elif choice == "6":
            filter_by_category()

        elif choice == "7":
            generate_report()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-8.")

if __name__ == "__main__":
    main_menu()
