

# NORMAL PATIENT WAITING QUEUE

from collections import deque

waiting_patients = deque()


def add_to_queue(patient_name):
    waiting_patients.append(patient_name)
    print(patient_name, "added to waiting queue successfully!")


def treat_next_patient():
    if waiting_patients:
        patient = waiting_patients.popleft()
        print("Now treating:", patient)
    else:
        print("No patients waiting.")


def show_queue():
    print("\n--- Normal Patient Waiting Queue ---")

    if not waiting_patients:
        print("Waiting queue is empty.")
        return

    for position, patient in enumerate(waiting_patients, start=1):
        print(position, "-", patient)
