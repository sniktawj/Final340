import cherrypy

class StudentController:
    @cherrypy.expose
    def index(self):
        # Return a form for user input
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Student Search</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 50px;
                    background-color: #f4f4f4;
                }
                .form-container {
                    display: inline-block;
                    background: #fff;
                    padding: 20px;
                    border-radius: 5px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }
                input[type="text"] {
                    width: 80%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                button {
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <div class="form-container">
                <h2>Find Student Details</h2>
                <form method="get" action="/students/details">
                    <label for="student_id">Enter Student ID:</label><br>
                    <input type="text" id="student_id" name="student_id" placeholder="ISAT-2024-XXXX" required><br>
                    <button type="submit">Search</button>
                </form>
            </div>
        </body>
        </html>
        """
    
    @cherrypy.expose
    def details(self, student_id=None):
        if not student_id:
            return "No Student ID provided. Please go back and enter a valid ID."

        # Retrieve student details from the database
        db_connection = mysql.connector.connect(
            host="localhost", user="your_user", password="your_password", database="your_database"
        )
        cursor = db_connection.cursor()
        cursor.execute("SELECT student_id, name, email, year FROM students WHERE student_id = %s", (student_id,))
        student = cursor.fetchone()
        cursor.close()
        db_connection.close()

        if student:
            return f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Student Details</title>
            </head>
            <body>
                <h2>Student Details</h2>
                <p><strong>Student ID:</strong> {student[0]}</p>
                <p><strong>Name:</strong> {student[1]}</p>
                <p><strong>Email:</strong> {student[2]}</p>
                <p><strong>Year:</strong> {student[3]}</p>
                <a href="/students">Search Again</a>
            </body>
            </html>
            """
        else:
            return f"No details found for Student ID: {student_id}. <a href='/students'>Try again</a>"
