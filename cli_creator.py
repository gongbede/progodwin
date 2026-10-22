import json
import uuid
from pathlib import Path

FILE_PATH = Path("tickets.json")


def load_tickets():
    if not FILE_PATH.exists():
        return []

    try:
        with FILE_PATH.open("r", encoding="utf-8") as file:
            tickets = json.load(file)
    except json.JSONDecodeError:
        raise ValueError("tickets.json contains invalid JSON.")

    if not isinstance(tickets, list):
        raise ValueError("The tickets file must contain a list.")

    for ticket in tickets:
        if not isinstance(ticket, dict):
            raise ValueError("Every ticket must be a dictionary.")

    return tickets


def save_tickets(tickets):
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4, ensure_ascii=False)


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def create_ticket(title, description):
    return {
        "id": str(uuid.uuid4()),
        "title": title,
        "description": description
    }


def display_tickets(tickets):
    if not tickets:
        print("\nNo tickets found.")
        return

    print("\n========== ALL TICKETS ==========")

    for ticket in tickets:
        print(f"\nID: {ticket['id']}")
        print(f"Title: {ticket.get('title', 'No title')}")
        print(f"Description: {ticket.get('description', 'No description')}")
        print("-" * 40)


def create_new_ticket():
    title = get_non_empty_input("\nEnter ticket title: ")
    description = get_non_empty_input("Enter ticket description: ")

    tickets = load_tickets()
    new_ticket = create_ticket(title, description)

    tickets.append(new_ticket)
    save_tickets(tickets)

    print("\nTicket created successfully!")
    print(f"Ticket ID: {new_ticket['id']}")
    print(f"Title: {new_ticket['title']}")


def main():
    while True:
        print("\n" + "=" * 40)
        print("       CAMPUSFLOW TICKET CREATOR")
        print("=" * 40)
        print("1. Create a ticket")
        print("2. View all tickets")
        print("3. Exit")
        print("=" * 40)

        choice = input("Select an option (1-3): ").strip()

        try:
            if choice == "1":
                create_new_ticket()
            elif choice == "2":
                tickets = load_tickets()
                display_tickets(tickets)
            elif choice == "3":
                print("\nThank you for using CampusFlow!")
                break
            else:
                print("\nInvalid selection. Please choose 1, 2, or 3.")

        except (OSError, ValueError) as error:
            print(f"\nError: {error}")

        input("\nPress Enter to return to the home menu...")


if __name__ == "__main__":
    main()