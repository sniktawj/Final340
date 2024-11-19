import cherrypy
import mysql.connector
from mysql.connector import Error

class RequirementController:
    def __init__(self):
        # Database connection details
        self.db_config = {
            'host': 'localhost',
            'user': 'root',       # Replace with your MySQL username
            'password': 'StrongPassword123!', # Replace with your MySQL password
            'database': 'ISAT_Courses'  # Replace with your database name
        }

    def connect_db(self):
        """Establish a database connection."""
        try:
            connection = mysql.connector.connect(**self.db_config)
            return connection
        except Error as e:
            cherrypy.log(f"Error connecting to database: {e}")
            return None

    @cherrypy.expose
    def index(self):
        return """
        <html>
            <head>
                <title>Requirements</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin-top: 50px;
                        background-color: #F4F4F4;
                    }
                    h1 {
                        color: #450084; /* JMU Purple */
                    }
                    form {
                        margin: 20px;
                    }
                    input[type="text"] {
                        padding: 10px;
                        width: 300px;
                        margin: 10px 0;
                    }
                    input[type="submit"] {
                        background-color: #C79700; /* JMU Gold */
                        border: none;
                        padding: 10px 20px;
                        color: white;
                        font-size: 16px;
                        border-radius: 5px;
                        cursor: pointer;
                    }
                    input[type="submit"]:hover {
                        background-color: #450084; /* JMU Purple */
                    }
                    table {
                        margin: 20px auto;
                        border-collapse: collapse;
                        width: 80%;
                    }
                    th, td {
                        border: 1px solid #ddd;
                        padding: 10px;
                        text-align: left;
                    }
                    th {
                        background-color: #C79700;
                        color: white;
                    }
                </style>
            </head>
            <body>
                <h1>Check Program Requirements</h1>
                <form method="get" action="search">
                    <label for="program">Enter Program or Track:</label><br>
                    <input type="text" id="program" name="program" placeholder="e.g., Biotechnology"><br>
                    <input type="submit" value="Search Requirements">
                </form>
            </body>
        </html>
        """

    @cherrypy.expose
    def search(self, program=None):
        """Search and display the requirements for a given program."""
        if not program:
            return "Please provide a program name."

        connection = self.connect_db()
        if not connection:
            return "Error connecting to the database."

        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT course_id, course_name, credit_hours 
                FROM requirements 
                WHERE program = %s
            """
            cursor.execute(query, (program,))
            results = cursor.fetchall()

            if not results:
                return f"<h2>No requirements found for program: {program}</h2>"

            # Generate HTML table for results
            html = f"""
            <html>
                <head>
                    <title>{program} Requirements</title>
                </head>
                <body>
                    <h1>Requirements for {program}</h1>
                    <table>
                        <thead>
                            <tr>
                                <th>Course ID</th>
                                <th>Course Name</th>
                                <th>Credit Hours</th>
                            </tr>
                        </thead>
                        <tbody>
            """
            for row in results:
                html += f"""
                            <tr>
                                <td>{row['course_id']}</td>
                                <td>{row['course_name']}</td>
                                <td>{row['credit_hours']}</td>
                            </tr>
                """
            html += """
                        </tbody>
                    </table>
                    <a href="/requirements">Search Again</a>
                </body>
            </html>
            """
            return html
        except Error as e:
            cherrypy.log(f"Error fetching requirements: {e}")
            return "An error occurred while fetching the requirements."
        finally:
            connection.close()
