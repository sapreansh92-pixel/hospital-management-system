Create database Hospital_Management_System ;

Use Hospital_Management_System ;

Create Table Patients
(patient_id int unsigned primary key auto_increment ,
patient_name varchar(50) not null , 
age int not null , 
gender varchar(20) not null , 
contact bigint not null, 
address text not null  ) ; 

Create Table Doctors 
(doctor_id int unsigned primary key auto_increment ,
doctor_name varchar(50) not null , 
specialization varchar(70) not null , 
contact bigint not null , 
availability tinytext 
) ; 

Create Table Appointments
(appointment_id int unsigned primary key auto_increment ,
patient_id int unsigned ,
doctor_id int unsigned,
appointment_date date ,
status varchar(30) default "Pending" ,
foreign key (patient_id) references Patients (patient_id),
foreign key (doctor_id) references Doctors (doctor_id) ON UPDATE CASCADE
) ; 
 
Create Table Bills 
(bill_id int unsigned primary key auto_increment ,
patient_id int unsigned ,
amount int ,
bill_date DATE , 
status varchar(30) ,
foreign key (patient_id) references Patients(patient_id) ON UPDATE CASCADE
) ;

-- HERE I INSERT DATA  IN THE TABLE --

INSERT INTO Patients (patient_name, age, gender, contact, address) VALUES 
('Aarav Sharma', 28, 'Male', 9876543210, 'Delhi'),
('Priya Verma', 34, 'Female', 9123456789, 'Mumbai'),
('Rohan Gupta', 22, 'Male', 9988776655, 'Bangalore'),
('Ananya Singh', 29, 'Female', 9811223344, 'Kolkata'),
('Vikram Malhotra', 45, 'Male', 9700112233, 'Chennai'),
('Neha Joshi', 31, 'Female', 9655443322, 'Pune'),
('Amit Kumar', 39, 'Male', 9544332211, 'Hyderabad'),
('Pooja Mehta', 26, 'Female', 9433221100, 'Ahmedabad'),
('Rahul Verma', 50, 'Male', 9322110099, 'Jaipur'),
('Sneha Reddy', 27, 'Female', 9211009988, 'Lucknow');

INSERT INTO Doctors (doctor_name, specialization, contact, availability) VALUES 
('Dr. Ramesh Rao', 'Cardiologist', 9800011122, 'Mon-Fri 10AM-2PM'),
('Dr. Sunita Williams', 'Dermatologist', 9800022233, 'Mon-Sat 12PM-4PM'),
('Dr. Manoj Bajpai', 'Orthopedic', 9800033344, 'Tue-Sun 9AM-1PM'),
('Dr. Kavita Devi', 'Pediatrician', 9800044455, 'Mon-Fri 2PM-6PM'),
('Dr. Alok Nath', 'Neurologist', 9800055566, 'Wed-Sun 10AM-3PM'),
('Dr. Meenakshi Sundaram', 'General Physician', 9800066677, 'Mon-Sat 9AM-5PM'),
('Dr. Suresh Raina', 'Eye Specialist', 9800077788, 'Mon-Thu 11AM-3PM'),
('Dr. Deepika Padukone', 'Psychiatrist', 9800088899, 'Fri-Sun 10AM-2PM'),
('Dr. Harsha Bhogle', 'Ophthalmologist', 9800099900, 'Mon-Fri 1AM-4PM'),
('Dr. Zoya Akhtar', 'Gynecologist', 9800012345, 'Tue-Sat 9AM-1PM');

INSERT INTO Appointments (patient_id, doctor_id, appointment_date, status) VALUES 
(1, 1, '2026-10-22', 'Pending'),
(2, 3, '2026-10-22', 'Completed'),
(3, 2, '2026-10-23', 'Pending'),
(4, 5, '2026-10-23', 'Cancelled'),
(5, 4, '2026-10-24', 'Completed'),
(6, 6, '2026-10-24', 'Pending'),
(7, 8, '2026-10-25', 'Pending'),
(8, 7, '2026-10-25', 'Completed'),
(9, 10, '2026-10-26', 'Pending'),
(10, 9, '2026-10-26', 'Completed');

INSERT INTO Bills (patient_id, amount, bill_date, status) VALUES 
(1, 1500.50, '2026-10-22', 'Paid'),
(2, 2000.00, '2026-10-22', 'Paid'),
(3, 800.00, '2026-10-23', 'Pending'),
(4, 3500.00, '2026-10-23', 'Paid'),
(5, 1200.00, '2026-10-24', 'Paid'),
(6, 500.00, '2026-10-24', 'Pending'),
(7, 2500.00, '2026-10-25', 'Paid'),
(8, 1800.00, '2026-10-25', 'Paid'),
(9, 3000.00, '2026-10-26', 'Pending'),
(10, 1000.00, '2026-10-26', 'Paid');

Drop Database hospital_management_system ;