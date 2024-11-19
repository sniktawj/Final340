import cherrypy
from app.models.courses import get_all_courses

class CourseController:
    @cherrypy.expose
    def index(self):
        courses = get_all_courses()
        return str(courses)  # Replace with a rendered template
