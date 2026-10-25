def create_ticket():
    ticket = {
    "id": 101,
    "title": "Login issue"
    }

    return ticket

result = create_ticket()
print("This is good:", result)