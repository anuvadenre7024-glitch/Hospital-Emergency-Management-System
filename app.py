
# HOSPITAL EMERGENCY MANAGEMENT SYSTEM

def main():
    while True:
        print("\n================================")
        print(" HOSPITAL MANAGEMENT SYSTEM")
        print("================================")
        print("1. Patient Registration")
        print("2. Emergency Priority Queue")
        print("3. Doctor Management")
        print("4. Patient Waiting Queue")
        print("5. Search Patient")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("Patient Registration Selected")

        elif choice == "2":
            print("Emergency Priority Queue Selected")

        elif choice == "3":
            print("Doctor Management Selected")

        elif choice == "4":
            print("Patient Waiting Queue Selected")

        elif choice == "5":
            print("Patient Search Selected")

        elif choice == "6":
            print("Thank you for using our system!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()

