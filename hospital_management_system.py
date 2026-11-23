# HERE I WILL MAKE HOSPITAL/CLINIC MANAGEMENT SYSTEM 

# Patient Registration
# Doctor management
# Appointment Booking 
# Paitent History 
# Billing

# Tables : Patient, Doctors , Appointment, Bills ta

import mysql.connector
import getpass
DB_PASSWORD = getpass.getpass("Enter MySQL password: ")

# MySQL Database Connection Setup
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",      
        password=DB_PASSWORD,
        database = "Hospital_Management_System"   
    )

# --- PATIENT FUNCTIONS --- 
def register_patient():

    try : 
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        contact = int(input("Enter Contact (digits): "))
        address = input("Enter Address: ")
        
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Patients (patient_name, age, gender, contact, address) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, age, gender, contact, address))
        conn.commit()
        print("--> Patient Registered Successfully in Database!\n")
        cursor.close()
        conn.close()

    except Exception :
        print("Something Went Wrong ....")
        print("Try Again With Correct Input ....")

def view_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Patients")
    rows = cursor.fetchall()
    print("\n--- PATIENT LIST ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Gender: {row[3]} | Contact: {row[4]} | Address: {row[5]}")
    print()
    cursor.close()
    conn.close()

def search_patient():
    keyword = input("Enter Patient Name or ID to Search: ")
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Patients WHERE patient_name LIKE %s OR patient_id = %s"
    cursor.execute(query, ('%' + keyword + '%', keyword))
    rows = cursor.fetchall()
    print("\n--- SEARCH RESULTS ---")

    if rows == [] :
        print('Patient Not Found...')

    else :
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Gender: {row[3]} | Contact: {row[4]}")
        print()
        cursor.close()
        conn.close()

def update_patient():

    try :
        p_id = input("Enter Patient ID to Update: ")
        contact = int(input("Enter New Contact: "))
        address = input("Enter New Address: ")
        
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE Patients SET contact = %s, address = %s WHERE patient_id = %s"
        cursor.execute(query, (contact, address, p_id))
        conn.commit()
        print("--> Patient Updated Successfully in Database!\n")
        cursor.close()
        conn.close()

    except Exception :
        print('Something Went Wrong...')

def delete_patient():

    try :
        p_id = input("Enter Patient ID to Delete: ")
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Patients WHERE patient_id = %s"
        cursor.execute(query, (p_id,))
        conn.commit()
        print("--> Patient Deleted Successfully from Database!\n")
        cursor.close()
        conn.close()

    except Exception :
        print('Patient ID Not found...')

# --- DOCTOR FUNCTIONS ---
def add_doctor():

    try :
        name = input("Enter Doctor Name: ")
        spec = input("Enter Specialization: ")
        contact = int(input("Enter Contact (digits): "))
        avail = input("Enter Availability: ")
        
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Doctors (doctor_name, specialization, contact, availability) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, spec, contact, avail))
        conn.commit()
        print("--> Doctor Added Successfully in Database!\n")
        cursor.close()
        conn.close()

    except Exception :
        print('Something Went Wrong...')

def view_doctors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Doctors")
    rows = cursor.fetchall()
    print("\n--- DOCTOR LIST ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Specialization: {row[2]} | Contact: {row[3]} | Available: {row[4]}")
    print()
    cursor.close()
    conn.close()

def search_doctor():

    try :
        keyword = input("Enter Doctor Name or Specialization to Search: ")
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Doctors WHERE doctor_name LIKE %s OR specialization LIKE %s"
        cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))
        rows = cursor.fetchall()
        print("\n--- SEARCH RESULTS ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Specialization: {row[2]} | Available: {row[4]}")
        print()
        cursor.close()
        conn.close()

    except Exception :
        print('Doctor Not Found...')

    
def update_doctor():

    try :

        d_id = input("Enter Doctor ID to Update: ")
        avail = input("Enter New Availability: ")
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE Doctors SET availability = %s WHERE doctor_id = %s"
        cursor.execute(query, (avail, d_id))
        conn.commit()
        print("--> Doctor Updated Successfully in Database!\n")
        cursor.close()
        conn.close()

    except Exception :
        print('Invalid Doctor ID ...')


def delete_doctor():

    try :
        d_id = input("Enter Doctor ID to Delete: ")
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Doctors WHERE doctor_id = %s"
        cursor.execute(query, (d_id,))
        conn.commit()
        print("--> Doctor Deleted Successfully from Database!\n")
        cursor.close()
        conn.close()

    except Exception :
        print('Invalid Doctor ID ...')
    


# --- APPOINTMENT FUNCTIONS ---
def book_appointment():

    try :
        p_id = input("Enter Patient ID: ")
        d_id = input("Enter Doctor ID: ")
        date = input("Enter Appointment Date (YYYY-MM-DD): ")
        status = "Pending"
        
        conn = get_connection()
        cursor = conn.cursor()
        try:
            query = "INSERT INTO Appointments (patient_id, doctor_id, appointment_date, status) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (p_id, d_id, date, status))
            conn.commit()
            print("-> Appointment Booked Successfully in Database!\n")
        except mysql.connector.Error as err:
            print(f"--> Database Error: {err}\n")
        cursor.close()
        conn.close()

    except Exception :
        print('Something Went Wrong...')


def view_appointments():
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
        SELECT a.appointment_id, p.patient_name, d.doctor_name, a.appointment_date, a.status 
        FROM Appointments as a
        JOIN Patients as p ON a.patient_id = p.patient_id
        JOIN Doctors as d ON a.doctor_id = d.doctor_id
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    print("\n--- APPOINTMENTS LIST ---")
    for row in rows:
        print(f"Appt ID: {row[0]} | Patient: {row[1]} | Doctor: {row[2]} | Date: {row[3]} | Status: {row[4]}")
    print()
    cursor.close()
    conn.close()

def search_appointment():
    app_id = input("Enter Appointment ID: ")
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
        SELECT a.appointment_id, p.patient_name, d.doctor_name, a.appointment_date, a.status 
        FROM Appointments a
        JOIN Patients p ON a.patient_id = p.patient_id
        JOIN Doctors d ON a.doctor_id = d.doctor_id
        WHERE a.appointment_id = %s
    '''
    cursor.execute(query, (app_id,))
    row = cursor.fetchone()
    if row:
        print(f"\nAppt ID: {row[0]} | Patient: {row[1]} | Doctor: {row[2]} | Date: {row[3]} | Status: {row[4]}\n")
    else:
        print("--> Appointment not found!\n")
    cursor.close()
    conn.close()

def cancel_appointment():

    try :
        app_id = input("Enter Appointment ID to Cancel: ")
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE Appointments SET status = 'Cancelled' WHERE appointment_id = %s"
        cursor.execute(query, (app_id,))
        conn.commit()
        print("--> Appointment Cancelled!\n")
        cursor.close()
        conn.close()

    except Exception :
        print('Wrong Appointment ID ...')


def complete_appointment():

    try :
        app_id = input("Enter Appointment ID to Complete: ")
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE Appointments SET status = 'Completed' WHERE appointment_id = %s"
        cursor.execute(query, (app_id,))
        conn.commit()
        print("--> Appointment Marked as Completed!\n")
        cursor.close()
        conn.close()

    except Exception :
        print('Wrong Appointment ID ...')
        
def view_patient_history():
    p_id = input("Enter Patient ID to view history: ")
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Pehle Patient ki personal details Li.....
    cursor.execute("SELECT patient_name, age, gender, contact FROM Patients WHERE patient_id = %s", (p_id,))
    patient = cursor.fetchone()
    
    if not patient:
        print("--> Patient not found!\n")
        cursor.close()
        conn.close()
        return
        
    print(f"\n=========================================")
    print(f"       PATIENT COMPLETE PROFILE          ")
    print(f"=========================================")
    print(f"Patient Name : {patient[0]}")
    print(f"Age          : {patient[1]}")
    print(f"Gender       : {patient[2]}")
    print(f"Contact No.  : {patient[3]}")
    print("-----------------------------------------")
    
    # 2. Appointment aur Doctor ki details fetch Ki
    cursor.execute('''
        SELECT a.appointment_id, d.doctor_name, a.appointment_date, a.status 
        FROM Appointments a
        JOIN Doctors d ON a.doctor_id = d.doctor_id
        WHERE a.patient_id = %s
    ''', (p_id,))
    appointments = cursor.fetchall()
    
    print("--- APPOINTMENT HISTORY ---")
    if appointments:
        for appt in appointments:
            print(f"Appt ID: {appt[0]} | Doctor: {appt[1]} | Date: {appt[2]} | Status: {appt[3]}")
    else:
        print("No appointments found for this patient.")
        
    print("-----------------------------------------")
    
    # 3. Bills aur Bill status fetch karein
    cursor.execute('''
        SELECT bill_id, amount, bill_date, status 
        FROM Bills 
        WHERE patient_id = %s
    ''', (p_id,))
    bills = cursor.fetchall()
    
    print("--- BILLING HISTORY ---")
    if bills:
        for bill in bills:
            print(f"Bill ID: {bill[0]} | Amount: ₹{bill[1]} | Date: {bill[2]} | Status: {bill[3]}")
    else:
        print("No bills found for this patient.")
        
    print("=========================================\n")
    
    cursor.close()
    conn.close()


# --- BILLING & REPORTS ---
def create_bill():
    p_id = input("Enter Patient ID: ")
    amount = int(input("Enter Bill Amount: "))
    date = input("Enter Bill Date (YYYY-MM-DD): ")
    status = input("Enter Bill Status Paid/Pending : ")
    
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO Bills (patient_id, amount, bill_date, status) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (p_id, amount, date, status))
        conn.commit()
        print("--> Bill Created Successfully in Database!\n")
    except mysql.connector.Error as err:
        print(f"--> Database Error: {err}\n")
    cursor.close()
    conn.close()

def view_bills():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Bills")
    rows = cursor.fetchall()
    print("\n--- ALL BILLS ---")
    for row in rows:
        print(f"Bill ID: {row[0]} | Patient ID: {row[1]} | Amount: {row[2]} | Date: {row[3]} | Status: {row[4]}")
    print()
    cursor.close()
    conn.close()

def calculate_total_revenue():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM Bills")
    total = cursor.fetchone()[0]
    print(f"\nTotal Hospital Revenue: ₹ {total if total else 0.0}\n")
    cursor.close()
    conn.close()

def hospital_reports():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Patients")
    p_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM Doctors")
    d_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM Appointments")
    a_count = cursor.fetchone()[0]
    
    print("\n--- HOSPITAL SUMMARY REPORT ---")
    print(f"Total Registered Patients : {p_count}")
    print(f"Total Doctors Available   : {d_count}")
    print(f"Total Appointments Booked : {a_count}\n")
    cursor.close()
    conn.close()


# --- MAIN MENU LOOP ---
def main():
    while True:
        print("========================================")
        print("     HOSPITAL / CLINIC MANAGEMENT       ")
        print("========================================")
        print("1. Register Patient        11. Book Appointment")
        print("2. View Patients           12. View Appointments")
        print("3. Search Patient          13. Search Appointment")
        print("4. Update Patient          14. Cancel Appointment")
        print("5. Delete Patient          15. Complete Appointment")
        print("                           16. View Patient History")
        print("6. Add Doctor              17. Create Bill")
        print("7. View Doctors            18. View Bills")
        print("8. Search Doctor           19. Calculate Total Revenue")
        print("9. Update Doctor           20. Hospital Reports")
        print("10. Delete Doctor          21. Exit")
        print("========================================")
        
        choice = input("Enter your choice (1-21): ")
        
        if   choice == '1': register_patient()
        elif choice == '2': view_patients()
        elif choice == '3': search_patient()
        elif choice == '4': update_patient()
        elif choice == '5': delete_patient()
        elif choice == '6': add_doctor()
        elif choice == '7': view_doctors()
        elif choice == '8': search_doctor()
        elif choice == '9': update_doctor()
        elif choice == '10': delete_doctor()
        elif choice == '11': book_appointment()
        elif choice == '12': view_appointments()
        elif choice == '13': search_appointment()
        elif choice == '14': cancel_appointment()
        elif choice == '15': complete_appointment()
        elif choice == '16': view_patient_history()
        elif choice == '17': create_bill()
        elif choice == '18': view_bills()
        elif choice == '19': calculate_total_revenue()
        elif choice == '20': hospital_reports()
        elif choice == '21':
            print("Exiting System. Goodbye!")
            break
        else:
            print("Invalid Choice! Please enter a number between 1 and 21.\n")

if __name__ == "__main__":
    main()
