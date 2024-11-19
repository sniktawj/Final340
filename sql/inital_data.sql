-- Create the database
CREATE DATABASE IF NOT EXISTS ISAT_Courses;
USE ISAT_Courses;

-- Table for Courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    CourseName VARCHAR(255) NOT NULL,
    Credits INT NOT NULL,
    Description TEXT
);

-- Table for Students
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    MajorID INT NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE
);

-- Table for Major Requirements
CREATE TABLE Requirements (
    RequirementID INT AUTO_INCREMENT PRIMARY KEY,
    MajorID INT NOT NULL,
    CourseID INT NOT NULL,
    RequirementType ENUM('Core', 'Elective') NOT NULL,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Table for Completed Courses
CREATE TABLE CompletedCourses (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT NOT NULL,
    CourseID INT NOT NULL,
    CompletionDate DATE NOT NULL,
    Grade VARCHAR(5),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Insert sample data into Courses
INSERT INTO Courses (CourseName, Credits, Description) VALUES
('ISAT 101 - Foundations of Integrated Science and Technology', 3, 'Introduction to ISAT concepts.'),
('ISAT 252 - Programming and Problem Solving', 4, 'Basic programming in Python and problem-solving skills.'),
('ISAT 321 - Systems Thinking and Analysis', 3, 'Principles of systems analysis.'),
('ISAT 459 - Biotechnology Applications', 4, 'Advanced topics in biotechnology.');

-- Insert sample data into Students
INSERT INTO Students (Name, MajorID, Email) VALUES
('Alice Johnson', 1, 'alice.johnson@example.com'),
('Bob Smith', 1, 'bob.smith@example.com');

-- Insert sample data into Requirements
INSERT INTO Requirements (MajorID, CourseID, RequirementType) VALUES
(1, 1, 'Core'),
(1, 2, 'Core'),
(1, 3, 'Core'),
(1, 4, 'Elective');

-- Insert sample data into Completed Courses
INSERT INTO CompletedCourses (StudentID, CourseID, CompletionDate, Grade) VALUES
(1, 1, '2023-05-15', 'A'),
(1, 2, '2023-12-01', 'B'),
(2, 1, '2023-04-20', 'B+');
