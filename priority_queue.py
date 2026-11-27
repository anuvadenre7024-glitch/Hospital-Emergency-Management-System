
# Emergency Priority Management

import heapq

patients = []

def add_patient(patient_id, name, priority):
    patient = (priority, patient_id, name)
    heapq.heappush(patients, patient)
    print("Patient added successfully!")

def show_waiting_list():
    print("\n--- Emergency Waiting List ---")

    for patient in sorted(patients):
        print(patient)

add_patient("P101", "Rahul", 1)
add_patient("P102", "Aman", 3)
add_patient("P103", "Priya", 2)

show_waiting_list()
