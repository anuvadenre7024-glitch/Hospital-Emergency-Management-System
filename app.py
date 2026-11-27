


# HOSPITAL EMERGENCY MANAGEMENT SYSTEM

from patient import register_patient
from priority_queue import add_patient, show_waiting_list, treat_next_patient
from doctor import show_doctors, assign_doctor, release_doctor
from waiting_queue import add_to_queue, show_queue, treat_next_patient as treat_normal_patient


def main():
    while True:
        print("\n================================")
        print(" HOSPITAL MANAGEMENT SYSTEM")
        print("================================")
        print("1. Patient Registration")
        print("2. Add Emergency Patient")
        print("3. Show Emergency Priority Queue")
        print("4. Treat Next Emergency Patient")
        print("5. Show Doctors")
        print("6. Assign Doctor")
        print("7. Release Doctor")
        print("8. Add Normal Patient")
        print("9. Show Normal Waiting Queue")
        print("10. Treat Next Normal Patient")
        print("11. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            register_patient()

        elif choice == "2":
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")

            try:
                priority = int(input("Enter priority (1-Critical, 2-Serious, 3-Stable): "))

                if priority in (1, 2, 3):
                    add_patient(patient_id, name, priority)
                else:
                    print("Invalid priority!")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            show_waiting_list()

        elif choice == "4":
            treat_next_patient()

        elif choice == "5":
            show_doctors()

        elif choice == "6":
            show_doctors()
            doctor_id = input("Enter Doctor ID to assign: ")
            assign_doctor(doctor_id)

        elif choice == "7":
            doctor_id = input("Enter Doctor ID to release: ")
            release_doctor(doctor_id)

        elif choice == "8":
            name = input("Enter Patient Name: ")
            add_to_queue(name)

        elif choice == "9":
            show_queue()

        elif choice == "10":
            treat_normal_patient()

        elif choice == "11":
            print("Thank you for using our system!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
