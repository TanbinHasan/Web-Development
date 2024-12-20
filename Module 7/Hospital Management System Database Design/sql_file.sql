CREATE DATABASE HospitalManagementSystem;
USE HospitalManagementSystem;

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Location VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Doctors (
    DoctorID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Specialization VARCHAR(50) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    DepartmentID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,
    DoctorID INT,
    PatientID INT,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL,
    CancellationReason VARCHAR(255),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

-- Insert dummy data
INSERT INTO Departments (Name, Location) VALUES 
('Cardiology', 'Building A'),
('Neurology', 'Building B'),
('Pediatrics', 'Building C'),
('Orthopedics', 'Building D'),
('Radiology', 'Building E');

INSERT INTO Doctors (Name, Specialization, Phone, DepartmentID) VALUES 
('Dr. Smith', 'Cardiologist', '1234567890', 1),
('Dr. Brown', 'Neurologist', '1234567891', 2),
('Dr. Taylor', 'Pediatrician', '1234567892', 3),
('Dr. Wilson', 'Orthopedic', '1234567893', 4),
('Dr. Lee', 'Radiologist', '1234567894', 5);

INSERT INTO Patients (Name, Age, Gender, Phone) VALUES 
('Alice Johnson', 30, 'Female', '9876543210'),
('Bob Smith', 45, 'Male', '9876543211'),
('Charlie Brown', 10, 'Male', '9876543212'),
('Diana Prince', 28, 'Female', '9876543213'),
('Edward Kim', 60, 'Male', '9876543214');

INSERT INTO Appointments (DoctorID, PatientID, Date, Time, Status, Notes) VALUES 
(1, 1, '2024-12-21', '09:00:00', 'Scheduled', 'Routine check-up'),
(2, 2, '2024-12-22', '10:00:00', 'Scheduled', 'Follow-up for headache'),
(3, 3, '2024-12-23', '11:00:00', 'Scheduled', 'Child vaccination'),
(4, 4, '2024-12-24', '12:00:00', 'Cancelled', 'Cancelled by patient'),
(5, 5, '2024-12-25', '13:00:00', 'Completed', 'MRI scan follow-up');
