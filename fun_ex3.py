def create_confirmation(customer, ticket_id):
    return f"Hello {customer}, your ticket number is {ticket_id}"

message = create_confirmation("Ada", 105)
print(message)