def calculate_ticket_cost(hours, hourly_rate, discount=0):
    total = hours * hourly_rate
    final_cost = total - discount
    return final_cost

result = calculate_ticket_cost(4, 2000, 1000)
print(result)
