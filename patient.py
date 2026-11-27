
# Patient Registration System

patients = []

def register_patient():
    print("\n--- Patient Registration ---")

    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    condition = input("Enter Emergency Condition: ")

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "condition": condition
    }

    patients.append(patient)

    print("\nPatient registered successfully!")
    print(patient)


register_patient()
