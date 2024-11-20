from app.models.database import db

class Registration:
    """Handles registration logic for students and courses."""

    @staticmethod
    def add_registration(student_id, course_id, semester, year, status="Registered"):
        """
        Adds a new registration record.
        
        Args:
            student_id (int): ID of the student registering.
            course_id (int): ID of the course being registered for.
            semester (str): Semester of the registration (e.g., 'Spring').
            year (int): Year of the registration.
            status (str): Registration status ('Registered', 'Waitlisted', or 'Dropped'). Default is 'Registered'.
        
        Returns:
            int: ID of the newly created registration record.
        """
        query = """
        INSERT INTO Registration (StudentID, CourseID, Semester, Year, RegistrationStatus)
        VALUES (%s, %s, %s, %s, %s)
        """
        db.execute(query, (student_id, course_id, semester, year, status))
        return db.lastrowid

    @staticmethod
    def get_registration_by_student(student_id):
        """
        Fetches all registration records for a given student.
        
        Args:
            student_id (int): ID of the student.
        
        Returns:
            list: List of dictionaries containing registration data.
        """
        query = """
        SELECT r.RegistrationID, r.Semester, r.Year, r.RegistrationStatus, 
               c.CourseName, c.Credits
        FROM Registration r
        JOIN Courses c ON r.CourseID = c.CourseID
        WHERE r.StudentID = %s
        """
        return db.fetch_all(query, (student_id,))

    @staticmethod
    def update_registration_status(registration_id, status):
        """
        Updates the status of an existing registration record.
        
        Args:
            registration_id (int): ID of the registration record.
            status (str): New registration status ('Registered', 'Waitlisted', or 'Dropped').
        """
        query = """
        UPDATE Registration
        SET RegistrationStatus = %s
        WHERE RegistrationID = %s
        """
        db.execute(query, (status, registration_id))

    @staticmethod
    def delete_registration(registration_id):
        """
        Deletes a registration record.
        
        Args:
            registration_id (int): ID of the registration record to delete.
        """
        query = "DELETE FROM Registration WHERE RegistrationID = %s"
        db.execute(query, (registration_id,))
