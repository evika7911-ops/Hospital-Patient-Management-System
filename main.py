import sys
from database import Database

def print_header(title):
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def display_patient(patient):
    if not patient:
        print("No record found.")
        return
    print(f"ID       : {patient[0]}")
    print(f"Name     : {patient[1]}")
    print(f"Age      : {patient[2]}")
    print(f"Gender   : {patient[3]}")
    print(f"Phone    : {patient[4]}")
    print(f"Disease  : {patient[5]}")
    print(f"Doctor   : {patient[6]}")
    print(f"Status   : {patient[7]}")
    print("-" * 50)

def add_patient_ui(db):
    print_header("ADD NEW PATIENT")
    name = input("Enter Patient Name: ").strip()
    
    while True:
        try:
            age = int(input("Enter Age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid age number.")
            
    gender = input("Enter Gender (Male/Female/Other): ").strip()
    phone = input("Enter Phone Number: ").strip()
    disease = input("Enter Medical Condition / Disease: ").strip()
    doctor = input("Enter Assigned Doctor: ").strip()

    db.add_patient(name, age, gender, phone, disease, doctor)
    print("\n[+] Patient registered successfully!")

def view_all_patients_ui(db):
    print_header("ALL PATIENT RECORDS")
    patients = db.get_all_patients()
    if not patients:
        print("No patient records found in the database.")
        return
    
    print(f"{'ID':<5} | {'Name':<20} | {'Age':<5} | {'Gender':<8} | {'Status':<10}")
    print("-" * 55)
    for p in patients:
        print(f"{p[0]:<5} | {p[1]:<20} | {p[2]:<5} | {p[3]:<8} | {p[7]:<10}")

def search_patient_ui(db):
    print_header("SEARCH PATIENT")
    try:
        p_id = int(input("Enter Patient ID: "))
        patient = db.search_patient_by_id(p_id)
        if patient:
            print("\nRecord Found:")
            display_patient(patient)
        else:
            print(f"\n[-] No patient found with ID: {p_id}")
    except ValueError:
        print("Invalid ID. Must be an integer.")

def update_patient_ui(db):
    print_header("UPDATE PATIENT DETAILS")
    try:
        p_id = int(input("Enter Patient ID to Update: "))
        patient = db.search_patient_by_id(p_id)
        if not patient:
            print(f"[-] No patient found with ID: {p_id}")
            return

        print("\nCurrent Details:")
        display_patient(patient)
        print("Enter new details (Press Enter to keep current value):")

        name = input(f"Name [{patient[1]}]: ").strip() or patient[1]
        
        age_input = input(f"Age [{patient[2]}]: ").strip()
        age = int(age_input) if age_input.isdigit() else patient[2]

        gender = input(f"Gender [{patient[3]}]: ").strip() or patient[3]
        phone = input(f"Phone [{patient[4]}]: ").strip() or patient[4]
        disease = input(f"Disease [{patient[5]}]: ").strip() or patient[5]
        doctor = input(f"Doctor [{patient[6]}]: ").strip() or patient[6]

        db.update_patient(p_id, name, age, gender, phone, disease, doctor)
        print("\n[+] Patient details updated successfully!")

    except ValueError:
        print("Invalid input format.")

def update_status_ui(db):
    print_header("UPDATE PATIENT STATUS")
    try:
        p_id = int(input("Enter Patient ID: "))
        patient = db.search_patient_by_id(p_id)
        if not patient:
            print(f"[-] No patient found with ID: {p_id}")
            return

        print(f"Current Status: {patient[7]}")
        print("1. Admitted\n2. Discharged\n3. Under Observation")
        choice = input("Select new status (1-3): ").strip()
        
        status_map = {"1": "Admitted", "2": "Discharged", "3": "Under Observation"}
        new_status = status_map.get(choice)

        if new_status:
            db.update_status(p_id, new_status)
            print(f"\n[+] Patient status updated to '{new_status}'.")
        else:
            print("Invalid choice selection.")

    except ValueError:
        print("Invalid ID format.")

def delete_patient_ui(db):
    print_header("DELETE PATIENT RECORD")
    try:
        p_id = int(input("Enter Patient ID to Delete: "))
        patient = db.search_patient_by_id(p_id)
        if not patient:
            print(f"[-] No patient found with ID: {p_id}")
            return

        confirm = input(f"Are you sure you want to delete patient '{patient[1]}'? (y/n): ").lower()
        if confirm == 'y':
            db.delete_patient(p_id)
            print("\n[+] Record deleted successfully.")
        else:
            print("\n[-] Deletion cancelled.")

    except ValueError:
        print("Invalid ID format.")

def main():
    db = Database()

    while True:
        print_header("HOSPITAL PATIENT MANAGEMENT SYSTEM")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Search Patient by ID")
        print("4. Update Patient Info")
        print("5. Discharge / Change Status")
        print("6. Delete Patient Record")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            add_patient_ui(db)
        elif choice == "2":
            view_all_patients_ui(db)
        elif choice == "3":
            search_patient_ui(db)
        elif choice == "4":
            update_patient_ui(db)
        elif choice == "5":
            update_status_ui(db)
        elif choice == "6":
            delete_patient_ui(db)
        elif choice == "7":
            db.close()
            print("\nExiting system. Goodbye!")
            sys.exit()
        else:
            print("\n[-] Invalid option. Please select between 1 and 7.")

if __name__ == "__main__":
    main()
