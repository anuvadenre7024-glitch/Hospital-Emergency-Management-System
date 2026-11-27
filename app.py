
# HOSPITAL EMERGENCY MANAGEMENT SYSTEM

from patient import register_patient
from priority_queue import add_patient, show_waiting_list, treat_next_patient


def main():
    while True:
        print("\n================================")
        print(" HOSPITAL MANAGEMENT SYSTEM")
        print("================================")
        print("1. Patient Registration")
        print("2. Add Emergency Patient")
        print("3. Show Emergency Priority Queue")
        print("4. Treat Next Emergency Patient")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            register_patient()

        elif choice == "2":
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")

            print("\nPriority levels:")
            print("1. Critical")
            print("2. Serious")
            print("3. Stable")

            try:
                priority = int(input("Enter priority (1-3): "))

                if priority in (1, 2, 3):
                    add_patient(patient_id, name, priority)
                else:
                    print("Invalid priority! Choose 1, 2 or 3.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            show_waiting_list()

        elif choice == "4":
            treat_next_patient()

        elif choice == "5":
            print("Thank you for using our system!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()

