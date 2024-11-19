import cherrypy
from app.controllers import courses, requirements, students

class ISATApp:
    @cherrypy.expose
    def index(self):
        return "Welcome to the ISAT Course Finder!"

# Mount controllers as routes
cherrypy.tree.mount(ISATApp(), '/')
cherrypy.tree.mount(courses.CourseController(), '/courses')
cherrypy.tree.mount(requirements.RequirementController(), '/requirements')
cherrypy.tree.mount(students.StudentController(), '/students')

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
