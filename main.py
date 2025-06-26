from ui import display_main_menu
from customer_ops import (
    initialize_data, view_all_customers, add_customer,
    update_customer, delete_customer, view_single_customer
)

def main():
    customers = initialize_data()
    while True:
        choice = display_main_menu()
        if choice == '1':
            view_all_customers(customers)
        elif choice == '2':
            add_customer(customers)
        elif choice == '3':
            update_customer(customers)
        elif choice == '4':
            delete_customer(customers)
        elif choice == '5':
            view_single_customer(customers)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()