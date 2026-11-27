
# Patient Search using Hash Map

patient_records = {}

def add_patient(patient_id, name, age):
    patient_records[patient_id] = {
        "name": name,
        "age": age
    }
    print("Patient saved successfully!")


def search_patient(patient_id):
    if patient_id in patient_records:
        print("\nPatient Found!")
        print("ID:", patient_id)
        print("Name:", patient_records[patient_id]["name"])
        print("Age:", patient_records[patient_id]["age"])
    else:
        print("Patient not found!")


# Example records
add_patient("P101", "Rahul", 25)
add_patient("P102", "Priya", 30)

search_patient("P101")
