# Step 1: Create lists for patients and bills
patients = [] 
bills = []   

# Step 2: Create a dictionary for health issues mapping to respective doctors
health_issues_to_doctors = {
    "fever": "General Physician",
    "cough": "General Physician",
    "headache": "Neurologist",
    "chest pain": "Cardiologist",
    "stomach ache": "Gastroenterologist",
    "fracture": "Orthopedic",
    "skin rash": "Dermatologist"
}

# Step 3: Create a dictionary for services and respective cost (now in Euros)
services_cost = {
    "consultation": 50,
    "blood test": 120,
    "x-ray": 180,
    "ultrasound": 250,
    "ecg": 90,
    "injection": 25
}

# Step 4: Print welcome message
print("\nWelcome to Hospital Management System (Lite Edition)")

# Step 5: Main program loop
while True:
    print("\nMain Menu:")
    print("1. Register New Patient")
    print("2. View All Patients")
    print("3. Search Patient by Doctor or Symptoms")
    print("4. Generate Bill for Patient")
    print("5. Show Unique Symptoms")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Option 1: Register new patient
    if choice == "1":
        print("\n--- New Patient Registration ---")
        name = input("Patient Name: ")
        age = input("Age: ")
        gender = input("Gender (M/F): ").upper()
        symptoms = input("Symptoms (comma separated): ").lower().split(",")

        # Determine doctor based on primary symptom
        primary_symptom = symptoms[0].strip()
        doctor = health_issues_to_doctors.get(primary_symptom, "General Physician")

        # Create patient record
        patient = {
            "name": name,
            "age": age,
            "gender": gender,
            "symptoms": [s.strip() for s in symptoms],
            "doctor": doctor,
            "services": []
        }

        patients.append(patient)
        print(f"\nPatient {name} registered successfully with {doctor}!")

    # Option 2: View all patients
    elif choice == "2":
        print("\n--- All Registered Patients ---")
        if not patients:
            print("No patients registered yet.")
        else:
            for idx, patient in enumerate(patients, 1):
                print(f"\nPatient {idx}:")
                print(f"Name: {patient['name']}")
                print(f"Age: {patient['age']}")
                print(f"Gender: {patient['gender']}")
                print(f"Symptoms: {', '.join(patient['symptoms'])}")
                print(f"Doctor: {patient['doctor']}")

    # Option 3: Search patient by doctor or symptoms
    elif choice == "3":
        print("\n--- Search Patients ---")
        search_term = input("Enter doctor name or symptom to search: ").lower()

        found_patients = []
        for patient in patients:
            if (search_term in patient['doctor'].lower() or 
                any(search_term in s for s in patient['symptoms'])):
                found_patients.append(patient)

        if not found_patients:
            print("No patients found matching your search.")
        else:
            print(f"\nFound {len(found_patients)} patient(s):")
            for p in found_patients:
                print(f"{p['name']} (Doctor: {p['doctor']}, Symptoms: {', '.join(p['symptoms'])})")

    # Option 4: Generate bill for patient
    elif choice == "4":
        print("\n--- Generate Patient Bill ---")
        if not patients:
            print("No patients registered yet.")
            continue

        print("Select patient:")
        for idx, patient in enumerate(patients, 1):
            print(f"{idx}. {patient['name']}")

        try:
            patient_idx = int(input("Enter patient number: ")) - 1
            if patient_idx < 0 or patient_idx >= len(patients):
                raise ValueError

            patient = patients[patient_idx]
            print(f"\nGenerating bill for {patient['name']}")

            # Display available services
            print("\nAvailable Services:")
            for service, cost in services_cost.items():
                print(f"{service.title()}: €{cost}")

            # Select services
            selected_services = []
            while True:
                service = input("\nEnter service to add (or 'done' to finish): ").lower()
                if service == "done":
                    break
                if service in services_cost:
                    selected_services.append(service)
                    print(f"Added {service} to bill.")
                else:
                    print("Invalid service. Please try again.")

            # Calculate total
            total = sum(services_cost[service] for service in selected_services)

            # Create bill record
            bill = {
                "patient_name": patient['name'],
                "services": selected_services,
                "total": total
            }
            bills.append(bill)

            # Update patient record
            patient['services'].extend(selected_services)

            # Print bill
            print("\n--- Final Bill ---")
            print(f"Patient: {patient['name']}")
            print("Services:")
            for service in selected_services:
                print(f"- {service.title()}: €{services_cost[service]}")
            print(f"\nTOTAL: €{total}")

        except (ValueError, IndexError):
            print("Invalid patient selection. Please try again.")

    # Option 5: Show unique symptoms
    elif choice == "5":
        print("\n--- Unique Symptoms Across All Patients ---")
        unique_symptoms = set()

        for patient in patients:
            for symptom in patient['symptoms']:
                unique_symptoms.add(symptom.strip())

        if not unique_symptoms:
            print("No symptoms recorded yet.")
        else:
            print(", ".join(sorted(unique_symptoms)))

    # Option 6: Exit program
    elif choice == "6":
        print("\nThank you for using Hospital Management System. Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please enter a number between 1-6.")
