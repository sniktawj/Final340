-- Create the database
CREATE DATABASE IF NOT EXISTS ISAT_Courses1;
USE ISAT_Courses1;

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
