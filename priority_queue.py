

# Emergency Priority Management System

import heapq

patients = []


def add_patient(patient_id, name, priority):
    patient = (priority, patient_id, name)
    heapq.heappush(patients, patient)
    print("Patient added to emergency queue successfully!")


def show_waiting_list():
    print("\n--- Emergency Waiting List ---")

    if not patients:
        print("No emergency patients waiting.")
        return

    for priority, patient_id, name in sorted(patients):
        print(
            "Priority:", priority,
            "| ID:", patient_id,
            "| Name:", name
        )


def treat_next_patient():
    if patients:
        priority, patient_id, name = heapq.heappop(patients)
        print("\nNext emergency patient:", name)
        print("Patient ID:", patient_id)
        print("Priority:", priority)
    else:
        print("No emergency patients waiting.")
