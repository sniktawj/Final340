from app.models.registration import Registration
import cherrypy

class RegistrationController:
    """Handles HTTP requests for course registration."""

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def add(self, student_id, course_id, semester, year, status="Registered"):
        """Adds a new registration."""
        try:
            registration_id = Registration.add_registration(student_id, course_id, semester, year, status)
            return {"success": True, "registration_id": registration_id}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def student(self, student_id):
        """Fetches registrations for a student."""
        try:
            registrations = Registration.get_registration_by_student(student_id)
            return {"success": True, "registrations": registrations}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def update(self, registration_id, status):
        """Updates registration status."""
        try:
            Registration.update_registration_status(registration_id, status)
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def delete(self, registration_id):
        """Deletes a registration."""
        try:
            Registration.delete_registration(registration_id)
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}
