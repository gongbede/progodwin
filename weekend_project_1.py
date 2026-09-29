contacts = ["Godwin", "Peter", "Kayla", "Regina"]
contacts.append("Joel")
print(contacts)
contacts.remove("Peter")
print(contacts)
for contact in contacts:
    print(contact)

print(contacts[: 3])
print(contacts[-2 :])
if "Godwin" in contacts:
    print("Godwin is on the list")

else:
    print("Godwin is not on the list")
