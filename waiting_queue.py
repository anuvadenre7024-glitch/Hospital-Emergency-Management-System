
# Normal Patient Waiting Queue

from collections import deque

waiting_patients = deque()

def add_to_queue(patient_name):
    waiting_patients.append(patient_name)
    print(patient_name, "added to waiting queue.")

def treat_next_patient():
    if waiting_patients:
        patient = waiting_patients.popleft()
        print("Now treating:", patient)
    else:
        print("No patients waiting.")

def show_queue():
    print("\n--- Patient Waiting Queue ---")
    for patient in waiting_patients:
        print(patient)


# Sample patients
add_to_queue("Rahul")
add_to_queue("Aman")
add_to_queue("Priya")

show_queue()
