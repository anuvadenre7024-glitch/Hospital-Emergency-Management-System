

# DOCTOR MANAGEMENT SYSTEM

doctors = {
    "D101": {"name": "Dr. Sharma", "available": True},
    "D102": {"name": "Dr. Verma", "available": True},
    "D103": {"name": "Dr. Khan", "available": False}
}


def show_doctors():
    print("\n--- Doctor Availability ---")

    for doctor_id, details in doctors.items():
        status = "Available" if details["available"] else "Busy"
        print(doctor_id, "-", details["name"], "-", status)


def assign_doctor(doctor_id):
    if doctor_id in doctors:
        if doctors[doctor_id]["available"]:
            doctors[doctor_id]["available"] = False
            print("Doctor assigned successfully!")
        else:
            print("This doctor is currently busy.")
    else:
        print("Doctor not found!")


def release_doctor(doctor_id):
    if doctor_id in doctors:
        doctors[doctor_id]["available"] = True
        print("Doctor is now available.")
    else:
        print("Doctor not found!")
