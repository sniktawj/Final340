from app.models.database import get_db_connection

def get_major_requirements(major_id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Requirements WHERE MajorID = %s", (major_id,))
    requirements = cursor.fetchall()
    db.close()
    return requirements
