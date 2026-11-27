
# Patient Linked List

class Node:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name
        self.next = None


class PatientLinkedList:
    def __init__(self):
        self.head = None

    def add_patient(self, patient_id, name):
        new_node = Node(patient_id, name)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        print("Patient added successfully!")

    def display_patients(self):
        current = self.head

        print("\n--- Patient Records ---")

        while current is not None:
            print(current.patient_id, current.name)
            current = current.next


# Example
records = PatientLinkedList()

records.add_patient("P101", "Rahul")
records.add_patient("P102", "Aman")
records.add_patient("P103", "Priya")

records.display_patients()
