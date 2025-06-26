from validation import validate_fields

def initialize_data():
    customers = [
        {"id": 1, "name": "Alice", "email": "alice@example.com", "phone": "07123456789", 
         "date_joined": "2022-01-01", "membership_status": "Gold", "balance": 100.0, "is_active": True},
        {"id": 2, "name": "Bob", "email": "bob@example.com", "phone": "07123456780", 
         "date_joined": "2022-02-01", "membership_status": "Silver", "balance": 50.0, "is_active": True}
    ]
    valid_customers = [c for c in customers if validate_fields(c)]
    return valid_customers

def view_all_customers(customers):
    for c in customers:
        print(c)

def view_single_customer(customers):
    cid = int(input("Enter customer ID: "))
    customer = next((c for c in customers if c["id"] == cid), None)
    print(customer if customer else "Customer not found.")

def add_customer(customers):
    try:
        new = {
            "id": int(input("ID: ")),
            "name": input("Name: "),
            "email": input("Email: "),
            "phone": input("Phone: "),
            "date_joined": input("Date Joined (YYYY-MM-DD): "),
            "membership_status": input("Membership Status: "),
            "balance": float(input("Balance: ")),
            "is_active": input("Active (True/False): ").lower() == "true"
        }
        if validate_fields(new):
            customers.append(new)
            print("Customer added successfully.")
        else:
            print("Invalid customer data.")
    except Exception as e:
        print(f"Error: {e}")

def update_customer(customers):
    cid = int(input("Enter ID to update: "))
    customer = next((c for c in customers if c["id"] == cid), None)
    if customer:
        customer["name"] = input("New name: ")
        print("Customer updated.")
    else:
        print("Customer not found.")

def delete_customer(customers):
    cid = int(input("Enter ID to delete: "))
    confirm = input("Are you sure? (y/n): ")
    if confirm.lower() == 'y':
        customers[:] = [c for c in customers if c["id"] != cid]
        print("Customer deleted.")