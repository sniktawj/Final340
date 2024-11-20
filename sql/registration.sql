-- Table for Registration
CREATE TABLE Registration (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each registration record
    StudentID INT NOT NULL, -- Reference to the student
    CourseID INT NOT NULL, -- Reference to the course
    Semester ENUM('Spring', 'Summer', 'Fall', 'Winter') NOT NULL, -- Semester of registration
    Year YEAR NOT NULL, -- Year of registration
    RegistrationStatus ENUM('Registered', 'Waitlisted', 'Dropped') DEFAULT 'Registered', -- Status of the registration
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
