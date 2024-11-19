from app.models.database import get_db_connection

def get_student_data(student_id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Students WHERE StudentID = %s", (student_id,))
    student = cursor.fetchone()
    db.close()
    return student
