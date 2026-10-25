def generate_confirmation(customer, ticket_id):
    message = f"Hello {customer}, your ticket ID is {ticket_id}."
    return message

confirmation = generate_confirmation("Ada", 101)

print(confirmation)

