from app.models.database import get_db_connection

def get_all_courses():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Courses")
    courses = cursor.fetchall()
    db.close()
    return courses
