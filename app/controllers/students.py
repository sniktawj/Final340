import cherrypy
from app.models.students import get_student_data
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('app/templates'))

class StudentController:
    @cherrypy.expose
    def index(self, student_id=None):
        if not student_id:
            return "Please provide a student ID."
        student = get_student_data(student_id)
        template = env.get_template('plan.html')
        return template.render(student=student)
