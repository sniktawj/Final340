import cherrypy
from app.models.courses import get_all_courses
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('app/templates'))

class CourseController:
    @cherrypy.expose
    def index(self):
        courses = get_all_courses()
        template = env.get_template('courses.html')
        return template.render(courses=courses)
